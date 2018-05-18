from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('Code Inverness_logfile.csv', 'r') as f:
    data = list(reader(f))

temp = [i[1] for i in data[1::]]
time = [parser.parse(i[16]) for i in data[1::]]

pyplot.title('Temperature changes over time')
pyplot.xlabel('Time/Hours')
pyplot.ylabel('Temperature/$^\circ$C')

pyplot.plot(time, temp)
pyplot.show()
