import pandas as pd
import os

FILE = "Book2.xlsx"
current_index = None  # ✅ Fix for undefined variable

# ---------- Load Excel ----------
if os.path.exists(FILE):
    df = pd.read_excel(FILE)
else:
    df = pd.DataFrame(columns=["username", "password", "pin", "balance"])
    df.to_excel(FILE, index=False)

# ---------- Save ----------
def save():
    df.to_excel(FILE, index=False)

# ---------- Register ----------
def register_user():
    global df
    u = input("Choose username: ").strip().lower()
    p = input("Set password: ").strip()
    pin = input("Set 4-digit PIN: ").strip()
    bal = input("Initial balance: ").strip()

    if u == "" or p == "" or pin == "" or bal == "":
        print("All fields required ❌")
        return

    if u in df["username"].str.lower().values:
        print("Username already exists ❌")
        return

    if not pin.isdigit() or len(pin) != 4:
        print("PIN must be 4 digits ❌")
        return
    pin = int(pin)

    if not bal.isdigit():
        print("Balance must be a number ❌")
        return
    bal = int(bal)

    df.loc[len(df)] = [u, p, pin, bal]
    save()
    print("Account created successfully ✅")

# ---------- Login ----------
def login_user():
    global current_index
    u = input("Username: ").strip().lower()
    p = input("Password: ").strip()

    

    user = df[
    (df["username"].str.lower().str.strip() == u) &
    (df["password"].astype(str).str.strip() == p)
]


    if user.empty:
        print("Invalid login ❌")
        return False

    current_index = user.index[0]

    # PIN verification
    attempts = 0
    while attempts < 3:
        pin_input = input("Enter PIN: ").strip()
        if pin_input.isdigit() and int(pin_input) == df.loc[current_index, "pin"]:
            print("Login successful ✅")
            return True
        else:
            print("Wrong PIN ❌")
            attempts += 1

    print("Account locked ❌")
    return False

# ---------- Deposit / Withdraw ----------
def deposit():
    global df
    amt = input("Enter deposit amount: ").strip()
    if not amt.isdigit() or int(amt) <= 0:
        print("Invalid amount ❌")
        return
    amt = int(amt)
    df.loc[current_index, "balance"] += amt
    save()
    print("Deposit successful ✅")
    print("New balance:", df.loc[current_index, "balance"])

def withdraw():
    global df
    amt = input("Enter withdraw amount: ").strip()
    if not amt.isdigit() or int(amt) <= 0:
        print("Enter positive amount ❌")
        return
    amt = int(amt)
    if amt > df.loc[current_index, "balance"]:
        print("Insufficient balance ❌")
        return
    df.loc[current_index, "balance"] -= amt
    save()
    print("Withdraw successful ✅")
    print("Remaining balance:", df.loc[current_index, "balance"])

# ---------- Dashboard / Menu ----------
def dashboard():
    while True:
        print("\n===== MENU =====")
        print("1. Account details")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Logout")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            print("\nAccount details:")
            print("Username:", df.loc[current_index, "username"])
            print("Balance:", df.loc[current_index, "balance"])
        elif choice == "2":
            print("Balance: Rs.", df.loc[current_index, "balance"])
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("Logging out... 👋")
            break
        else:
            print("Invalid choice ❌")

# ---------- MAIN ----------
while True:
    print("\n===== MAIN MENU =====")
    print("1. Login")
    print("2. Create new account")
    print("3. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        if login_user():
            dashboard()
    elif choice == "2":
        register_user()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")
