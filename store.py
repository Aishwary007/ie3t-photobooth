import os

f = open("copies.txt",'r')
f2 = open("emails.txt",'r')
f3 = open("data.txt",'a')

a = f.readline()
b = f2.readline()
f3.write(a + "    " + b + "\n")
f3.close()
f2.close()
f.close()
os.system("mv capt0000.jpg " + b)

