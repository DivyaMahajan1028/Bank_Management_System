
import mysql.connector
import random

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Divya@147",
    database="Bank_management_system"
)
print("Connected:", conn)
mycursor = conn.cursor()


def new_user():
    n = input("Enter Your Name: ").upper()
    p = random.randint(1000, 9999)
    print(f"Your PIN is: {p}")
    Amount = 0
    mycursor.execute("INSERT INTO customer_info(Name, pin, Balance) VALUES (%s, %s, %s)", (n, p, Amount))
    conn.commit()
    print("User registered successfully.\n")


def existing_user():
    N = input("Enter Your Name: ").upper()
    P = int(input("Enter Your PIN: "))

    
    mycursor.execute("SELECT * FROM customer_info WHERE Name = %s AND pin = %s", (N, P))
    result = mycursor.fetchone()

    if result:
        print(f"\nWelcome {N} to Your Account")
        while True:
            print("\nPlease select an option:")
            print("1) Credit")
            print("2) Debit")
            print("3) Check Balance")
            print("4) Delete Account")
            print("5)LogOut")
            choice = input("Enter Your Choice (1-5): ")

            if choice == "1":
                amount = int(input("Enter amount to deposit: "))
                mycursor.execute("UPDATE customer_info SET Balance = Balance + %s WHERE Name = %s AND pin = %s", (amount, N, P))
                conn.commit()
                print("Amount credited successfully.")

            elif choice == "2":
                amount = int(input("Enter amount to withdraw: "))
                mycursor.execute("SELECT Balance FROM customer_info WHERE Name = %s AND pin = %s", (N, P))
                current_balance = mycursor.fetchone()[0]
                if current_balance >= amount:
                    mycursor.execute("UPDATE customer_info SET Balance = Balance - %s WHERE Name = %s AND pin = %s", (amount, N, P))
                    conn.commit()
                    print("Amount debited successfully.")
                else:
                    print("Insufficient balance.")

            elif choice == "3":
                mycursor.execute("SELECT Balance FROM customer_info WHERE Name = %s AND pin = %s", (N, P))
                current_balance = mycursor.fetchone()[0]
                print(f"Your current balance is: Rs {current_balance}")

            elif choice == "4":
                confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
                if confirm == "yes":
                    mycursor.execute("DELETE FROM customer_info WHERE Name = %s AND pin = %s", (N, P))
                    conn.commit()
                    print("Your account has been deleted.")
                    break  
                else:
                    print("Account deletion cancelled.")

            elif choice == "5":
                print("Thank you for using the system. LogOut Successfully!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    else:
        print("Incorrect name or PIN. Please try again.\n")

# Main menu
def main():
    while True:
        user_type = input("EXISTING USER or NEW USER or EXIT: ").upper()
        if user_type == "NEW USER":
            new_user()
        elif user_type == "EXISTING USER":
            existing_user()
        elif user_type == "EXIT":
            print("EXIT SUCCESSFULLY!")
            break
        else:
            print("Invalid input. Please enter NEW USER, EXISTING USER, or Exit.")

main()



