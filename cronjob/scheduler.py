"""
    ----------------------------------------------------------------------------
    Scheduler module
    ----------------------------------------------------------------------------
    1. Can create cron jobs with specific time schedule

        Case	        Meaning
        @reboot	        Every boot
        @hourly	        0 * * * *
        @daily	        0 0 * * *
        @weekly	        0 0 * * 0
        @monthly	    0 0 1 * *
        @yearly	        0 0 1 1 *
    ----------------------------------------------------------------------------
    2. can remove all cron jobs
    ----------------------------------------------------------------------------
"""
from crontab import CronTab, CronItem


class Scheduler:
    """Scheduler class"""
    def __init__(self, command: str):
        """
        Here we will initiate a Cron
        and set the command
        :param command: command to execute
        """
        self.cron = CronTab(user=True)
        self.command = command

    def __create_cron_job(self) -> CronItem:
        """
        Create a new job and return it
        :return: job
        """
        job = self.cron.new(command=self.command)
        return job

    def minutely_execution(self) -> bool:
        """
        Execute job every minute
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.minute.every(1)
            job.enable()
            self.cron.write()
            print(job)
            if self.cron.render():
                print("done")
                return True
            print("failed")
            return False
        except Exception as error:
            print(error)
            return False

    def hourly_execution(self) -> bool:
        """
        Execute job every hour
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.minute.on(0)
            job.hour.during(0, 23)
            job.enable()
            self.cron.write()
            if self.cron.render():
                return True
            return False
        except Exception as error:
            print(error)
            return False

    def daily_execution(self) -> bool:
        """
        Execute job every day
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.minute.on(0)
            job.hour.on(0)
            job.enable()
            self.cron.write()
            if self.cron.render():
                return True
            return False
        except Exception as error:
            print(error)
            return False

    def weekly_execution(self) -> bool:
        """
        Execute job every week
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.minute.on(0)
            job.hour.on(0)
            job.dow.on(1)
            job.enable()
            self.cron.write()
            if self.cron.render():
                return True
            return False
        except Exception as error:
            print(error)
            return False

    def monthly_execution(self) -> bool:
        """
        Execute job every month
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.minute.on(0)
            job.hour.on(0)
            job.day.on(1)
            job.month.during(1, 12)
            job.enable()
            self.cron.write()
            if self.cron.render():
                return True
            return False
        except Exception as error:
            print(error)
            return False

    def yearly_execution(self) -> bool:
        """
        Execute job every year
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.minute.on(0)
            job.hour.on(0)
            job.month.on(12)
            job.enable()
            self.cron.write()
            if self.cron.render():
                return True
            return False
        except Exception as error:
            print(error)
            return False

    def execute_after_reboot(self) -> bool:
        """
        Execute job after every reboot
        :return:
        """
        try:
            job = self.__create_cron_job()
            job.every_reboot()
            job.enable()
            self.cron.write()
            if self.cron.render():
                return True
            return False
        except Exception as error:
            print(error)
            return False

    def delete_all_jobs(self) -> bool:
        """
        remove all cron jobs
        :return:
        """
        try:
            self.cron.remove_all()
            return True
        except Exception as error:
            print(error)
            return False
