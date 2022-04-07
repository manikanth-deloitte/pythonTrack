from datetime import datetime,timedelta


def addTime(time_str, minu,hr):
    given_time = datetime.strptime(time_str,'%H:%M:%S')
    update_time = given_time + timedelta(hours=hr, minutes=minu)
    updated_time = update_time.time()
    return updated_time


def calTime(shows,time,gap,interval,length):
    gap = int(gap)
    len_s = length.split(":")
    minutes = int(interval) + int(len_s[-1])
    hr = int(len_s[0])
    s = ""

    for i in range(int(shows)):
        re = addTime(time, minutes, hr)
        s += str(time) + "-" + str(re) + ",\n"
        re = str(re)
        time1 = addTime(re, gap, hr=0)
        time = str(time1)

    return s