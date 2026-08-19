# 🛡️ Codebreaker Security Terminal

A comprehensive, terminal-based cybersecurity suite and cryptography lab built with Python. 

This project was developed to demonstrate core computer science principles including **Data Structures (Stacks)**, **Binary File Handling**, **Algorithmic Logic**, and **Data Visualization**. It serves as a fully functional security terminal complete with user authentication, encryption engines, and password analysis tools.

---

## 📋 Table of Contents
- [Features](#-features)
- [Syllabus Mapping](#-syllabus-mapping)
- [Tech Stack & Libraries](#-tech-stack--libraries)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)

---

## 🚀 Features

### 1. The Encryption Lab
A three-tier cryptography engine demonstrating the evolution of data security:
*   **Caesar Cipher (Basic):** Shift-based alphabetical encryption.
*   **Vigenère Cipher (Intermediate):** Keyword-based polyalphabetic substitution.
*   **Bitwise XOR Engine (Maximum Security):** A custom One-Time Pad encryption using the `secrets` module, `bytearray` manipulation, and bitwise XOR (`^`) mathematics.

### 2. Hashing Protocols
*   **SHA-256 Hashing:** Simulates one-way data protection for verifying text integrity, utilizing Python's built-in `hashlib`.

### 3. User Authentication System
*   Secure Login and Signup system.
*   Stores user credentials locally using the `pickle` module to write and read `.dat` binary dictionaries.

### 4. Advanced Password Toolkit
*   **Strength Tester:** Analyzes password length, complexity, and character types to output a mathematical security score (0-100).
*   **Secure Generator:** Automatically generates complex, high-entropy passwords based on user parameters.

### 5. Data Analytics & Visualization
*   Logs password testing data (Length, Complexity, Score) to a `.csv` file.
*   Parses the CSV data to render an interactive **3D Scatter Plot** using `matplotlib`.

### 6. Session Action History (Data Structures)
*   Implements a **LIFO (Last-In, First-Out) Stack** using Python lists.
*   Pushes all user actions (e.g., "Encrypted File", "Tested Password") to the stack and pops them for session history viewing.

---

## 📚 Syllabus Mapping (Class 12 CS)

This project strictly adheres to and exceeds the CBSE Class 12 Computer Science requirements:
*   **File Handling:** Text files (`.txt`), Binary files (`pickle` / `.dat`), and CSV files (`.csv`).
*   **Data Structures:** Implementation of a Stack (Push/Pop operations).
*   **Data Visualization:** Interactive plotting using `matplotlib.pyplot`.
*   **Control Flow & Logic:** Advanced string manipulation, `while` loops, and error handling.

---

## 💻 Tech Stack & Libraries

**Core Language:** Python 3  
**External Libraries Required:**
*   `matplotlib` (For 3D data visualization)

**Built-in Python Modules Used:**
*   `pickle` (Binary file handling)
*   `csv` (Data logging)
*   `hashlib` (SHA-256 generation)
*   `secrets` (Cryptographically secure random number generation)
*   `os` (Terminal screen clearing and file system management)

---

## ⚙️ Installation & Setup

1. **Clone or Download the Repository:**
   Extract the project files into a dedicated folder.

2. **Install Dependencies:**
   Open your terminal or command prompt and install the required visualization library:
   ```bash
   pip install matplotlib