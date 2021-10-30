fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
count = 0
spam_confidence_accumulator = 0.0
lst = list()
for line in fh:
    line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        words = line.split()
        spam_confidence = float(words[1])
        print(spam_confidence)
        spam_confidence_accumulator += spam_confidence
        count += 1

print("Spam Confidence Accumulator: " + str(spam_confidence_accumulator))
print("Average: " + str(spam_confidence_accumulator/count))
print("There were", count, "lines in the file with X-DSPAM-Confidence as the first word")
