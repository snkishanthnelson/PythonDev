f1 = open('Text.txt','r')
f2 = open('Text2.txt','a')

for i in f1:
    f2.write(i)