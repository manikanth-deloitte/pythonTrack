file = open("string.txt","w")
file.write("This assignment is based on file handling")
file.close()

with open("string.txt",'r') as rfile:
    words = rfile.read().split(" ")
    max_len = len(max(words, key=len))
    for s in words:
        if len(s) == max_len:
            print(s)