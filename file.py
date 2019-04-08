fd = "myname.txt"

file = open(fd, 'w')
file.write("Hello Aayush Sir")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
