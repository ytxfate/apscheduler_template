import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


def main_func():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# ========================= cron定时调度（某一定时时刻执行）=================================== #
"""
https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html#module-apscheduler.triggers.cron

    (int|str) 表示参数既可以是int类型，也可以是str类型
    (datetime | str) 表示参数既可以是datetime类型，也可以是str类型
    year (int|str) – 4-digit year -（表示四位数的年份，如2008年）
    month (int|str) – month (1-12) -（表示取值范围为1-12月）
    day (int|str) – day of the (1-31) -（表示取值范围为1-31日）
    week (int|str) – ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩展形式）或2006W527（紧凑形式））
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun) - （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）
    hour (int|str) – hour (0-23) - （表示取值范围为0-23时）
    minute (int|str) – minute (0-59) - （表示取值范围为0-59分）
    second (int|str) – second (0-59) - （表示取值范围为0-59秒）
    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive) - （表示开始时间）
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive) - （表示结束时间）
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone) -（表示时区取值）
"""
#表示2017年3月22日17时19分07秒执行该程序
scheduler.add_job(main_func, 'cron', year=2017, month=3, day=22, hour=17, minute=19, second=7)

# 特殊 cron 执行示例
# scheduler.add_job(main_func, "cron", day="2-7", hour=7) # 每月 2 至 7 日 7 点执行
# scheduler.add_job(main_func, "cron", hour="8-22", minute="0,10,20,30,40,50") # 每天 8-22 点每 10 分钟执行一次

# ============================ interval 间隔调度（每隔多久执行）================================ #
"""
    weeks (int) – number of weeks to wait
    days (int) – number of days to wait
    hours (int) – number of hours to wait
    minutes (int) – number of minutes to wait
    seconds (int) – number of seconds to wait
    start_date (datetime|str) – starting point for the interval calculation
    end_date (datetime|str) – latest possible date/time to trigger on
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
"""
#表示每隔3天17时19分07秒执行一次任务
scheduler.add_job(main_func, 'interval', days=3, hours=17, minutes=19, seconds=7)

# ============================== date 定时调度（作业只会执行一次）============================== #
"""
    run_date (datetime|str) – the date/time to run the job at  -（任务开始的时间）
    timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already
"""
# The job will be executed on November 6th, 2009 at 16:30:05
scheduler.add_job(main_func, 'date', run_date=datetime.datetime(2009, 11, 6, 16, 30, 5), args=['text'])

scheduler.start()
