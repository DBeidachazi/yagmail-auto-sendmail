
前段时间因为疫情被封在了学校
宿舍需要去走廊里拿饭
就想着公平一点，宿舍的每一个人都轮流去拿饭
排个轮值表贴门上感觉不太方便
大家天天都会关注手机，那就在饭点前把今天需要去取饭的人通知了
在网上查了半天只有 Sever酱推送的 用起来比较麻烦
就写了点东西，采用邮件推送，放在服务器上：
库yagmail
推荐网易邮箱




import yagmail
import datetime
#
user = "xxx@163.com" #邮箱账户
password = "XXXXXXXXXXXXXXX" #SMTP密钥
host = 'smtp.163.com' #SMTP服务器地址
start = datetime.date(2022, 4, 22) #从何时开始轮值
list = ["a", "b", "c", "d", "e"] #人员名单

# 日期差函数
today_time = datetime.date.today()
def count_differ_days(start, today_time):

    # UTC时间，所以需要UTC时间+8
    # start = start + datetime.timedelta(hours=8)
    today_time = today_time + datetime.timedelta(hours=8)
    d1 = datetime.date(start.year, start.month, start.day)
    d2 = datetime.date(today_time.year, today_time.month, today_time.day)
    return (d2 - d1).days

# 日期差
difference = count_differ_days(start, today_time)

# list 长度
list_len = len(list)

# 今日轮值的人
duty = list[difference % list_len]

#通过邮箱服务器登录自己的邮箱
email = yagmail.SMTP(user, password, host)

#开始发送邮件
email.send(to=['xxxx@qq.com', 'xxxxxxx@gmail.com'],
           subject='今天的轮值的人是 ' + duty + " !",
           contents='From Yagmail Bot')
