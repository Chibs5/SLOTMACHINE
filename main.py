MAX_LINES = 3

def deposit():
    while True:
        amount = input("Enter the amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Invalid input. Please enter a valid amount.")

    return amount

def get_number_of_line():
    

def main():
    balance = deposit()

main()
