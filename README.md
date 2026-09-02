# 🔐 Codebreaker — Security Suite

> **A modular, terminal-based Python security suite for encryption, password security, authentication, analytics, and more.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)

Codebreaker is a Python-based security toolkit designed to bring multiple security utilities together under one terminal application.

The project started as an exploration of encryption and authentication algorithms and is gradually evolving into a broader **personal security suite** containing encryption tools, password utilities, account management, activity tracking, data visualization, and other security-focused features.

> ⚠️ **This project is currently under active development.** Some features are complete, while others are planned or being implemented.

---

## ✨ Features

### 🔒 Encryption

Codebreaker currently includes custom encryption and decryption systems.

- **XOR-based encryption**
- SHA-256 integrity verification
- Per-user encryption watermarking
- Encryption key management
- User-specific decryption protection
- Planned Caesar Cipher
- Planned Vigenère Cipher

---

### 🔑 Authentication

User authentication provides the foundation for protecting user-specific data.

- User registration
- User login
- Unique User IDs
- Password confirmation
- Failed-attempt handling
- Planned logout system
- Planned user-data management

---

### 🛡️ Password Security

A collection of tools designed to help users create and evaluate stronger passwords.

#### Password Strength Tester

Checks passwords against multiple criteria:

- Minimum length
- Uppercase characters
- Lowercase characters
- Numbers
- Special characters
- Strength score
- Suggestions for improving weak passwords

#### Password Generator — Coming Soon

A dedicated password generator is planned with options for:

- Custom password length
- Uppercase characters
- Lowercase characters
- Numbers
- Special characters
- Randomized secure passwords

---

### 🔐 Password Manager — Coming Soon

A secure password-management system is planned for storing and managing account credentials.

Planned functionality:

- Add credentials
- View saved credentials
- Edit credentials
- Remove credentials
- Website/account organization
- Password generation
- Encrypted credential storage
- Authentication before accessing stored passwords

> The goal is to keep credentials encrypted rather than leaving a beautiful little collection of passwords sitting in plaintext waiting for disaster.

---

### 📊 Graph & Analytics — Coming Soon

Codebreaker will include data visualization and analytics for security-related information.

Planned functionality:

- Password-strength visualization
- Security statistics
- User activity graphs
- Historical data analysis
- Matplotlib-based visualizations

---

### 📜 Action History — Coming Soon

A session-based action history system will keep track of operations performed within the application.

Planned functionality:

- Record user actions
- Push actions into history
- Pop recent actions
- View session history
- LIFO stack-based implementation

Example:

```text
[22:14:03] User logged in
[22:14:18] Password strength tested
[22:15:02] File encrypted
[22:15:17] Password generated
```

---

## 🧩 Planned Architecture

Codebreaker is designed to remain modular so that individual security systems can be developed independently.

```text
Codebreaker
│
├── 🔒 Encryption
│   ├── XOR Encryption
│   ├── Caesar Cipher
│   └── Vigenère Cipher
│
├── 🔑 Authentication
│   ├── Registration
│   ├── Login
│   └── User Management
│
├── 🛡️ Password Security
│   ├── Password Strength
│   ├── Password Generator
│   └── Password Manager
│
├── 📜 Activity
│   └── Action History
│
├── 📊 Analytics
│   └── Graphs & Visualization
│
└── 🖥️ Terminal Interface
    └── Main Menu
```

---

## 📋 Feature Status

| Feature | Status |
|---|:---:|
| XOR Encryption | ✅ Complete |
| XOR Decryption | ✅ Complete |
| SHA-256 Integrity Checking | ✅ Complete |
| User Registration | ✅ Complete |
| User Login | ✅ Complete |
| Password Strength Tester | ✅ Complete |
| Main Menu | 🚧 In Development |
| Caesar Cipher | 🚧 Planned |
| Vigenère Cipher | 🚧 Planned |
| Password Generator | 🚧 Planned |
| Password Manager | 🚧 Planned |
| Action History | 🚧 Planned |
| Graph & Analytics | 🚧 Planned |
| Logout | 🚧 Planned |
| User Data Management | 🚧 Planned |

---

## 🛠️ Technologies

Codebreaker is built primarily with Python and focuses on implementing security concepts using Python's standard libraries and selected third-party modules.

### Core

- Python 3
- File I/O
- CSV
- Pickle
- Data structures
- Modular programming

### Security

- `hashlib`
- `secrets`
- Custom encryption algorithms
- SHA-256 hashing

### Visualization

- Matplotlib *(planned/being implemented)*

### Terminal Interface

- `pwinput`
- Terminal-based menus and interaction

---

## 📂 Project Structure

```text
Project_Encrypt/
│
├── Main_UI.py
│
├── Functions/
│   ├── Encryptions.py
│   ├── Decryption.py
│   ├── PW_Strength.py
│   ├── PW_Generator.py
│   ├── Graph.py
│   ├── Action_Hist.py
│   └── User_Auth.py
│
├── Data/
│   └── UserData/
│       └── user_data.csv
│
└── README.md
```

The structure will evolve as additional modules such as the password manager and analytics systems are implemented.

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- `pwinput`
- `matplotlib`

### Installation

```bash
git clone https://github.com/DarkKnight-38/Project_Encrypt.git
cd Project_Encrypt

pip install pwinput matplotlib
```

### Run

```bash
python Main_UI.py
```

---

## 🔬 Example

### Encrypting a message

```python
from Functions.Encryptions import max_encrypt
from Functions.Decryption import max_decrypt

uid = 12345678

max_encrypt(
    "Hello World",
    "cipher.txt",
    "keys.dat",
    uid
)

max_decrypt(
    "cipher.txt",
    "keys.dat",
    uid
)
```

---

## 🛣️ Roadmap

### Phase 1 — Core Security

- [x] XOR encryption
- [x] SHA-256 integrity verification
- [x] User registration
- [x] User authentication
- [x] Password strength analysis

### Phase 2 — Security Utilities

- [ ] Password generator
- [ ] Password manager
- [ ] Caesar cipher
- [ ] Vigenère cipher
- [ ] Improved encryption/decryption workflow

### Phase 3 — Monitoring & Analytics

- [ ] Action history
- [ ] Security activity logging
- [ ] Password statistics
- [ ] Graphs and visualization
- [ ] Security dashboard

### Phase 4 — Hardening

- [ ] Secure password hashing
- [ ] Improved key management
- [ ] Better data protection
- [ ] Input validation
- [ ] Error handling
- [ ] Security audit

---

## ⚠️ Security Notice

Codebreaker is primarily a **learning and development project**.

Some components currently use approaches that are not appropriate for production security systems. In particular:

- Password storage requires proper password hashing.
- Pickle files should never be loaded from untrusted sources.
- Custom cryptographic algorithms should not be considered replacements for established cryptographic libraries.
- Encryption key management is still under development.

Do **not** use the current development version to protect highly sensitive or critical information.

---

## 🎯 Project Goals

The long-term goal of Codebreaker is to turn a collection of individual Python security experiments into a unified security toolkit.

The project aims to explore:

- Cryptography
- Authentication
- Password security
- Secure storage
- Data structures
- File handling
- Data visualization
- Modular software architecture
- Security best practices

---

## 👨‍💻 Contributors

- **Sasank**
- **Raphael**

---

## 📌 Status

**Codebreaker is actively being developed.**

New security utilities, management tools, analytics features, and improvements are planned for future releases.

> *Break the code. Secure the data.* 🔐