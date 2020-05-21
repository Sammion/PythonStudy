# @author Sam
# @date 2018-01-21
# desc 常见内建模块学习（一）
# 处理时间和日期的标准库
# datetime 是一个模块，第二个是类名

from datetime import datetime, timedelta, timezone

# 获取当前时间
now = datetime.now()
print(now)
print(now.timestamp())

# 指定日期和时间
dt = datetime(2017, 1, 21, 13, 40, 23)
print(dt)
print(dt.timestamp())

# timestamp 转换成时间
t = 1516514411.047477
print(datetime.utcfromtimestamp(t))
print(datetime.fromtimestamp(t))

# str转换成时间
cday = datetime.strptime('2018-01-21 08:00:01', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 转换成字符串
n = datetime.now()
print(n.strftime('%a,%b %d %H:%M'))
print(n.strftime('%H:%M %d-%m-%Y'))

# datetime 加减运算
l = datetime.now()
print('now is %s' % l)
print(l + timedelta(hours=-10))
print(l + timedelta(days=2, hours=3, seconds=10, minutes=10))
print(l - timedelta(weeks=1))

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC changes!!!')
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)