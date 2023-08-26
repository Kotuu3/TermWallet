import requests
import time
import sys
import getpass

previous_balance = None


print(" ")
print(" /$$$$$$$$                                /$$      /$$           /$$ /$$             /$$    ")
print("|__  $$__/                               | $$  /$ | $$          | $$| $$            | $$    ")
print("   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$ | $$ /$$$| $$  /$$$$$$ | $$| $$  /$$$$$$  /$$$$$$ ")
print("   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$/$$ $$ $$ |____  $$| $$| $$ /$$__  $$|_  $$_/ ")
print("   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$$$_  $$$$  /$$$$$$$| $$| $$| $$$$$$$$  | $$    ")
print("   | $$| $$_____/| $$      | $$ | $$ | $$| $$$/ \  $$$ /$$__  $$| $$| $$| $$_____/  | $$ /$$")
print("   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$/   \  $$|  $$$$$$$| $$| $$|  $$$$$$$  |  $$$$/")
print("   |__/ \_______/|__/      |__/ |__/ |__/|__/     \__/ \_______/|__/|__/ \_______/   \___/  ")
print(" ")
print("============================================================================================")
print(" ")



def fetch_balance(username):
    api_url = f"https://server.duinocoin.com/users/{username}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        balance_info = data['result']['balance']
        return balance_info['balance']

    else:
        print("nie pykło")
        return None


username = input("Username: ")
previous_balance = None

print(" ")

while True:
    new_balance = fetch_balance(username)

    if new_balance is not None:
        if previous_balance is not None and new_balance != previous_balance:
            sys.stdout.write("\rBalance: {:.5f}".format(new_balance))
            sys.stdout.flush()
            previous_balance = new_balance
        elif previous_balance is None:
            sys.stdout.write("\rBalance: {:.5f}".format(new_balance))
            sys.stdout.flush()
            previous_balance = new_balance

    time.sleep(1)  # Opóźnienie na 1 sekundę