from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f'{i+1} : {items}')

def createfile():
    try:
        name = input("please tell your file name:")
        p = Path(name)
        if not p.exists():

            with open(p,'w') as fs:
                 data = input("what you want to write in the file:")
                 fs.write(data)
            print(f"file created succesfully")
        else:
             print("this file already exist")
              

    except Exception as err:
        print(f"file created successfully")  

def readfile():
    try:
        readfileandfolder()
        name = input("what file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
             
             with open(p,'r') as fs:
                 data = fs.read()
                 print(data)

             print("file read succesfully")    
        else:
            print("file dosen't exists")  
    except Exception as err:
        print(f"an error occured {err}")  

def updatefile():
    try:    
        readfileandfolder()
        name = input("what file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of file")
            print("press 2 for overwriting the file")
            print("press 3 for appending some content in your file")

            res = int(input("tell your number"))

            if res ==1:
                name2 = input("tell your new file")
                p2= Path(name)
                p.rename(p2)

            if res==2:
                with open(p,"w") as fs:
                    data = input("tell what you write")
                    fs.write(data)

            if res==3:
                with open(p,'a') as fs:
                    data = input("tell what you append in file")
                    fs.write(""+data)

    except Exception as err:
        print(f"an error occur {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("which file you delete")
        p = Path(name)

        if p.exists() and p.is_file():
           os.remove(name)

           print("file remove succesfully")

        else:
            print("no file remove succesfully")

    except Exception as err:
        print(f"an error occure {err}")
          

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

click = int(input("please tell your number"))

if click == 1:
    createfile()

if click == 2:
    readfile()
    

if click == 3:
    updatefile()

if click == 4:
    deletefile()

    