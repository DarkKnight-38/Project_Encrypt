import os
import secrets
import pickle
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

USER_DB_FILE = "users.dat"
global_action_stack = []

def push_to_stack(action):
    global_action_stack.append(action)

def core_encrypt(raw_bytes):
    encrypted_bytes = bytearray()
    key_list = []
    
    for byte in raw_bytes:
        secure_shift = secrets.randbelow(256)
        key_list.append(secure_shift)
        scrambled_byte = byte ^ secure_shift
        encrypted_bytes.append(scrambled_byte)
        
    return encrypted_bytes, key_list

def core_decrypt(encrypted_bytes, key_list):
    if len(encrypted_bytes) != len(key_list):
        return None
        
    decrypted_bytes = bytearray()
    
    for idx in range(len(encrypted_bytes)):
        secure_shift = key_list[idx]
        original_byte = encrypted_bytes[idx] ^ secure_shift
        decrypted_bytes.append(original_byte)
        
    return decrypted_bytes

class CodebreakerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Codebreaker Security Terminal")
        self.geometry("900x600")
        self.resizable(False, False)
        
        if not os.path.exists(USER_DB_FILE):
            with open(USER_DB_FILE, 'wb') as f:
                pickle.dump({}, f)
                
        self.current_user = ""
        self.frames = {}
        self.setup_login_frame()

    def setup_login_frame(self):
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(pady=80, padx=250, fill="both", expand=True)

        label = ctk.CTkLabel(self.login_frame, text="SYSTEM LOGIN", font=("Roboto", 28, "bold"))
        label.pack(pady=30, padx=10)

        self.user_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username", width=250)
        self.user_entry.pack(pady=10, padx=10)

        self.pass_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=250)
        self.pass_entry.pack(pady=10, padx=10)

        login_btn = ctk.CTkButton(self.login_frame, text="Login", width=250, command=self.login_user)
        login_btn.pack(pady=15, padx=10)

        reg_btn = ctk.CTkButton(self.login_frame, text="Register", width=250, command=self.register_user, fg_color="transparent", border_width=1)
        reg_btn.pack(pady=5, padx=10)

    def login_user(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        
        try:
            with open(USER_DB_FILE, 'rb') as f:
                db = pickle.load(f)
        except Exception:
            db = {}
            
        if username in db and db[username] == password:
            self.current_user = username
            push_to_stack(f"User login: {username}")
            self.login_frame.destroy()
            self.setup_dashboard()
        else:
            messagebox.showerror("Authentication Error", "Invalid credentials entered.")

    def register_user(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        
        if len(username) < 3 or len(password) < 3:
            messagebox.showwarning("Warning", "Minimum 3 characters required for credentials.")
            return
            
        try:
            with open(USER_DB_FILE, 'rb') as f:
                db = pickle.load(f)
        except Exception:
            db = {}
            
        if username in db:
            messagebox.showerror("Registration Error", "User already exists in database.")
            return
            
        db[username] = password
        with open(USER_DB_FILE, 'wb') as f:
            pickle.dump(db, f)
            
        push_to_stack(f"Registered new user profile: {username}")
        messagebox.showinfo("Success", "Registration complete. You may now login.")

    def setup_dashboard(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.pack(side="right", fill="both", expand=True)

        logo_label = ctk.CTkLabel(self.sidebar_frame, text="CODEBREAKER", font=("Roboto", 22, "bold"))
        logo_label.pack(pady=30, padx=20)

        enc_str_btn = ctk.CTkButton(self.sidebar_frame, text="Encrypt Text", command=self.show_encrypt_string)
        enc_str_btn.pack(pady=10, padx=20)

        dec_str_btn = ctk.CTkButton(self.sidebar_frame, text="Decrypt Text", command=self.show_decrypt_string)
        dec_str_btn.pack(pady=10, padx=20)
        
        file_tool_btn = ctk.CTkButton(self.sidebar_frame, text="Bulk File Tool", command=self.show_file_tool)
        file_tool_btn.pack(pady=10, padx=20)

        hist_btn = ctk.CTkButton(self.sidebar_frame, text="Action Stack", command=self.show_history)
        hist_btn.pack(pady=10, padx=20)

        user_label = ctk.CTkLabel(self.sidebar_frame, text=f"User: {self.current_user}", font=("Roboto", 12))
        user_label.pack(side="bottom", pady=10)

        logout_btn = ctk.CTkButton(self.sidebar_frame, text="Logout System", command=self.logout, fg_color="#c0392b", hover_color="#922b21")
        logout_btn.pack(side="bottom", pady=20, padx=20)

        self.create_encrypt_string_frame()
        self.create_decrypt_string_frame()
        self.create_file_tool_frame()
        self.create_history_frame()
        
        self.show_encrypt_string()

    def clear_main_frame(self):
        for frame in self.frames.values():
            frame.pack_forget()

    def show_encrypt_string(self):
        self.clear_main_frame()
        self.frames["encrypt_string"].pack(fill="both", expand=True)

    def show_decrypt_string(self):
        self.clear_main_frame()
        self.frames["decrypt_string"].pack(fill="both", expand=True)
        
    def show_file_tool(self):
        self.clear_main_frame()
        self.frames["file_tool"].pack(fill="both", expand=True)

    def show_history(self):
        self.clear_main_frame()
        self.refresh_history()
        self.frames["history"].pack(fill="both", expand=True)

    def logout(self):
        push_to_stack(f"User logout sequence: {self.current_user}")
        self.current_user = ""
        self.sidebar_frame.destroy()
        self.main_frame.destroy()
        self.setup_login_frame()

    def create_encrypt_string_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.frames["encrypt_string"] = frame

        title = ctk.CTkLabel(frame, text="STRING ENCRYPTION ENGINE", font=("Roboto", 24))
        title.pack(pady=30)

        self.enc_input = ctk.CTkTextbox(frame, height=150)
        self.enc_input.pack(pady=10, padx=40, fill="x")

        process_btn = ctk.CTkButton(frame, text="Generate Secure Payload", width=200, command=self.process_encryption)
        process_btn.pack(pady=20)

    def process_encryption(self):
        raw_text = self.enc_input.get("1.0", "end-1c")
        if not raw_text.strip():
            messagebox.showwarning("Warning", "Input cannot be empty.")
            return

        raw_bytes = raw_text.encode('utf-8')
        enc_bytes, key_list = core_encrypt(raw_bytes)
        enc_hex = enc_bytes.hex()
        
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Encrypted File")
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(enc_hex)
            
            secure_payload = {
                "owner": self.current_user,
                "key": key_list
            }
            
            key_path = save_path.replace(".txt", "_key.dat")
            with open(key_path, 'wb') as f:
                pickle.dump(secure_payload, f)
                
            push_to_stack(f"Encrypted custom string -> {os.path.basename(save_path)}")
            messagebox.showinfo("Operation Successful", f"Data saved and secured for user: {self.current_user}\nDecryption Key: {os.path.basename(key_path)}")
            self.enc_input.delete("1.0", "end")

    def create_decrypt_string_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.frames["decrypt_string"] = frame

        title = ctk.CTkLabel(frame, text="STRING DECRYPTION ENGINE", font=("Roboto", 24))
        title.pack(pady=30)

        self.dec_output = ctk.CTkTextbox(frame, height=200)
        self.dec_output.pack(pady=10, padx=40, fill="x")

        process_btn = ctk.CTkButton(frame, text="Load Encrypted Files", width=200, command=self.process_decryption)
        process_btn.pack(pady=20)

    def process_decryption(self):
        txt_path = filedialog.askopenfilename(title="Select Encrypted Hex Text File", filetypes=[("Text Files", "*.txt")])
        if not txt_path:
            return
            
        dat_path = filedialog.askopenfilename(title="Select Binary Key File", filetypes=[("DAT Files", "*.dat")])
        if not dat_path:
            return

        try:
            with open(txt_path, 'r', encoding='utf-8') as f:
                enc_hex = f.read().strip()
                
            with open(dat_path, 'rb') as f:
                payload = pickle.load(f)

            if isinstance(payload, dict):
                if payload.get("owner") != self.current_user:
                    messagebox.showerror("ACCESS DENIED", f"Security Alert: This file is locked to user '{payload.get('owner')}'.")
                    push_to_stack(f"Unauthorized access attempt on {os.path.basename(dat_path)}")
                    return
                key_data = payload.get("key")
            else:
                key_data = payload

            try:
                enc_bytes = bytes.fromhex(enc_hex)
            except ValueError:
                messagebox.showerror("Fatal Error", "The file contains invalid hexadecimal data.")
                push_to_stack("Decryption failure: Invalid HEX format")
                return

            dec_bytes = core_decrypt(enc_bytes, key_data)
            
            if dec_bytes is None:
                messagebox.showerror("Fatal Error", "Key length mismatch detected. File corruption or wrong key.")
                push_to_stack("Decryption failure: Key Length Mismatch")
                return

            try:
                dec_string = dec_bytes.decode('utf-8')
            except UnicodeDecodeError:
                messagebox.showerror("Fatal Error", "Failed to decode bytes. The key may be incorrect.")
                push_to_stack("Decryption failure: Corrupted bytes")
                return

            self.dec_output.delete("1.0", "end")
            self.dec_output.insert("1.0", dec_string)
            push_to_stack(f"Successfully decrypted payload: {os.path.basename(txt_path)}")
            messagebox.showinfo("Success", "Security payload successfully decrypted.")

        except Exception as e:
            messagebox.showerror("System Error", f"Unexpected failure: {e}")

    def create_file_tool_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.frames["file_tool"] = frame

        title = ctk.CTkLabel(frame, text="BULK FILE ENCRYPTION TOOL", font=("Roboto", 24))
        title.pack(pady=30)
        
        info_label = ctk.CTkLabel(frame, text="Securely encrypt entire documents using XOR Cryptography.", font=("Roboto", 14))
        info_label.pack(pady=10)

        enc_file_btn = ctk.CTkButton(frame, text="Select File to Encrypt", width=250, command=self.process_file_encrypt)
        enc_file_btn.pack(pady=20)

    def process_file_encrypt(self):
        file_path = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_path:
            return
            
        try:
            with open(file_path, 'rb') as f:
                file_bytes = f.read()
                
            enc_bytes, key_list = core_encrypt(file_bytes)
            
            secure_payload = {
                "owner": self.current_user,
                "key": key_list
            }
            
            enc_path = file_path + ".locked"
            with open(enc_path, 'wb') as f:
                f.write(enc_bytes)
                
            key_path = file_path + ".dat"
            with open(key_path, 'wb') as f:
                pickle.dump(secure_payload, f)
                
            push_to_stack(f"Bulk encrypted file: {os.path.basename(file_path)}")
            messagebox.showinfo("Operation Complete", f"File secured successfully.\nLocked File: {os.path.basename(enc_path)}\nKey File: {os.path.basename(key_path)}")
            
        except Exception as e:
            messagebox.showerror("File Error", f"Could not process the file: {e}")

    def create_history_frame(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.frames["history"] = frame

        title = ctk.CTkLabel(frame, text="ACTION STACK HISTORY (LIFO)", font=("Roboto", 24))
        title.pack(pady=20)

        self.hist_output = ctk.CTkTextbox(frame, height=250, state="disabled")
        self.hist_output.pack(pady=10, padx=40, fill="both", expand=True)
        
        clear_btn = ctk.CTkButton(frame, text="Clear Stack", command=self.clear_history, fg_color="#d35400", hover_color="#a04000")
        clear_btn.pack(pady=10)

    def refresh_history(self):
        self.hist_output.configure(state="normal")
        self.hist_output.delete("1.0", "end")
        
        if not global_action_stack:
            self.hist_output.insert("end", "The stack is currently empty.\n")
        else:
            temp_list = []
            while global_action_stack:
                item = global_action_stack.pop()
                self.hist_output.insert("end", f"[ACTION] -> {item}\n")
                temp_list.append(item)
            
            temp_list.reverse()
            for item in temp_list:
                global_action_stack.append(item)
                
        self.hist_output.configure(state="disabled")

    def clear_history(self):
        global global_action_stack
        global_action_stack = []
        self.refresh_history()
        messagebox.showinfo("Stack Cleared", "Action history has been purged from memory.")

if __name__ == "__main__":
    app = CodebreakerApp()
    app.mainloop()