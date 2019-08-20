# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create function
def sayHello(name = 'cabrown'):
    """
    Prints Hello and then name.
    """

    print('Hello ' + name)

# sayHello()
# return value
def getSum(num1,num2):
    total = num1 + num2
    return total

# print(getSum(4,5))
numSum = getSum(2,3)

def addOneToNum(num):
    num = num + 1
    # num += 1
    return num

num = 5

newNum = addOneToNum(num)
print(newNum)


# A lambda function is a small anonymous function
# A lambda function cat take any number of arguments, but can only have one expression. Very similart to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

print(getSum(9,2))

addOneToNum = lambda num : num + 1

print(addOneToNum(5))