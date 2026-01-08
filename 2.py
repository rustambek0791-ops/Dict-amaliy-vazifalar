import os
login = {
    "jeymsbond" : "agent007",
    "tony_stark" : "ironman101",
    "piterparker": "spider12.12",
    "sherlok": "sher.104"
}
username = input("Username >>> ")
password = input("Parol >>> ")
if username in login:
    if login[username] == password:
        print("Hisobga kirdingiz")
    else:
        print("Parol notugri!")
else:
    print ("Foydalanuvchi topilmadi!")