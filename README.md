# VantaCrypt — Terminal Security Suite

VantaCrypt is an educational, modular Python security application featuring password auditing, cryptographically random password generation, local credential vault management, terminal data visualizations, and multi-tier encryption experiments. Its interface combines modern Rich panels and tables with interactive InquirerPy arrow-key navigation.

> ⚠️ **Security Notice:** VantaCrypt is developed primarily for educational exploration and local experimentation. Account passwords and vault records are currently stored without encryption at rest. Do not use this tool to protect production or sensitive credentials.

---

## 🚀 Getting Started

### Prerequisites

- **Python:** Version 3.8 or newer.
- **Terminal:** A terminal supporting ANSI color and Unicode (e.g., Windows Terminal, PowerShell, iTerm2, or modern Linux shells). A wider terminal window ($\ge 90$ columns) is recommended for ASCII banners and credential tables.

### Quick Start (Windows PowerShell)

1. Clone or navigate to the project directory:
   ```powershell
   cd path\to\Project_Encrypt
   ```

2. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Launch VantaCrypt:
   ```powershell
   .\.venv\Scripts\python.exe VantaCrypt.py
   ```

*(If dependencies are already installed in your active Python environment, run `python VantaCrypt.py`).*

### Launchers

VantaCrypt supports multiple entry points for flexibility:
- **`VantaCrypt.py`** *(Primary Launcher)*: Starts the application via `Main.main_menu()`.
- **`Main.py`**: Direct controller file with interactive loops and tool routing.
- **`Main_UI.py`**: Backwards-compatible launcher script redirecting to `Main.py`.

On macOS/Linux, use `python3 -m venv .venv` and `.venv/bin/python VantaCrypt.py`. All storage paths are relative to the project root directory.

---

## 🎮 Navigation & Interface

- **Keyboard Navigation:** Use `↑` / `↓` arrow keys to highlight options and press `Enter` to select.
- **Masthead & Live Status Bar:** Displays the session user state (`[ACTIVE]` or `[GUEST]`), assigned 8-digit Unique ID (`UID`), live action counts, and vault item count.
- **Cyberpunk Color Theme:**
  - **Banner:** Neon Purple (`#a855f7`)
  - **Tool Panels & Prompts:** Electric Cyan (`#06b6d4` / `#38bdf8`)
  - **Credential Vault:** Amber / Gold (`#f59e0b` / `#facc15`)
  - **Session History:** Blue (`#3b82f6` / `#60a5fa`)
  - **Status Indicators:** Emerald Green (`#10b981`) for success, Crimson Red (`#ef4444`) for errors
- **Input Security:** Passwords and sensitive inputs are masked with asterisks (`*`) during entry.

---

## 🛠️ Feature Matrix

| Feature | Module | Current Status & Capabilities |
| :--- | :--- | :--- |
| **Authentication** | `Functions/User_Auth.py` | CSV-backed account storage (`user_data.csv`), password confirmation, automatic 8-digit UID generation, and session login/logout. |
| **Password Strength Audit** | `Functions/PW_Strength.py` | 5-rule complexity analysis (length $\ge 8$, uppercase, lowercase, numbers, special symbols) with visual meter and tailored hardening tips. |
| **Password Generator** | `Functions/PW_Generator.py` | Generates randomized passwords (length 8–128, default 16) with configurable character categories (lowercase, uppercase, digits, symbols). |
| **Credential Vault** | `Functions/PW_Manager.py` | Full credential lifecycle: **Add**, **View**, **Edit**, and **Remove** records. Non-empty vault viewing and edits require master account password authentication. |
| **Minimum Cipher** | `Functions/Encryption.py`<br>`Functions/Decryption.py` | Per-character dynamic shift cipher (range -20 to 20); outputs ciphertext `.txt` and pickled `.dat` key payload watermarked with the user's UID. |
| **Intermediate Cipher** | `Functions/Encryption.py`<br>`Functions/Decryption.py` | Polyalphabetic **Vigenère cipher** using a custom keyword; validates alphabetic characters and enforces UID decryption authorization. |
| **Maximum Cipher** | `Functions/Encryption.py`<br>`Functions/Decryption.py` | Cryptographic stream cipher: per-character XOR via `secrets.randbelow(256)`, hex-encoded ciphertext, and SHA-256 integrity verification. |
| **Session Action History** | `Functions/Action_Hist.py` | Chronological in-memory audit log of session events displayed in a formatted Rich table with color-coded status chips. |
| **Analytical Graph** | `Functions/Graphs.py` | Real-time terminal horizontal bar chart powered by `plotext`, grouping session activities by category (Vault, Ciphers, Auth, History). |

---

## 🔒 Cipher Files & Formats

Encryption operations generate two paired output files:
1. **Ciphertext File (`.txt`):** Stores shifted characters, Vigenère transformed characters, or hex-encoded XOR bytes.
2. **Key File (`.dat`):** A pickled binary payload containing the decryption keys/shifts/keywords and the owner's `UID`. Maximum mode also embeds a SHA-256 hash of the original plaintext.

Decryption requires both files and verifies that the logged-in user's `UID` matches the `uniqueid` recorded in the key file. Maximum decryption computes a fresh SHA-256 hash and compares it against the signature to detect file tampering.

---

## 📂 Project Structure

```text
Project_Encrypt/
├── VantaCrypt.py           # Primary application launcher
├── Main.py                 # Core controller, interactive menus & routing
├── Main_UI.py              # Compatibility entry point
├── UI.py                   # Rich presentation layer & InquirerPy prompts
├── requirements.txt        # Third-party dependencies
├── README.md               # Project documentation
├── README.txt              # Plain-text setup & troubleshooting guide
├── .gitignore
│
├── Functions/
│   ├── User_Auth.py        # Registration & login authentication portal
│   ├── PW_Strength.py      # Password audit meter & checklist
│   ├── PW_Generator.py     # Random password generation
│   ├── PW_Manager.py       # Credential vault CRUD operations
│   ├── Encryption.py       # Minimum, Intermediate (Vigenère), & Maximum encryption
│   ├── Encryptions.py      # Compatibility shim re-exporting Encryption
│   ├── Decryption.py       # Reverse transformation & SHA-256 integrity check
│   ├── Graphs.py           # Plotext terminal bar charts
│   ├── Graph.py            # Compatibility shim re-exporting Graphs
│   └── Action_Hist.py      # Session audit log
│
└── Data/
    ├── UserData/
    │   └── user_data.csv   # User credentials and assigned UIDs
    └── PWManagerData/
        └── password_vault_<UID>.dat  # Per-user credential vault files
```

---

## 📦 Dependencies

| Package | Purpose |
| :--- | :--- |
| `InquirerPy>=0.3.4` | Interactive terminal arrow-key menus, input prompts, and confirmations |
| `rich>=13.0.0` | Terminal formatting, colors, panels, tables, layout, and progress bars |
| `plotext>=5.3.2,<6` | Terminal-rendered horizontal bar charts for security analytics |

Install all dependencies with:
```powershell
pip install -r requirements.txt
```

---

## ⚠️ Known Limitations & Security Notes

- **Unencrypted Storage at Rest:** Account passwords in `user_data.csv` and vault entries in `password_vault_<UID>.dat` are stored unencrypted.
- **Pickle Security:** Python `pickle` deserialization should only be performed on trusted local files.
- **Educational Cryptography:** Custom shift and XOR ciphers serve as algorithmic demonstrations rather than replacements for standardized cryptographic algorithms (e.g., AES-GCM, ChaCha20-Poly1305).
- **Session Scope:** Action History and Analytical Graphs track events during the current running process; logs are cleared when the program exits.

---

## 👨‍💻 Contributors

- **Sasank**
- **Raphael**
