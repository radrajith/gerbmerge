#enter file name
file = open('merge2.TXT', 'r+')
output = open('merge2_corrected.TXT','a')
list = []
i=0
for line in file:
    if 'T' in line:
        list.append(line)
        print line
        newLine = line[:3]
        output.write(newLine + '\n')
    else:
        output.write(line)
output.seek(0)
output.write('%\n')
output.write('M74')
for i in list:
    output.write(i)
output.write('%')
file.close()
output.close()
