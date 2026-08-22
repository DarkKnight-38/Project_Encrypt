# Local Application Imports
import Action_Hist
import Encryptions
import Decryption
import Graph
import PW_Generator
import PW_Strength
import User_Auth
import sys

def main_menu():
    # -----------------------------------------
    # PHASE 1: AUTHENTICATION LOOP
    # -----------------------------------------
    UID = None
    
    # Stay in this loop until we get a valid UID
    while UID is None:
        print("\n--- WELCOME ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit Program")
        
        auth_choice = input("Enter your choice: ")
        
        if auth_choice == '1':
            result = User_Auth.register()
            if result is not False and result is not None:
                UID = result  # <--- CHANGED THIS BACK FROM 'pass'
            else:
                continue
                
        elif auth_choice == '2':
            result = User_Auth.login()
            if result is not False and result is not None:
                UID = result
                continue
            else:
                continue # Restart auth loop on failure
                
        elif auth_choice == '3':
            print("Exiting program. Goodbye!")
            sys.exit() # Completely closes the python script
            
        else:
            print("[!] Invalid choice. Please enter 1, 2, or 3.")

    # -----------------------------------------
    # PHASE 2: MAIN APPLICATION LOOP
    # -----------------------------------------
    print(f"\n[*] Authentication successful! Loading tools...")
    
    # Now that we have the UID, run the main tools until they want to exit
    
    print("\n--- MAIN MENU ---")
    print("1. Password Strength Checker")
    print("2. Password Generator")
    print("3. Encryption/Decryption")
    print("4. Action History")
    print("5. Graphs")
    print("6. Exit")

    while True:
        
        choice = input("Enter your choice: ")

        if choice == '1':
            if UID is None:
                print("[!] You must be logged in to use this.")
                continue
            print("Loading Password Strength Checker...")
            PW_Strength.strength_test()

        elif choice == '2':
            print("Loading Password Generator...")
            PW_Generator.password_generator()

        elif choice == '3':
            enc_type = input("Choose encryption type (min/inter/max): ").strip().lower()
            if enc_type == 'min':
                pass
            elif enc_type == 'inter':
                pass
            elif enc_type == 'max':
                print("Maximum encryption selected.")
                encrypt_choice = input("Do you want to encrypt a file? (y/n): ")
                if encrypt_choice.lower() == 'y':
                    text = input("Enter the text to encrypt: ")
                    txt_file = input("Enter the name of the output .txt file: ")
                    enc_key_file = input("Enter the name of the output encryption key file: ")
                    Encryptions.max_encrypt(text, txt_file, enc_key_file, UID)
                                
                decrypt_choice = input("Do you want to decrypt a file? (y/n): ")
                if decrypt_choice.lower() == 'y':
                    txt_file = input("Enter the name of the .txt file to decrypt: ")
                    enc_key_file = input("Enter the name of the encryption key file: ")
                    Decryption.max_decrypt(txt_file, enc_key_file, UID)
                
        elif choice == '4':
            print("Loading Action History...")
            # Action_Hist.your_function_name_here()

        elif choice == '5':
            print("Loading Graphs...")
            # Graph.your_function_name_here()

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            sys.exit()  # <--- CHANGED FROM 'break' TO COMPLETELY KILL THE SCRIPT
            
        else:
            print("[!] Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main_menu()