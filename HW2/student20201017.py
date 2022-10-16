import openpyxl

wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']

row_id = 1
student_num = 0
total = [] 
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
		total.append(sum_v)
		student_num += 1	
	row_id += 1

# grade
total_sorted = [] 
total_sorted = sorted(total)
total_sorted.reverse()

rank = []
for i in total:
	rank.append(total_sorted.index(i)+1)
#print(rank)

allC = 0
if len(set(rank)) == 1:
	#모두 동점인 경우
	allC = 1

grade_list = []
abc = [ [], [], [] ]


for r in rank:
	a_condition = student_num * 0.3
	b_condition = student_num * 0.7
	
	if a_condition >= r and len(abc[0]) < a_condition and allC == 0:
		grade = "A"
		abc[0].append(r)
	elif student_num * 0.7 >= r and len(abc[1]) < b_condition and allC == 0:
		grade = "B"
		abc[1].append(r)
	else:
		grade = "C"
		abc[2].append(r)

	grade_list.append(grade)	
		
#print(abc)
#print(grade_list)

if allC == 0:
	for a in range(len(abc)):
		sorted_abc = sorted(abc[a])
		for b in range(len(abc[a])):
			if b < len(abc[a])/2:
				grade_list[rank.index(sorted_abc[b])] += '+'
			else:
				grade_list[rank.index(sorted_abc[b])] += '0'
else:
	for i in range(len(grade_list)):
		grade_list[i] += '0'			
#print(grade_list)
row_id = 1 
for row in ws:
	if row_id != 1:	
		ws.cell(row = row_id, column = 8).value = grade_list.pop(0) 
	row_id += 1

wb.save("student.xlsx")
