# Library Imports
import sys
# Local Application Imports
import Data.ActionHist_Stack.Action_Hist as Action_Hist
import Functions.Encryptions as Encryptions
import Functions.Decryption as Decryption
import Functions.Graph as Graph
import Functions.PW_Generator as PW_Generator
import Functions.PW_Strength as PW_Strength
import Data.UserData.User_Auth as User_Auth


def main_menu():
    # PHASE 1: AUTHENTICATION LOOP
    UID = None

    while UID is None:
        print("\n" + "="*30)
        print("Welcome to the Password Management System")
        print("="*30)
        print("1. Register")
        print("2. Login")
        print("3. Exit Program")
       
        auth_choice = input("Enter your choice: ")
       
        if auth_choice == '1':
            result = User_Auth.register()
            if result is not False and result is not None:
                pass
            else:
                continue
               
        elif auth_choice == '2':
            CurrentUID = User_Auth.login()
            if CurrentUID is not False and CurrentUID is not None:
                UID = CurrentUID
                continue
            else:
                continue # Restart auth loop on failure
               
        elif auth_choice == '3':
            print("Exiting program...")
            sys.exit() # Completely closes everything
           
        else:
            print("[!] Invalid choice. Please enter 1, 2, or 3.")


    # PHASE 2: MAIN APPLICATION LOOP

    print(f"\n[*] Authentication successful! Loading tools...")
   
    # Main tools menu
   
    print("\n--- MAIN MENU ---")
    print("1. Password Strength Checker")
    print("2. Password Generator")
    print("3. Encryption/Decryption")
    print("4. Action History")
    print("5. Graphs")
    print("6. Logout")
    print("7. Exit")

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
                print("Minimum encryption selected.")
                encrypt_choice = input("Do you want to encrypt a file? (y/n): ")
                if encrypt_choice.lower() == 'y':
                    text = input("Enter the text to encrypt: ")
                    encrypted_file = input("Enter the name of the output .txt file: ")
                    encryption_key_file = input("Enter the name of the output encryption key file: ")
                    Encryptions.min_encrypt(encrypted_file, encryption_key_file, text, UID)
                               
                decrypt_choice = input("Do you want to decrypt a file? (y/n): ")
                if decrypt_choice.lower() == 'y':
                    encrypted_file = input("Enter the name of the .txt file to decrypt: ")
                    encryption_key_file = input("Enter the name of the encryption key file: ")
                    Decryption.min_decrypt(encrypted_file, encryption_key_file, UID)
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
            print("Logging out...")
            UID = None
            main_menu()

        elif choice == '7':
            print("Exiting the program...")
            sys.exit()
           
        else:
            print("[!] Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main_menu()




