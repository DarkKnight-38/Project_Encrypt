# 🔐 VantaCrypt — Security Suite

> **A modular, terminal-based Python security suite for encryption, password security, authentication, analytics, and credential management.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)

VantaCrypt is a Python-based security toolkit designed to bring multiple security utilities together under a unified, interactive terminal application.

The project began as an exploration of encryption and authentication algorithms and has evolved into a **personal security suite** containing encryption tools, password evaluation and generation utilities, credential vault management, session tracking, and data visualization.

---

## ✨ Features

### 🔒 Encryption & Decryption

Custom multi-tiered encryption and integrity verification systems:

- **Maximum Encryption (XOR Stream Cipher)**: Cryptographically secure key stream generated via `secrets.randbelow(256)`, hex-encoded ciphertext, SHA-256 cryptographic signature, and owner UID watermarking.
- **Minimum Encryption (Shift Cipher)**: Variable per-character shift cipher with user authorization checking.
- **Integrity Verification**: Automatic SHA-256 hash comparison during decryption to detect any data tampering.
- **Access Control**: Watermarked Unique ID (UID) verification prevents unauthorized users from decrypting sensitive files.
- **Planned Ciphers**: Intermediate Vigenère cipher in development.

---

### 🔑 Authentication

Secure, session-based user authentication:

- User registration and login with masked input (`pwinput`).
- Automated 8-digit unique ID (`UID`) generation.
- Password confirmation and credential validation.
- Auto-initialization of user storage (`Data/UserData/user_data.csv`).
- Clean session logout and re-authentication support.

---

### 🛡️ Password Security

A collection of utilities designed to evaluate, generate, and store secure credentials.

#### 1. Password Strength Tester
Evaluates passwords against 5 security criteria with actionable improvement suggestions:
- Length ($\ge 8$ characters)
- Uppercase letters
- Lowercase letters
- Numerical digits
- Special symbols

#### 2. Password Generator
Generates cryptographically random passwords tailored to user specifications:
- Configurable length (8 to 512 characters) with numeric input validation.
- Optional character sets (lowercase, uppercase, numbers, symbols).
- Seamless integration with the Password Manager for one-step credential storage.

#### 3. Password Manager (Vault)
An authentication-gated credential manager storing account information per user UID:
- **Add**: Store website, username, password (manual or generated), and notes.
- **View**: Display saved credentials after password verification.
- **Edit**: Update credentials and notes for existing website entries.
- **Remove**: Securely delete entries from the vault.
- **Safe Storage**: Multi-record serialized vault files (`Data/PWManagerData/password_vault_<UID>.dat`) with corruption and EOF recovery.

---

### 📜 Action History

In-memory session audit logging that tracks all operations performed in the application:
- Logs authentication events, tool launches, encryption tasks, and vault interactions.
- Formatted chronological history viewer with empty state awareness.

---

### 📊 Graph & Analytics — In Development

Visual data analytics for security patterns and activity tracking:
- Password strength trend graphs.
- Historical user activity visualization.
- Matplotlib-based dashboard.

---

### 🛡️ Crash Protection & Error Handling

Engineered for stability and clean user interaction:
- **Input Validation**: Re-prompts on invalid numerical inputs (`ValueError`) without crashing.
- **Missing File Auto-Creation**: Creates required folders and CSV headers on demand.
- **Corrupt File Safeguards**: Catches corrupt pickle payloads, non-hex ciphertext, and truncated files gracefully.
- **Terminal Compatibility**: Uses ASCII-safe indicators to prevent Windows terminal `UnicodeEncodeError` (`cp1252`).
- **Signal Handling**: Gracefully catches `Ctrl+C` (`KeyboardInterrupt`) and `EOFError` across all menus.
- **Global Exception Boundary**: Catches unexpected tool exceptions in the main loop to preserve the active session.

---

## 📋 Feature Status

| Feature | Status |
|---|:---:|
| XOR Encryption (Maximum) | ✅ Complete |
| XOR Decryption & SHA-256 Verification | ✅ Complete |
| Shift Cipher (Minimum) | ✅ Complete |
| User Registration & Login | ✅ Complete |
| Password Strength Tester | ✅ Complete |
| Password Generator | ✅ Complete |
| Password Manager (Add, View, Edit, Remove) | ✅ Complete |
| Action History Session Logging | ✅ Complete |
| Interactive Terminal UI (`InquirerPy` + `rich`) | ✅ Complete |
| Robust Error Handling & Crash Prevention | ✅ Complete |
| User Logout | ✅ Complete |
| Intermediate Encryption (Vigenère) | 🚧 Planned |
| Graph & Analytics (Matplotlib) | 🚧 In Development |

---

## 🛠️ Technologies

- **Language**: Python 3.x
- **CLI & Formatting**: [InquirerPy](https://github.com/kazhala/InquirerPy), [Rich](https://github.com/Textualize/rich)
- **Input Security**: [pwinput](https://github.com/asweigart/pwinput)
- **Standard Libraries**: `secrets`, `hashlib`, `pickle`, `csv`, `os`, `random`, `string`

---

## 📂 Project Structure

```text
Project_Encrypt/
│
├── Main_UI.py                      # Interactive CLI entry point and menu router
├── requirements.txt                # Python dependencies
│
├── Functions/
│   ├── User_Auth.py                # Registration and login logic
│   ├── Encryptions.py              # Shift and XOR stream encryption
│   ├── Decryption.py               # Decryption and SHA-256 verification
│   ├── PW_Strength.py              # Password evaluation engine
│   ├── PW_Generator.py             # Random password generator
│   ├── PW_Manager.py               # Encrypted vault CRUD operations
│   ├── Action_Hist.py              # Session audit logger
│   └── Graph.py                    # Analytics stub
│
├── Data/
│   ├── UserData/
│   │   └── user_data.csv           # Registered users and assigned UIDs
│   └── PWManagerData/
│       └── password_vault_<UID>.dat # User credential vaults
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or newer
- `pip` package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DarkKnight-38/Project_Encrypt.git
   cd Project_Encrypt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python Main_UI.py
```

---

## ⚠️ Security Notice

VantaCrypt is developed primarily as an **educational and experimental security suite**.

While algorithms use Python's cryptographically secure `secrets` library and SHA-256 integrity verification:
- Password credentials in `user_data.csv` should be hashed with a slow KDF (e.g., bcrypt/Argon2) before production deployment.
- Deserialization with `pickle` should only be conducted on trusted local files.
- Do not use this tool as a primary replacement for audited enterprise password managers.

---

## 👨‍💻 Contributors

- **Sasank**
- **Raphael**

---

## 📌 Status

*Active Development — Break the code. Secure the data.* 🔐