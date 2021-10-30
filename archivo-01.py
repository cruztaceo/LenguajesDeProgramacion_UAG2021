fname = input("Enter file name: ")

if len(fname) < 1 : fname = "texto.txt"
try:
    fh = open(fname)
except:
    print('File not found')
    quit()

count = 0
for line in fh:
    words = line.split(":")
    print(words[0] + " -- " + words[2])
    count += 1

print("There were", count, "lines in the file")
