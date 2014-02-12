reader=open('test.txt','r')

for line in reader:
    temp=line.strip()
    print len(temp)
reader.close()