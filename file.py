fd = "name.txt"

file = open(fd, 'a')
file.write("Hello Aayush Sir")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
