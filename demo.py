#target transaction to search
target = "Withdrow $2000"

# Function to search for a transaction in nested history
def find_transaction(history, target_transaction):
    for item in history:
        if isinstance(item, list):
            if find_transaction(item, target_transaction):
                return True
        elif item == target_transaction:
            print(f"Transaction '{target_transaction}' found in history")
            return True
    return False

# Corrected simulated bank transaction history
transaction_history = [
    ["January",
     ["Week 1", "Deposit $1000", "Withdraw $2000"],
     ["Week 2", "Deposit $30000", "Withdraw $5500"]],
    ["February",
     ["Week 1", "Withdraw $1500"],
     ["Week 2", "Deposit $4500"]],
    ["March",
     ["Week 1", "Deposit $2500", "Withdraw $2000"],
     ["Week 2", "Deposit $8000", "Withdraw $1000"]]
]

# Target transaction to search
target = "Withdraw $2000"

# Call the function
found = find_transaction(transaction_history, target)
if not found:
    print(f"Transaction '{target}' not found.")


