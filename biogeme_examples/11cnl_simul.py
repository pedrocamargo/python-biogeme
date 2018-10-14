#######################################
#
# File: 11cnl_simul.py
# Author: Michel Bierlaire, EPFL
# Date: Wed Dec 21 13:24:57 2011
#
#######################################

from biogeme import *
from headers import *
from cnl import *
from loglikelihood import *
from statistics import *


#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed

ASC_TRAIN = Beta('ASC_TRAIN',0.0982524,-10,10,0 )

B_TIME = Beta('B_TIME',-0.776857,-10,10,0 )

B_COST = Beta('B_COST',-0.818896,-10,10,0 )

ALPHA_EXISTING = Beta('ALPHA_EXISTING',0.495081,0,1,0 )
ALPHA_PUBLIC = 1 - ALPHA_EXISTING

MU_EXISTING = Beta('MU_EXISTING',2.51485,1,10,0 )

ASC_SM = Beta('ASC_SM',0,-10,10,1 )

ASC_CAR = Beta('ASC_CAR',-0.240459,-10,10,0 )

MU_PUBLIC = Beta('MU_PUBLIC',4.11326,1,10,0 )

# Utility functions

#If the person has a GA (season ticket) her incremental cost is actually 0 
#rather than the cost value gathered from the
# network data. 
SM_COST =  SM_CO   * (  GA   ==  0  ) 
TRAIN_COST =  TRAIN_CO   * (  GA   ==  0  )

# For numerical reasons, it is good practice to scale the data to
# that the values of the parameters are around 1.0. 
# A previous estimation with the unscaled data has generated
# parameters around -0.01 for both cost and time. Therefore, time and
# cost are multipled my 0.01.

# The following statements are designed to preprocess the data. It is
# like creating a new columns in the data file. This should be
# preferred to the statement like
# TRAIN_TT_SCALED = TRAIN_TT / 100.0
# which will cause the division to be reevaluated again and again,
# throuh the iterations. For models taking a long time to estimate, it
# may make a significant difference.
 
TRAIN_TT_SCALED = DefineVariable('TRAIN_TT_SCALED', TRAIN_TT / 100.0)
TRAIN_COST_SCALED = DefineVariable('TRAIN_COST_SCALED', TRAIN_COST / 100)
SM_TT_SCALED = DefineVariable('SM_TT_SCALED', SM_TT / 100.0)
SM_COST_SCALED = DefineVariable('SM_COST_SCALED', SM_COST / 100)
CAR_TT_SCALED = DefineVariable('CAR_TT_SCALED', CAR_TT / 100)
CAR_CO_SCALED = DefineVariable('CAR_CO_SCALED', CAR_CO / 100)

V1 = ASC_TRAIN + B_TIME * TRAIN_TT_SCALED + B_COST * TRAIN_COST_SCALED
V2 = ASC_SM + B_TIME * SM_TT_SCALED + B_COST * SM_COST_SCALED
V3 = ASC_CAR + B_TIME * CAR_TT_SCALED + B_COST * CAR_CO_SCALED

# Associate utility functions with the numbering of alternatives
V = {1: V1,
     2: V2,
     3: V3}

# Associate the availability conditions with the alternatives
CAR_AV_SP =  DefineVariable('CAR_AV_SP',CAR_AV  * (  SP   !=  0  ))
TRAIN_AV_SP =  DefineVariable('TRAIN_AV_SP',TRAIN_AV  * (  SP   !=  0  ))

av = {1: TRAIN_AV_SP,
      2: SM_AV,
      3: CAR_AV_SP}

#Definition of nests:
alpha_existing = {1: ALPHA_EXISTING,
                  2:0.0,
                  3:1.0}

alpha_public = {1: ALPHA_PUBLIC,
                2: 1.0,
                3: 0.0}

nest_existing = MU_EXISTING, alpha_existing
nest_public = MU_PUBLIC, alpha_public
nests = nest_existing, nest_public

# The choice model is a cross-nested logit, with availability conditions
prob1 = cnl_avail(V,av,nests,1)
prob2 = cnl_avail(V,av,nests,2)
prob3 = cnl_avail(V,av,nests,3)

simulate = {'Prob. 1': prob1,
            'Prob. 2': prob2,
            'Prob. 3': prob3,
            'Choice 1': CHOICE == 1,
            'Choice 2': CHOICE == 2,
            'Choice 3': CHOICE == 3}


# Defines an iterator on the data
rowIterator('obsIter', '__dataFile__') 

# DEfine the likelihood function for the estimation
BIOGEME_OBJECT.SIMULATE = Enumerate(simulate,'obsIter')

# All observations verifying the following expression will not be
# considered for estimation
# The modeler here has developed the model only for work trips.  
# Observations such that the dependent variable CHOICE is 0 are also removed.
exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) + ( CHOICE == 0 )) > 0

BIOGEME_OBJECT.EXCLUDE = exclude

BIOGEME_OBJECT.FORMULAS['Train utility'] = V1
BIOGEME_OBJECT.FORMULAS['Swissmetro utility'] = V2
BIOGEME_OBJECT.FORMULAS['Car utility'] = V3
