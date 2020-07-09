from cronjob.scheduler import Scheduler
from settings import cron_job_command

if __name__ == "__main__":
    # Execute job
    scheduler = Scheduler(cron_job_command)
    scheduler.minutely_execution()
