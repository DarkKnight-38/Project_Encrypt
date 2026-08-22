# Local Application Imports
import Action_Hist
import Encryptions
import Decryption
import Graph
import PW_Generator
import PW_Strength
import User_Auth

print("1. Register")
print("2. Login")

choice = input("Enter your choice: ")
if choice == '1':
    User_Auth.register()
elif choice == '2':
    User_Auth.login()


