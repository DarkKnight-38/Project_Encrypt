VANTACRYPT -- TERMINAL SECURITY SUITE
======================================

VantaCrypt is an educational, modular Python terminal security suite
featuring user authentication, password strength analysis, password
generation, credential vault management, terminal-based activity charts,
and multi-tiered file encryption (Shift, Vigenere, and XOR Stream ciphers).


REQUIREMENTS
------------
- Python 3.8 or newer
- Terminal or command prompt supporting ANSI color and Unicode
- Project files including VantaCrypt.py and requirements.txt

All third-party modules are listed in requirements.txt:
  - InquirerPy (interactive arrow-key terminal menus)
  - rich (styling, tables, panels, and progress bars)
  - plotext (terminal-rendered activity charts)


WINDOWS SETUP (POWERSHELL / CMD)
---------------------------------

1. Open PowerShell or Command Prompt.

2. Change to the folder containing VantaCrypt:
   
       cd path\to\Project_Encrypt

3. (Recommended) Create a virtual environment:

       python -m venv .venv

4. Install the required modules:

       .\.venv\Scripts\python.exe -m pip install -r requirements.txt

5. Run VantaCrypt:

       .\.venv\Scripts\python.exe VantaCrypt.py


RUNNING VANTA CRYPT AGAIN
-------------------------
After initial setup, open a terminal in the project directory and run:

    .\.venv\Scripts\python.exe VantaCrypt.py

If dependencies are already installed in your system Python:

    python VantaCrypt.py

Alternative Launchers:
- python Main.py       (Direct application controller)
- python Main_UI.py    (Compatibility launcher redirecting to Main.py)


MACOS OR LINUX SETUP
--------------------
From the project root folder, run:

    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    .venv/bin/python VantaCrypt.py


NAVIGATION & CONTROLS
---------------------
- Use the Up and Down arrow keys to navigate menus.
- Press Enter to confirm your selection.
- Sensitive inputs (passwords) are masked with asterisks (*).
- Use a terminal window of at least 90 columns for the best visual experience.


WHAT IS INCLUDED
----------------
1. Authentication: User registration, unique 8-digit UID generation, and login.
2. Password Strength Audit: 5-point evaluation meter with hardening tips.
3. Password Generator: Customizable random passwords (length 8-128).
4. Password Vault: Add, view, edit, and remove website credentials with password lock.
5. Minimum Cipher: Per-character random shift cipher with UID authorization.
6. Intermediate Cipher: Polyalphabetic Vigenere cipher using a custom keyword.
7. Maximum Cipher: Cryptographic XOR stream cipher with SHA-256 integrity check.
8. Session Action History: Chronological in-memory activity audit table.
9. Analytical Graph: Terminal horizontal bar chart of session events via plotext.


TROUBLESHOOTING
---------------
- "Python is not recognized":
  Make sure Python 3.8+ is installed and added to your system PATH.
  On Windows, try using "py" instead of "python".

- "No module named InquirerPy / rich / plotext":
  Install dependencies into your active environment using:
      pip install -r requirements.txt

- Relative paths and files missing:
  Always execute commands from the project root directory so relative
  paths (Data/UserData/ and Data/PWManagerData/) resolve correctly.

- Terminal display issues:
  Use a modern terminal such as Windows Terminal, PowerShell 7+, or
  standard Linux/macOS terminals with UTF-8 support enabled.


SECURITY NOTICE
---------------
VantaCrypt is developed for educational and experimental purposes.
Credentials and vault entries are stored unencrypted at rest.
Do not use this application to store real-world sensitive passwords.


CONTRIBUTORS
------------
- Sasank
- Raphael

- Terminal display issues:
  Use a modern terminal such as Windows Terminal, PowerShell 7+, or
  standard Linux/macOS terminals with UTF-8 support enabled.


SECURITY NOTICE
---------------
VantaCrypt is developed for educational and experimental purposes.
Credentials and vault entries are stored unencrypted at rest.
Do not use this application to store real-world sensitive passwords.


CONTRIBUTORS
------------
- Sasank
- Raphael

