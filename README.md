<div align="center">

# 🎟️ PyTicket - Telegram IT Support Bot

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Telegram API](https://img.shields.io/badge/Telegram-Bot_API-2CA5E0.svg?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots)
[![Git Workflow](https://img.shields.io/badge/Workflow-Feature_Branches-brightgreen.svg?style=for-the-badge&logo=github&logoColor=white)]()

*A lightweight, asynchronous Telegram bot designed to streamline IT support requests directly via chat. Built for 24/7 deployment on a Raspberry Pi.*

*(Demo GIF coming soon)*

</div>

---

## 💡 About The Project

Traditional ticketing systems are often clunky and require users to log into complex web portals. **PyTicket** brings the support desk directly to where the users already are: their messenger. 

Users can open, view, and close IT support tickets via simple Telegram commands. The bot is fully asynchronous, ensuring non-blocking performance even when handling multiple users simultaneously.

### ✨ Key Features
* **Frictionless Ticket Creation:** Users can open tickets instantly via `/ticket <description>`.
* **Real-Time Status Tracking:** List all active issues using `/tickets`.
* **Quick Resolution:** Resolve and archive tickets using `/close <id>`.
* **Persistent Storage:** Fully integrated with a PostgreSQL database to ensure no data is lost during restarts.
* **Always On:** Configured to run as a continuous background service on a Raspberry Pi.

---

## 🛠️ Tech Stack & Architecture

* **Language:** Python 3.11+
* **Framework:** `python-telegram-bot` (Asynchronous / asyncio)
* **Database:** PostgreSQL (Replacing the initial in-memory prototype)
* **Environment:** `python-dotenv` for secure credential management
* **Hardware:** Raspberry Pi (Deployment)

### 🧑‍💻 Development Workflow (Note for Recruiters)
This project was built adhering to strict industry standards:
* **GitHub Flow:** Strict use of `feature/*` branches and Pull Requests. No direct commits to `main`.
* **Clean Code:** Adherence to PEP 8 standards, static type hinting (`typing`), and early return patterns.
* **Iterative Prototyping:** Transitioned from an in-memory dictionary data store to a robust PostgreSQL relational database.

---

## 🚀 Local Setup & Installation

Want to run this bot locally? Follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DarJas0/py-ticket-system.git
   cd py-ticket-system
   ```
   
2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Environment Variables:**

   Create a `.env` file in the root directory and add your Telegram Bot Token and database credentials:
   ```bash
   TELEGRAM_TOKEN=your_secure_token_here
   DB_HOST=localhost
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_NAME=pyticket
   ```
   
5. **Run the bot:**
   ```bash
   python main.py
   ```
   
<div align="center">
<i>Built with clean architecture in mind by Dardan.</i>
</div>