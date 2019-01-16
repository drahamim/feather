import time

BLAH = .25
X = 250
Y = 0
Z = 0

Scale = 10

while True:
	
	values= '''
	Red = {a} 
	Green = {b} 
	Blue = {c}
	'''.format(a=`X`, b=`Y`, c=`Z`) 


	print(values)
	print("DELAYED")
	time.sleep(BLAH)
	if (X >= 0 and  0 <= Y < 250 and Z == 0):
		print('Logic')		
		X -=  Scale
		Y +=  Scale
	elif (X == 0 and 0 <= Y <= 250 and 250 > Z >= 0):
		print('Second')
		Y -= Scale
		Z += Scale
	elif (X >= 0 and Y == 0 and 10 < Z <= 250) :
		print('Third')
		X += Scale
		Z -= Scale
	elif (X == 240 and Y == 0 and Z == 10):
		print('End GO BACK!')
		X = 250
		Y = 0
		Z = 0		