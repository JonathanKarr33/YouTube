document = open("example.txt","r")
for line in document:
    print(line)
document.close()

with open("example.txt","r") as document:
    for line in document:
        print(line)