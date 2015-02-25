import os
execfile('capture.py')
f = open('copies.txt','w')
f.write('0')
os.system('clear')
ans = raw_input("PAID[Y/N] : ")
if ans=='y' or ans=='Y':
    try:
        print("WORKING")
        copy = raw_input("Enter number of copies : ")
        if copy:
            f.write(copy)
        f.close()
        os.system('python mail.py')
    except:
        print("Error")
elif ans=='n' or ans=='N':
    try:
        print("WORKING")
        f.close()
        execfile('wmrk.py')
        execfile('mail.py')
    except:
        print("Error")


    

    
    
