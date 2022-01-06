def swapFileData():

    file1 = input("enter the original file: ")
    file2 = input("enter the file to be swapped: ")

    with open(file1,'r') as a:
        date_a=a.read()
    with open (file2,'r') as b:
        date_b=b.read() 

 
    with open(file1,'w+') as a:
        a.write(date_b)

    with open (file2,'w+') as b:
        b.write(date_a)

swapFileData()                   


