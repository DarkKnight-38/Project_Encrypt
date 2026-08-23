# 🔐 Codebreaker — Security Terminal

A terminal-based Python security toolkit combining custom encryption, integrity hashing, user authentication, and password analysis — built as a hands-on exploration of core CS fundamentals (file I/O, data structures, and algorithmic logic).

![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Feature Status](#-feature-status)
- [How It Works](#-how-it-works)
- [Project Structure](#️-project-structure)
- [Getting Started](#-getting-started)
- [Quick Start Examples](#-quick-start-examples)
- [Known Limitations](#️-known-limitations)
- [Roadmap](#-roadmap)
- [Contributors](#-contributors)

---

## 🧭 Overview

Codebreaker is a modular command-line application organized around a few core systems:

- **Encryption Lab** — a bitwise XOR one-time-pad cipher with SHA-256 integrity verification and per-user watermarking
- **Authentication** — CSV-backed user registration and login
- **Password Toolkit** — a rule-based strength analyzer (generator planned)
- **Session Tools** — action history and data visualization (both planned)

The project is under active development — some modules are fully working, others are scaffolded but not yet implemented. The table below reflects the current state honestly so contributors know exactly what's left to build.

---

## ✅ Feature Status

| Module | Feature | Status |
|---|---|---|
| Encryption | Bitwise XOR cipher (`max_encrypt` / `max_decrypt`) | ✅ Complete |
| Encryption | Caesar cipher (`min_encrypt` / `min_decrypt`) | 🚧 Stub |
| Encryption | Vigenère cipher (`inter_encrypt` / `inter_decrypt`) | 🚧 Stub |
| Integrity | SHA-256 hash verification | ✅ Complete |
| Auth | Registration | ✅ Complete |
| Auth | Login | ✅ Complete |
| Auth | Logout | 🚧 Stub |
| Auth | Clear user data | 🚧 Stub |
| Password Tools | Strength tester | ✅ Complete |
| Password Tools | Password generator | 🚧 Stub |
| Session | Action history (LIFO stack) | 🚧 Stub |
| Analytics | Matplotlib visualization | 🚧 Stub |
| UI | Main menu routing | 🚧 Placeholder only |

---

## ⚙️ How It Works

### 🔒 Encryption Lab
`max_encrypt()` / `max_decrypt()` implement a one-time-pad-style cipher:

- Generates a cryptographically secure random key (via `secrets`) for every character in the input
- XORs each character against its key to produce ciphertext, written to a `.txt` file as hex
- Stores the keys, a SHA-256 signature of the original text, and the encrypting user's unique ID together in a pickled `.dat` file
- On decryption, the payload is **watermarked** — only the UID that created the file can decrypt it, and the SHA-256 signature is re-checked afterward to confirm the data wasn't tampered with

### 🔑 Authentication
User credentials are stored in `Data/UserData/user_data.csv`. On registration, a unique 8-digit ID is generated and passwords are confirmed with up to 3 retry attempts before the flow aborts.

### 📊 Password Strength Tester
Scores a password from 0–5 based on five criteria: minimum length (8+), uppercase, lowercase, digits, and special characters — then prints targeted suggestions for whichever checks failed.

---

## 🗂️ Project Structure

```
Codebreaker-Security-Terminal/
├── Main_UI.py
├── Functions/
│   ├── Action_Hist.py      # Session history stack (push/pop)
│   ├── Decryption.py       # Decryption engines
│   ├── Encryptions.py      # Encryption engines
│   ├── Graph.py            # Data visualization
│   ├── PW_Generator.py     # Password generator
│   ├── PW_Strength.py      # Password strength tester
│   └── User_Auth.py        # Login / registration
├── Data/
│   └── UserData/
│       └── user_data.csv
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- [`pwinput`](https://pypi.org/project/pwinput/) — required for masked password entry
- `matplotlib` — required once the visualization module is implemented

### Installation

```bash
git clone <repo-url>
cd Codebreaker-Security-Terminal
pip install pwinput matplotlib
```

> A `requirements.txt` isn't included yet — worth adding once dependencies are finalized.

### Running

```bash
python Main_UI.py
```

> Note: `main_menu()` currently just prints a header and returns — it isn't wired up to route between features yet. See [Known Limitations](#️-known-limitations).

---

## 🧪 Quick Start Examples

Since the main menu isn't fully routed yet, individual modules can be exercised directly:

**Encrypt & decrypt a message:**
```python
from Functions.Encryptions import max_encrypt
from Functions.Decryption import max_decrypt

uid = 12345678
max_encrypt("Hello World", "cipher.txt", "keys.dat", uid)
max_decrypt("cipher.txt", "keys.dat", uid)
```

**Test a password's strength:**
```python
from Functions.PW_Strength import strength_test
strength_test()
```

**Register and log in a user:**
```python
from Functions.User_Auth import register, login
register()
login()
```

---

## ⚠️ Known Limitations

- **Plaintext passwords** — `user_data.csv` currently stores passwords unhashed. Fine for a learning project, but hash (e.g. with `hashlib`) before storing if this is ever exposed beyond local use.
- **`pickle` deserialization** — `.dat` files are loaded with `pickle.load`, which executes arbitrary code for untrusted input. Only load `.dat` files you've generated yourself.
- **No menu routing yet** — `Main_UI.main_menu()` is a placeholder; modules must currently be called directly (see examples above).

---

## 🛣️ Roadmap

- [ ] Wire up `main_menu()` to route between all features
- [ ] Implement Caesar and Vigenère ciphers
- [ ] Implement password generator
- [ ] Implement action history stack (push/pop + session log view)
- [ ] Implement Matplotlib 3D visualization from logged password-test data
- [ ] Implement logout and clear-user-data
- [ ] Hash stored passwords instead of storing them in plaintext

---

## 👥 Contributors

- **Sasank**
- **Raphael**
