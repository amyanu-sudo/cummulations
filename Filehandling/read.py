#open() returns a file object 
f = open("demofile.txt", "r")
#reads the entire file
print(f.read())
#reads the first 5 characters of the file
print(f.read(5))
#reads one line of the file
print(f.readline())
#loops through line by line
for x in f:
  print(x)
#closes the file
f.close()
