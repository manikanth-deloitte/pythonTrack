
from datetime import datetime,timedelta
# # Given timestamp in string
# time_str = '9:00'
# # create datetime object from timestamp string
# given_time = datetime.strptime(time_str, '%H:%M')
# print('Given timestamp: ', given_time)
# n = 15
# # Add 15 minutes to datetime object
# final_time = given_time + timedelta(minutes=n)
# print('Final Time (15 minutes after given time ): ', final_time.time())


def addTime(time_str, minu,hr):
    given_time = datetime.strptime(time_str,'%H:%M:%S')
    update_time = given_time + timedelta(hours=hr,minutes=minu)
    updated_time = update_time.time()
    return updated_time

shows='3'
time = '9:20:00'
gap = int('30')
interval = '15'
length = '1:20'
len_s = length.split(":")
minutes = int(interval)+int(len_s[-1])
hr = int(len_s[0])
print(addTime(time,minutes,hr))
s=""

for i in range(int(shows)):
    re = addTime(time,minutes,hr)
    s += str(time)+"-"+str(re)+"\n"
    re = str(re)
    time1 = addTime(re,gap,hr=0)
    time = str(time1)

print(s)