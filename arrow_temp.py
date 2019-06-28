import arrow

# 获取当前时间
arrow.now().format(fmt="YYYY-MM-DD HH:MM:SS")
arrow.utcnow()

# 将时间戳转化为arrow对象
arrow.get(1519534533)
arrow.get('1519534533')
arrow.get(1519534533.153443)
arrow.get('1519534533.153443')

# 将字符串转换为arrow对象
arrow.get('2018-02-24 12:30:45', 'YYYY-MM-DD HH:mm:ss')
# 直接创建arrow对象
arrow.get(2018, 1, 2, 3, 4, 5, 6)
arrow.Arrow(2018, 1, 2, 3, 4, 5, 6)

# arrow对象属性
a = arrow.now()
a.datetime          # --> to datetime.datetime(有时区)
a.naive             # --> to datetime.datetime(无时区)
a.timestamp         # --> to int timestrap
a.float_timestamp   # --> to float timestrap
a.tzinfo            # --> to datetime.datetime

a.year      # --> get year
a.month     # --> get month
a.day       # --> get day
a.hour      # --> get hour
a.minute    # --> get minute
a.second    # --> get second
a.microsecond   # --> 微秒

# 时间推移
# years,months,weeks,days,hours，seconds，microseconds
a.shift(days= -1)

# 时间替换
a.replace(hour=9)

import datetime
arrow.get(datetime.datetime.now())