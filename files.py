# Python has functions for creating, reading, updating, and deleting files

# Open a file
myFile = open('myfile.txt','w')

# Get some info
print('name: ', myFile.name)
print('Is Cosed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# write to file
myFile.write('I love python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt','a')
myFile.write(' I also like PHP')
myFile.close()

# read from a file
myFile = open('myfile.txt','r+')
text = myFile.read(10)
print(text)