import sys
import numpy as np
import os
import re
import operator

trainingF = sys.argv[1]
testF = sys.argv[2]

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def trainingToMatrix(filename):
	data = []
	f = open(filename)
	for line in f:
		data.extend(line.strip())
	str = filename
	label = re.sub(r'[^0-9]', '', str)
	return data, label[0]

def alltrainingFileToMatrix():
	group = []
	labels = []	
	fileList = os.listdir(trainingF+'/')
	for dataFile in fileList:	
		data, label = trainingToMatrix(trainingF+'/'+dataFile)
		group.append(data)
		labels.append(label)
	groupM = np.array(group, dtype=int)
	return groupM, labels

def testFileToMatrix():
	testList = os.listdir(testF+'/')
	testGroup = []
	testLabels = []
	for testFile in testList:
		data = []
		f = open(testF+'/'+testFile)
		for line in f:
			data.extend(line.strip())

		str = testFile 
		label = re.sub(r'[^0-9]', '', str)
		
		testGroup.append(data)
		testLabels.append(label[0])
	return testGroup, testLabels	

def errorCount(testMat, digitMat, digitLabels, k):
	index = 0
	errCount = 0
	for test in testMat:
		testM = np.array(test, int)
		#print(str(index)+'번 test')
		maybe = classify0(testM, digitMat, digitLabels, k)
		if maybe != testLabels[index]:
			errCount = errCount + 1
		index = index + 1
	return errCount, index
	
digitMat, digitLabels = alltrainingFileToMatrix()
testMat, testLabels = testFileToMatrix()

for k in range(1, 21):	
	errCount, total = errorCount(testMat, digitMat, digitLabels, k)
	print(str(int(errCount/float(total)*100.0)))

