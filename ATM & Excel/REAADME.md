# Banking Management System (ATM Simulation) 🏦

> *A console-based ATM simulation built with Python & Excel*

---

## 💡 What is this?

A fully functional ATM simulation system where users can create accounts, login securely with PIN verification, and perform all basic banking operations. All data is stored and managed in an Excel file using Pandas.

---

## ✨ Features

### 👤 Account System
- **User Registration** — Set username, password, 4-digit PIN & initial balance
- **Secure Login** — Username + password + PIN triple verification
- **PIN Attempt Limit** — Account locked after 3 wrong PIN attempts
- **Duplicate Prevention** — Username already exists check

### 💰 Banking Operations
- **Check Balance** — View current account balance instantly
- **Deposit Money** — Add funds with full input validation
- **Withdraw Money** — Withdraw with insufficient balance check
- **Account Details** — View full account information
- **Logout** — Secure session logout

### 🗄️ Excel Database (Pandas)
- All user data stored in `Book2.xlsx`
- Auto-creates Excel file if it doesn't exist
- Real-time save after every transaction
- Data columns: Username, Password, PIN, Balance

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Core language |
| Pandas | Excel database read/write |
| OpenPyXL | Excel file support |
| OS module | File existence check |

---

## 📁 Project Structure

```
banking-management-system/
│
├── ATM & Excel.py    # Main application file
└── Book2.xlsx        # Excel database (auto-created)
```

---

## 🚀 How to Run

**1. Install required libraries:**
```bash
pip install pandas openpyxl
```

**2. Run the app:**
```bash
python "ATM & Excel.py"
```

---

## 🖥️ How it Works

```
===== MAIN MENU =====
1. Login
2. Create new account
3. Exit

===== MENU (After Login) =====
1. Account details
2. Check balance
3. Deposit money
4. Withdraw money
5. Logout
```

---

## 🔐 Security Features
- Password authentication
- 4-digit PIN verification
- 3 attempts limit before account lock
- Input validation on all fields

---

## 👨‍💻 Developer

**M. Yahya Iqbal**  
Software Engineering Student — Aligarh Institute of Technology, Karachi  
📧 muhammadyahyaiqbal1@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/yahya-iqbal) | [GitHub](https://github.com/Yahya-Iqbal1) | [Portfolio](https://yahya-iqbal.netlify.app)
