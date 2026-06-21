import json
import random
import string
from pathlib import Path

class Bank:
    database = "data.json"
    data = []

    try:
    
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")
        
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=5)
        num = random.choices(string.digits,k=1)
        spchar = random.choices("!@#$^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    


    def Createaccount(self):
        info = {
            "name": input("Tell your name:"),
            "age" :  int(input("Tell Your age:")),
            "email" : input("Tell your Email:"),
            "pin" : int(input("Tell your Pin:")),
            "account" : Bank.__accountgenerate(),
            "balance": 0
        }
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print("Sorry you cannot create your account")
        else:
            print("account has been created successfully!!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.update()

    def Deposite(self):
        accountnumber = input("Tell your account number")
        pin = int(input("Tell your pin"))

        print(Bank.data)

        userdata = [i for i in Bank.data if i['account'] == accountnumber and i['pin'] == pin]

        if userdata == False:
            print("no such account exists")
            return
        else:
          amount = int(input("How much money you want to deposite"))
        if amount > 10000 or amount <= 0:
            print("sorry amount is too much you can deposite below 10000 and above 0")
        else:
            print(userdata)
            userdata[0]['balance'] += amount
            Bank.update()
            print("amount deposited succesfully")

    def Withdraw(self):
            accountnumber = input("Tell your account number")
            pin = int(input("Tell your pin"))
    
            print(Bank.data)
    
            userdata = [i for i in Bank.data if i['account'] == accountnumber and i['pin'] == pin]
    
            if userdata == False:
                print("no such account exists")
                return
            else:
              amount = int(input("How much money you want to Withdraw"))
            if userdata[0]['balance'] < amount:
                print("sorry amount is too much you can Withdraw below 10000 and above 0")
            else:
                userdata[0]['balance'] -= amount
                Bank.update()
                print("amount Withdrew succesfully")

    def Details(self):
         accountnumber = input("Tell your account number")
         pin = int(input("Tell your pin"))

         userdata = [i for i in Bank.data if i['account'] == accountnumber and i['pin'] == pin]
         print("Your information are \n\n\n")
         for i in userdata[0]:
             print(f"{i} : {userdata[0][i]}")

    def UpdateDetails(self):
         accountnumber = input("Tell your account number")
         pin = int(input("Tell your pin"))
         
         userdata = [i for i in Bank.data if i['account'] == accountnumber and i['pin'] == pin]

         if userdata == False:
             print("No such user found")
         else:
             print("You cnanot change age,deposite amount")

             print("Fill the details for chnage or leave it empty if no changes")

             newdata ={
                 "name" : input("please enter new name or enter"),
                 "email" :input("please enter new email or press enter"),
                 "pin" : int(input("Please enter new pin or press enter"))
             }

             if newdata["name"] == "":
                 newdata["name"] = userdata[0]['name']
             if newdata["email"] == "":
                 newdata["email"] = userdata[0]['email']
            
             if newdata["pin"] == "":
                 newdata["pin"] = userdata[0]['pin']

             newdata['age'] = userdata[0]['age']
             newdata['account'] = userdata[0]['account']
             newdata['balance'] = userdata[0]['balance']

             if type(newdata['pin']) == str:
                 newdata['pin'] = int(newdata['pin'])

             for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

             Bank.update()
             print("Details updated successfully!!")

    def delete(self):
        accountnumber = input("Tell your account number")
        pin = int(input("Tell your pin"))
                 
        userdata = [i for i in Bank.data if i['account'] == accountnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user data exists")
        else:
            check = input("Press Y if you actually delete the account or press N")
            if check == 'N' or check == 'n':
              print("bypass")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account delete successfully!!")

                Bank.update()
                

user = Bank()
print("for create an account preee 1")
print("for Deposite Money pree 2")
print("for Withdrawl the Money press 3")
print("For Details Press 4")
print("For Update press 5")
print("For Delete the account 6")

check = int(input("Tell your response:"))

if check == 1 :
    user.Createaccount()

if check == 2:
    user.Deposite()

if check == 3:
    user.Withdraw()

if check == 4:
    user.Details()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.delete()
