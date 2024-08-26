import random
#To run 'python basics.py'

#console.log
print("hello fron snake")

#variables are mutable

myVar = "thurs a snayk in mah boote!"
MY_VAR = "don't ever change me pls"

#array
myArr = [1,2,3]

#.push
myArr.append(4)
print(myArr)

#.length 
print(len(myVar))

# functions cannot be called before declaration
# myFunkyFunction("too early")

#functions & template literal / formatted string
def myFunkyFunction(str):
    print(f"Hello... Why are you saying '{str}'")


myFunkyFunction("boy howdy")


# random number (int)
random_number = random.randint(1, 10)
random_number2 = random.randint(1, 10)
print(random_number)

# if else

if random_number < 5:
    print("too low")
elif random_number > 5:
    print("too high!")
else:
    print("Just right")

print(random_number)
print(random_number2)

# or and not !

if random_number < 5 and random_number2 < 5:
    print("both too low")

if random_number < 5 or random_number2 < 5:
    print("at least one value is too low")

if not random_number > 5:
    print("first number is too low")