#len(12345)- length function cant accept integer data types bcos it accepts String only as of now
len("12345")
#We havent used print so it will not be printed.
# Anything within in a double quote is considered as String so here it is getting accepted
print(type("12345"))
print(type(12345))
print(type(123.235))
print(type(True))
print(type(False))
print("123"+"456")
print(123+456)
#Conversion of Datatype
print(int(123)+int(456))
print(int("123")+int("456"))
#Debugging the Exercises-
#print("Number of letters in your name: " , len(input("Enter your name")))
print("Number of letters in your name: " +str(len(input("Enter your name"))))
