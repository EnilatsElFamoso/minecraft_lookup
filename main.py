import requests
import os
from os import system
import json
import random
import datetime

os.system('cls')

system("title " + "MinecraftLookup")

def lookup():
    def get_uuid():
        os.system('cls')
        username = input("Username: ")

        resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        uuid = resp.json()["id"]

        print(f"Current UUID for " + username + f" is {uuid}")
        del uuid
        del resp
        del username

    def get_username():
        os.system('cls')
        uuid = input("Uuid: ")

        resp = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}")
        username = resp.json()["name"]

        print(f"The current username for this uuid is {username}")
        del uuid
        del resp
        del username

    def get_username_history():
        os.system('cls')
        username = input("Username: ")

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

    def get_skin():
        os.system('cls')
        username = input("Username: ")

        resp = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        uuid = resp.json()["id"]

        print(f"Current skin for this username is https://crafatar.com/skins/{uuid}\nCurrent skin for this username in 3d  is https://crafatar.com/renders/body/{uuid}")
        del uuid
        del resp
        del username

    def hypixel_info():
        def getInfo(call):
            r = requests.get(call)
            return r.json()



        name = input("Username: ")
        API_KEY = "2ed95fd8-2895-43cf-bb51-37259f002a42"


        name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"
        data = (getInfo(name_link))
        verif = data["success"]
        print("")
        if verif == True:
            found = data["player"]
            if found in [None, "null", 'null']:
                print("Player not found")
            else:    
                print(name_link + "\n\n")
                print("Profile Found!\n")
                username = data["player"]["playername"]
                language = "out"
                rank = "out"
                karma = "out"
                _id = data["player"]["_id"]
                uuid = data["player"]["uuid"]
                last_login = data["player"]["lastLogin"]
                first_login = data["player"]["firstLogin"]

                print("Id: " + _id)
                print("Uuid: " + uuid)
                print("Username: " + username)
                print("Rank: " +  rank)
                print("Language: " + language)
                print("Karma: " + str(karma))
                print("\n")
                print("First login : "), print(datetime.datetime.fromtimestamp(first_login // 1000.0))
                print(datetime.datetime.fromtimestamp(last_login // 1000.0))
        else:   
            print(name_link)
            get_id = random.randint(0, 3000)
            id = get_id
            print("Profile not found, error has been sent to R.D.A.C (ID:" + str(id) + " )")
            print("If you want to know more about this error contact R.D.A.C and give the error ID")
            alert = {
                "avatar_url":"https://i.imgur.com/m5tTDkm.png",
                "name":"R.D.A.C",
                "embeds": [
                    {
                        "author": {
                            "name": f" Erreur ID: {id}",
                            "icon_url": "https://i.imgur.com/m5tTDkm.png",
                            "url": "https://i.imgur.com/m5tTDkm.png"
                            },
                        "description": f"{data} ",
                        "color": 8421504,
                        "footer": {
                        "text": f"upload from Minecraft Lookup"
                        }
                    }
                ]
            }
            webhook ="https://discord.com/api/webhooks/1000138685632753759/Px7jNE2agyn5UJbdoILyM7Q19F5yeR1xAiImy1UOC1hAPgi6KOyU7pU5svqjh03MgWpg"
            requests.post(webhook, json=alert)





    print("""
    [1] Get uuid
    [2] Get username with uuid
    [3] Get name History
    [4] Get skin
    [5] Get hypixel info
    """)
    choice =input("\n [>] ")

    if choice not in ['1', '2', '3', '4', '5']:
        os.system('cls')
        lookup()
    
    elif choice == '1':
        get_uuid()
        lookup()

    elif choice == '2':
        get_username()
        lookup()

    elif choice == '3':
        get_username_history()
        lookup()

    elif choice == '4':
        get_skin()
        lookup()

    elif choice == '5':
        os.system('cls')
        hypixel_info()
        lookup()


lookup()