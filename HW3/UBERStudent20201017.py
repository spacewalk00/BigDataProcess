#!/user/bin/python3

import sys
import datetime

file = open(sys.argv[2], "wt")
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
weekday = [{}, {}, {}, {}, {}, {}, {}]

#with open("uber.txt", "rt") as fp:
with open(sys.argv[1], "rt") as fp:
	lines = fp.readlines()
	for line in lines:
		fields = line.split(",")
		
		region = fields[0]
		date = fields[1].split("/")
		v = fields[2]
		t = fields[3]

		wd_index = datetime.date(int(date[2]), int(date[0]), int(date[1])).weekday()
		if region in weekday[wd_index].keys():
			vehicles = int(weekday[wd_index][region].split(',')[0]) + int(v)
			trips = int(weekday[wd_index][region].split(',')[1]) + int(t)
			weekday[wd_index][region] = str(vehicles) + "," + str(trips)
		else:
			weekday[wd_index][region] = v + "," + t
for i in range(7):
	for r in weekday[i].keys(): 		
		file.write("%s,%s %s\n" %(r, days[i], weekday[i][r]))	
		
		
		
			
file.close()			
