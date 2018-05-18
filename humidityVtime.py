from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('Code Inverness_logfile.csv', 'r') as f:
    data = list(reader(f))

temp = [i[2] for i in data[1::]]
time = [parser.parse(i[16]) for i in data[1::]]

pyplot.title('Humidity changes over time')
pyplot.xlabel('Time/Hours')
pyplot.ylabel('The percentage of relative humidity')

pyplot.plot(time, temp)
pyplot.show()
