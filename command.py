from colorama import Fore, Style, init
import datetime
import random
import time
init(autoreset=True)
importfeature = False
importable = False
AdvancedCommand = False
Username = "User001"
Login = False
ClientID = "U47hjL4k12#"
RandomID = random.randint(100000000000000, 999999999999999)

print("Welcome to Terminal Code v1.0!")

# Main Loop
while True:
	command = input(">>> Enter command: ").strip()

	if command == "/reboot":
		print("Rebooting...")
		time.sleep(5)
		print("Shutting down...")
		time.sleep(1)
		print("Loading...")
		Login = False
		AdvancedCommand = False
		importfeature = False
		importable = False
		RandomID = random.randint(100000000000000, 999999999999999)
		time.sleep(3)
		print("Running Terminal Code...")
		time.sleep(5)
		print("Terminal Code Successfuly running...")
	elif command == "/shutdown":
		print("Shutting down...")
		time.sleep(5)
		print("Closing app...")
		time.sleep(3)
		print("Program Terminated")
		break
	elif Login == True and command == "/stat":
		print("Loading data...")
		time.sleep(5)
		print("---------------------------------")
		print("| Publisher | Robben            |")
		print("| Copyright | 2026©Robben       |")
		print("| App Name  | Terminal Code     |")
		print("| Version   | v1.0              |")
		print(f"| Client ID | {ClientID}       |")
		print(f"| Random ID | {RandomID}   |")
		print("---------------------------------")
	elif Login == True and command == f"/user ClientID {ClientID}":
		command = input(f">>> /{ClientID}/: ").strip()
		if command == "enableAdvancedCommand":
			print("Processing...")
			time.sleep(5)
			print("Advanced Command enabled")
			importfeature = True
	elif Login == True and command == f"/user RandomID {RandomID}":
		command = input(f">>> /{RandomID}/: ").strip()
		if command == "enableAdvancedCommand+":
			print("Loading...")
			time.sleep(3)
			AdvancedCommand = True
			print("You can now use double slash (//test) to use more complex command")
	elif Login == True and importfeature == True and command == "/import data":
		print("")
		command = input(">>> /data/: ").strip()
		if command == "modify":
			command = input(">>> /data/modify/: ").strip()
			if command == "importable: True":
				importable = True
				print("'importable' set to True")
			elif command == "importable: False":
				importable = False
				print("'importable' set to False")
	elif Login == True and importfeature == True and command == "/data open game == 'SPACE SHOOTER'":
		print("Open at https://robben199.github.io/SPACE-SHOOTER-GAME/")
	elif Login == True and importfeature == True and command == "/data pickup file == (README.txt)":
		print("Opening README.txt...")
		time.sleep(1)
		print("Hello, Welcome to Terminal Code! \n \n Terminal Code now can use /data command to code more complex.")
	elif Login == True and importfeature == True and command == "/data list file":
		print("1. README.txt")
	elif AdvancedCommand == True and command == "//test":
		print("Welcome to double slash!")
	elif command == "/date":
	    now = datetime.datetime.now()
	    print(now.strftime("%a %b %d %H:%M:%S %Y"))
	elif command == f"/user login {ClientID}":
		print("Logging in...")
		time.sleep(3)
		print(f"Welcome, {Username}")
		Login = True
	elif Login == True and command == "/user logout":
		print("Logging out...")
		time.sleep(3)
		Login = False
		AdvancedCommand = False
		importfeature = False
		importable = False
		print("You are now entering guest mode")
	elif Login == True and command == f"/user emergency {ClientID} and {RandomID} call":
		emergency = input(">>> Enter Emergency Number: ").strip()
		if emergency == "911":
			print(f"Calling {emergency}...")
			time.sleep(5)
			emergency = input(">>> 911 What's your emergency?: ").strip()
			if emergency != "":
				print(f"Your emergency is '{emergency}'")
				emergency2 = input(">>> Where are you now?: ").strip()
				if emergency2 != "":
					print(f"So, you are at {emergency2}, Ok, we will arrive very soon.")
					print(Fore.GREEN + "(i) You need to wait 60 seconds.")
					time.sleep(60)
					print(Fore.WHITE + f"Alright, your emergency {emergency} is done.")
				else:
					print("Your location cannot be empty!")
					print("Emergency Cancelled")
			else:
				print("Your emergency cannot be empty!")
				print("Emergency Cancelled")
	elif command == "/help":
		print("Loading...")
		time.sleep(3)
		print("HELP:\nTerminal Code is a program that use for debugging. All command will explained. ")
		print("\n1. '/shutdown' and '/reboot'\nShutdown the program or reboot the program")
		print("\n2. '/user login (ClientID)'\nLogin to your account by entering your ClientID, if you login, you starting to unlock more command.")
		print("\n3. '/user logout'\nLogout to your account, becoming guest and the command become limited.")
		print("\n4. '/user ClientID (ClientID)'\nThis command need your ClientID, then you can type 'enableAdvancedCommand' to start unlocking more feature like '/data'.")
		print("\n5. '/user RandomID (RandomID)'\nThis command need your RandomID, then you can type 'enableAdvancedCommand+' to start unlocking double slash (//test) feature.")
		print("\n6. '/stat'\nThis command only works if you already login. It shows the publisher, copyright, version, your ClientID, and your RandomID.")
		print("\n7. '/date'\nThis command will show current day, hours, minutes, and seconds through your operating system.")
	else:
		print(f"Error: Unknown Command: {command}")