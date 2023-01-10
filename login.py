import time,os
print("Login in this code!")
time.sleep(1)
username = input("Username : ").lower()
if username =="almighty123":
        print("Welcomeback!",username)
else:
    print("you don't haveacces to use this program")
    os.system("clear")
    time.sleep(1)
    exit()
password = input("Password : ").lower()
if password =="almighty1234!":
    print("Correct! you are now logined in", username,"account")
else:
    print("you don't haveacces to use this program")
    time.sleep(1)
    print("Clossing this program!")
    exit()
