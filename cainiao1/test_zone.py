'''
说明：同样的代码，linux上的时间 比window上的时间少8小时，如何统一都显示为中国时区的时间？
分析：天涯共此时，我在中国的电脑上执行print(datetime.now()),打印的是2021-12-23 18:00:00,
        同时，有一个格林威治的人，也在电脑上运行了同样的语句，他电脑上应打印肯定是他们当地的时间：2021-12-23 10:00:00
        所以，我想要格林威治的人也打印中国时间怎么办？告诉他时区即可
'''

from datetime import datetime, timedelta, timezone

TZ = timezone(timedelta(hours=8))
# 你将在全世界任何一个时区的电脑上，都打印的是中国时间，可以把下面的代码在linux上执行看结果
print(datetime.now(TZ))
