import os
import glob
import shutil

examples_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'biogeme_examples')

all_scripts = [x for x in glob.iglob(os.path.join(examples_folder, '*.py'))]

batch_job = []
for script in all_scripts:
    path, file = os.path.split(script)
    job, extension = os.path.splitext(file)

    # Create the folder to hold that script
    job_folder = os.path.join(path, job).replace('\\', '/')
    os.makedirs(job_folder)

    # move the script there
    shutil.move(script, os.path.join(job_folder, file))

    # If running on a Unix-based system, the command would have a single / (e.g. ...:/tmp/mr - w/tmp...)
    docker_command = 'docker run -v {}://tmp/mr -w //tmp/mr/{} biogeme pythonbiogeme {} ../swissmetro.dat\n'.format(examples_folder, job, job)
    batch_job.append(docker_command)

with open(os.path.join(examples_folder, 'docker_batch.bat'), 'w') as f:
    f.writelines(batch_job)
