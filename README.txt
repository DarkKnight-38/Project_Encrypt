VANTACRYPT — HOW TO RUN
=======================

REQUIREMENTS
------------
- Python 3.8 or newer
- A terminal or command prompt
- The project files, including VantaCrypt.py and requirements.txt

All required third-party Python modules are listed in requirements.txt.


WINDOWS SETUP
-------------

1. Open Command Prompt or PowerShell.

2. Change to the folder containing VantaCrypt.py and requirements.txt.
   Example:

       cd path\to\VantaCrypt

3. (Recommended) Create a virtual environment:

       python -m venv .venv

4. Install the required modules:

       .\.venv\Scripts\python.exe -m pip install -r requirements.txt

5. Run VantaCrypt:

       .\.venv\Scripts\python.exe VantaCrypt.py


RUNNING IT AGAIN
----------------
After setup, open a terminal in the project folder and run:

    .\.venv\Scripts\python.exe VantaCrypt.py

If you have already installed the requirements into your active Python
environment, you can instead run:

    python VantaCrypt.py


MACOS OR LINUX
--------------
From the project folder, run:

    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    .venv/bin/python VantaCrypt.py


TROUBLESHOOTING
---------------
- If Python is not recognized, install Python and ensure it is available
  from your terminal. On Windows, try the py command instead of python.
- If a module is missing, install the dependencies again using:

      python -m pip install -r requirements.txt

  If you are using the virtual environment, use its Python interpreter
  to run pip, as shown in the setup instructions.
- Run commands from the project folder so relative file paths work.
- A terminal with Unicode and color support is recommended.
