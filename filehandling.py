import os,sys

if os.path.isfile("myfile.txt"):

    f = open("myfile.txt","w")

    print("Enter text, Type (#) when done: \n")

    s = ''

    while s!='#':
    
        s = input()
        f.write(s)
    f.close()

    f1 = open("myfile.txt","r")
    r = f1.read()
    print(r)
    f1.close()

else:
    print("file does not exist")