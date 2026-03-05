<div align="center">

```
  _   _           _     ____            
 | | | | __ _ ___| |__ / ___| ___ _ __  
 | |_| |/ _` / __| '_ \| |  _ / _ \ '_ \ 
 |  _  | (_| \__ \ | | | |_| |  __/ | | |
 |_| |_|\__,_|___/_| |_|\____|\___|_| |_|
```

# #️⃣ HashGen — Text to Hash Converter

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=flat-square)]()
[![Author](https://img.shields.io/badge/Author-Mudasir%20Zia-purple?style=flat-square)](https://github.com/CyberBros435)

> **A powerful, terminal-based text-to-hash converter supporting 12 hashing algorithms.**  
> Instantly generate MD5, SHA family, and BLAKE2 hashes from any text — with a sleek, colorized CLI.

</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Supported Algorithms](#-supported-algorithms)
- [Requirements](#-requirements)
- [Quick Install (One Command)](#-quick-install-one-command)
- [Step-by-Step Installation](#-step-by-step-installation)
- [Usage](#-usage)
- [Example Session](#-example-session)
- [Project Structure](#-project-structure)
- [Related Projects](#-related-projects)
- [Author](#-author)
- [Disclaimer](#-disclaimer)

---

## 🧠 About

**HashGen** is a Python CLI tool that converts any plain text into a cryptographic hash using your choice of 12 industry-standard algorithms. It features a clean loop-based interface — select an algorithm, hash as many strings as you want, then switch algorithms or exit — all without restarting the tool.

Built for **cybersecurity learners, developers, CTF players, and anyone** who needs quick, reliable hash generation from the terminal.

---

## ✨ Features

| Feature | Description |
|---|---|
| #️⃣ **12 Hash Algorithms** | MD5, SHA-1, SHA-2 family, SHA-3 family, BLAKE2b, BLAKE2s |
| 🔁 **Loop Mode** | Hash unlimited strings per algorithm without restarting |
| 🎨 **ASCII Banner** | Dynamic algorithm banners generated with `pyfiglet` |
| 🛡️ **Input Validation** | Rejects empty inputs with clear error messages |
| 🎨 **Colorized CLI** | Clean color-coded output via `colorama` |
| ❌ **Safe Exit** | Type `q` to return to main menu anytime |

---

## 🔐 Supported Algorithms

| # | Algorithm | Output Length | Type |
|---|---|---|---|
| 1 | **MD5** | 128-bit (32 hex) | Legacy digest |
| 2 | **SHA-1** | 160-bit (40 hex) | Legacy digest |
| 3 | **SHA-224** | 224-bit (56 hex) | SHA-2 family |
| 4 | **SHA-256** | 256-bit (64 hex) | SHA-2 family |
| 5 | **SHA-384** | 384-bit (96 hex) | SHA-2 family |
| 6 | **SHA-512** | 512-bit (128 hex) | SHA-2 family |
| 7 | **SHA3-224** | 224-bit (56 hex) | SHA-3 family |
| 8 | **SHA3-256** | 256-bit (64 hex) | SHA-3 family |
| 9 | **SHA3-384** | 384-bit (96 hex) | SHA-3 family |
| 10 | **SHA3-512** | 512-bit (128 hex) | SHA-3 family |
| 11 | **BLAKE2b** | 512-bit (128 hex) | Modern digest |
| 12 | **BLAKE2s** | 256-bit (64 hex) | Modern digest |

---

## ⚙️ Requirements

- **OS:** Windows / Linux / macOS (cross-platform)
- **Python:** 3.7 or higher
- **Dependencies:**

```
colorama==0.4.6
pyfiglet==0.8.1
```

---

## ⚡ Quick Install (One Command)

```bash
git clone https://github.com/CyberBros435/Hash_Generator.git && cd Hash_Generator && pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

---

## 🛠️ Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/CyberBros435/Hash_Generator.git
```

### 2. Navigate into the Project Directory

```bash
cd Hash_Generator
```

### 3. (Optional) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install colorama==0.4.6 pyfiglet==0.8.1
```

### 5. Run the Tool

```bash
python main.py
```

---

## 🚀 Usage

On launch, you'll see the ASCII banner and the main menu:

```
[ 1 ]. MD5
[ 2 ]. SHA1
[ 3 ]. SHA224
[ 4 ]. SHA256
[ 5 ]. SHA384
[ 6 ]. SHA512
[ 7 ]. SHA3_224
[ 8 ]. SHA3_256
[ 9 ]. SHA3_384
[ 10 ]. SHA3_512
[ 11 ]. BLAKE2B
[ 12 ]. BLAKE2S
[ 13 ]. EXIT
```

Select a number and press `Enter`. You'll enter a loop for that algorithm where you can hash as many strings as you like.

---

## 💻 Example Session

```
Enter Your choice:   4

  ____  _   _    _     ____  ____   ___
 / ___|| | | |  / \   |___ \| ___| / __|
 \___ \| |_| | / _ \    __) |___ \| (__
  ___) |  _  |/ ___ \  / __/ ___) |\__ \
 |____/|_| |_/_/   \_\|_____|____/ |___/

Enter Your Text (q -> "exit"):   hello
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Enter Your Text (q -> "exit"):   CyberBros
7f8a4c3e9d1b2f6a...

Enter Your Text (q -> "exit"):   q
```

Returns to the main menu after `q`.

---

## 📁 Project Structure

```
Hash_Generator/
│
├── main.py               # Main entry point & all hash logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🔗 Related Projects

> Part of the **CyberBros435** network & security toolkit collection:

| Tool | Description | Link |
|---|---|---|
| 🔍 **IP Scanner** | IPv4 scanner, ping, tracert & ipconfig | [CyberBros435/IP_Scanner](https://github.com/CyberBros435/IP_Scanner) |
| 🌐 **DNS Server** | Hostname to IPv4 resolver | [CyberBros435/DNS_Server](https://github.com/CyberBros435/DNS_Server) |
| #️⃣ **Hash Generator** | Text to hash converter *(this repo)* | [CyberBros435/Hash_Generator](https://github.com/CyberBros435/Hash_Generator) |
| 🔎 **Hash Identifier** | Identify unknown hash types | [CyberBros435/Hash_Identifier](https://github.com/CyberBros435/Hash_Identifier) |

---

## 👤 Author

**Mudasir Zia**  
🔗 GitHub: [@CyberBros435](https://github.com/CyberBros435)  
📦 Repository: [CyberBros435/Hash_Generator](https://github.com/CyberBros435/Hash_Generator)

---

## ⚠️ Disclaimer

> This tool is intended **for educational and authorized use only.**  
> The author is **not responsible** for any misuse of this software.  
> Always use hashing tools **responsibly and ethically.**

---

<div align="center">

Made with ❤️ by [Mudasir Zia](https://github.com/CyberBros435) · ⭐ Star this repo if you found it useful!

</div>
