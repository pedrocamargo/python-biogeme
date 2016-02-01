FROM dockerfile/python

RUN \
  curl -O http://biogeme.epfl.ch/distrib/biogeme-2.4.tar.gz && \
  tar xvzf biogeme-2.4.tar.gz && \
  cd biogeme-2.4 && \
  ./configure && \
  make && make install && \
  make clean
