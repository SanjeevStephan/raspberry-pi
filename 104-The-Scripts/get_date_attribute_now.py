# Python3 code to demonstrate
# attributes of now()
	
# importing datetime module for now()
import datetime
	
# using now() to get current time
current_time = datetime.datetime.now()
	
# Printing attributes of now().
print ("The attributes of now() are : ")
	
print ("Year : " + current_time.year)
	
print("Month : " + current_time.month)
	
#print ("Day : ", end = "")
print ("Day " + current_time.day)
