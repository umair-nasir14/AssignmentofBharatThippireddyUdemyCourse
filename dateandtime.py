import datetime,time

epochseconds = time.time()
print(epochseconds)

tnow = time.ctime(epochseconds)
print(tnow)

dtnow = datetime.datetime.today()
print('Current date: {}/{}/{}'.format(dtnow.day,dtnow.month,dtnow.year))
print('Current time: {}:{}:{}'.format(dtnow.hour,dtnow.minute,dtnow.second))

