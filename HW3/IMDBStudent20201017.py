#/user/bin/python3

import sys

genre_dict = dict()

#movies.dat 읽어서 장르 count하기
with open(sys.argv[1], "rt") as fp:
#with open("movies.txt", "rt") as fp:
	data = fp.read()
	lines = data.split("\n")

	for line in lines:
		fields = line.split("::")

		genre_with_bar = fields[2]
		genre_per = genre_with_bar.split("|")

		for genre in genre_per:
			if genre not in genre_dict:
				genre_dict[genre] = 1
			else:
				genre_dict[genre] += 1
#print(genre_dict)	
genre_tuple = genre_dict.items()

#movieoutput.txt에 지정된 형식으로  쓰기
with open(sys.argv[2], "w") as fp:
#with open("movieoutput.txt", "w") as fp:
	for element in genre_tuple:
		line = element[0]+" "+str(element[1])+"\n"
		fp.write(line)
