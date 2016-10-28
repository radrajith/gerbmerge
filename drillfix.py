#enter file name
import os

dir = os.getcwd()
print(dir)
file = open(dir+'\merge2.TXT', 'r+') #open merge2.txt file as a read write option
output = open('merge2_corrected.TXT','a')
list = []
i=0
for line in file:
    if 'T' in line:
        list.append(line)
        #print line
        #newLine = line[:3]
        #output.write(newLine + '\n')
    #else:
        #output.write(line)
output.seek(0)
output.write('%\nM48\nM74\n')
for i in list:
    output.write(i)
output.write('%\n')
file.seek(0)
for line in file:
    if '%' in line:
        for line in file:
            if 'T' in line:
                #list.append(line)
                #print line
                newLine = line[:3]
                output.write(newLine + '\n')
            else:
                output.write(line)
file.close()
output.close()
print('correct file created in '+dir)
