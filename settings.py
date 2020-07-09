import os


SENDER_EMAIL = "sender@gmail.com"
SENDER_PASSWORD = "your gmail app password"
RECEIVER_EMAIL = "receiver@gmail.com"

directory = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2)
project_root_dir = directory[0] + "/" + directory[1] + "/" + directory[2]

venv_directory = directory[0] + "/" + directory[1]
python_location = venv_directory + '/bin/python3'
executive_file = directory[0] \
                 + "/" + directory[1] \
                 + "/" + directory[2] \
                 + '/spy.py'
cron_job_command = python_location + " " + executive_file
