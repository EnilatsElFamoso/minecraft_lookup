import requests
import os

os.system('cls')

def lookup():
    def get_uuid():
        username = input("Pseudo: ")

        resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        uuid = resp.json()["id"]

        print(f"Current UUID for " + username + f" is {uuid}")
        del uuid
        del resp
        del username

    def get_username():
        uuid = input("Uuid: ")

        resp = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}")
        username = resp.json()["name"]

        print(f"Le pseudo associé a cette UUID est {username}")
        del uuid
        del resp
        del username

    def get_username_history():
        username = input("Pseudo: ")

        resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        uuid = resp.json()["id"]

        name_history = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names").json()
        history = ""
        name_data = list()
        for data in name_history:
            name_data.append(data["name"])

        for i in range(len(name_data)):
            history += name_data[i] + " > "

        print(history)

        del uuid
        del resp
        del username
        del history
        del name_data

    print("""
    [1] Get uuid
    [2] Get username with uuid
    [3] Name History
    """)
    choice =input("\n [>] ")

    if choice not in ['1', '2', '3']:
        os.system('cls')
        lookup()
    
    elif choice == '1':
        os.system('cls')
        get_uuid()
        lookup()

    elif choice == '2':
        os.system('cls')
        get_username()
        lookup()

    elif choice == '3':
        os.system('cls')
        get_username_history()
        lookup()

lookup()