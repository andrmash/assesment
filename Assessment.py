

## define infants as less than 6 months
infantAge = 6
## keep all ages in months
## not sure if a dict is always ordered - but ideally we should look 
## at rows order by minAge to ensure we get the first class with availabilty if there is an overlap in ages


def classAvailability(age):
	for row in dict:
	    if age <= infantAge and age > row['minAge'] and age <= row['maxAge'] and row['infantsEnrolled'] < row['infantsCapacity'] :
	        # print (row['Name'],row['minAge'],row['maxAge']) 
	        return True

	    if age > infantAge and age > row['minAge'] and age <= row['maxAge'] and row['currentlyEnrolled'] < row['capacity'] :
	        # print (row['Name'],row['minAge'],row['maxAge'])  
	        return True
	return False


# enrollment data - would be pulled from a database etc

#test 1 - 7 month old allocated to class 2 which empty - should return TRUE
dict = [
{'Name': 'Class1', 'minAge': 0, 'maxAge': 6, 'capacity' : 5, "infantsCapacity" : 5,"infantsEnrolled" : 5, "currentlyEnrolled" : 5},  ## check infant age group
{'Name': 'Class2', 'minAge': 0, 'maxAge': 24, 'capacity' : 10, "infantsCapacity" : 2,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class3', 'minAge': 24, 'maxAge': 36, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class4', 'minAge': 48, 'maxAge': 60, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
]

print classAvailability(7)

#test 2 - infant class is full should overflow to empty 'class2' ie return true
dict = [
{'Name': 'Class1', 'minAge': 0, 'maxAge': 6, 'capacity' : 5, "infantsCapacity" : 5,"infantsEnrolled" : 5, "currentlyEnrolled" : 5},  ## check infant age group
{'Name': 'Class2', 'minAge': 0, 'maxAge': 24, 'capacity' : 10, "infantsCapacity" : 2,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class3', 'minAge': 24, 'maxAge': 36, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class4', 'minAge': 48, 'maxAge': 60, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
]

print classAvailability(5)

#test 3 - out or range age should retturn false
dict = [
{'Name': 'Class1', 'minAge': 0, 'maxAge': 6, 'capacity' : 5, "infantsCapacity" : 5,"infantsEnrolled" : 5, "currentlyEnrolled" : 5},  ## check infant age group
{'Name': 'Class2', 'minAge': 0, 'maxAge': 24, 'capacity' : 10, "infantsCapacity" : 2,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class3', 'minAge': 24, 'maxAge': 36, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class4', 'minAge': 48, 'maxAge': 60, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
]

print classAvailability(62)
print classAvailability(-5)


#test 4 - all infant classes full - should return False
dict = [
{'Name': 'Class1', 'minAge': 0, 'maxAge': 6, 'capacity' : 5, "infantsCapacity" : 5,"infantsEnrolled" : 5, "currentlyEnrolled" : 5},  ## check infant age group
{'Name': 'Class2', 'minAge': 0, 'maxAge': 24, 'capacity' : 10, "infantsCapacity" : 2,"infantsEnrolled" : 2, "currentlyEnrolled" : 0},
{'Name': 'Class3', 'minAge': 24, 'maxAge': 36, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
{'Name': 'Class4', 'minAge': 48, 'maxAge': 60, 'capacity' : 15, "infantsCapacity" : 0,"infantsEnrolled" : 0, "currentlyEnrolled" : 0},
]

print classAvailability(5)




