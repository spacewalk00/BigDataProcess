#!/user/bin/python3

import sys
import datetime

#with open("uber.txt", "rt") as fp:
with open(sys.argv[1], "rt") as fp:
	lines = fp.readlines()
	for line in lines:
		fields = line.split(",")

		date_slash = fields[1]
		date = date_slash.split("/")	

		days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
		dayObject = datetime.date(int(date[2]), int(date[0]), int(date[1]))
		wd = days[dayObject.weekday()] 
			
		#with open("uberoutput.txt", "at") as fw:
		with open(sys.argv[2], "at") as fw:
			fw.write(line.replace(date_slash + ",", wd + " "))	
			

