from datetime import datetime

# today's date
today = datetime.now();

transaction_number = 0


# after transaction
def after_transaction (balance, transaction):
    # input validation
    if not isinstance(balance, int) or not isinstance(transaction, int):
        return "At least one of your entries is not a whole number"

    # making the transaction_number variable globally accessible
    global transaction_number

    # transactional calculation
    new_balance = balance + transaction

    # updating transaction number
    transaction_number += 1

    # date in this format: 12:03:16 PM | Thu Jul 23, 2026.
    date = f"{today.strftime("%H")}:{today.strftime("%M")}:{today.strftime("%S")} {today.strftime("%p")} | {today.strftime("%a")} {today.strftime("%b")} {today.strftime("%d")}, {today.strftime("%Y")}."

    # returning the result of the transaction
    if new_balance < 0:
        return f"Your transaction is invalid. \nBalance: ${balance} \nTransaction Number: {transaction_number} \nStatus: Failed \nDate: {date} \n"
    else:
        return f"Your transaction was successful. \nBalance: ${new_balance} \nTransaction Number: {transaction_number} \nStatus: Successful \nDate: {date} \n"

print(after_transaction(5, 5))
print(after_transaction(500, 20))
print(after_transaction(300, -200))
print(after_transaction(3, -1000))
print(after_transaction(3, -4))
print(after_transaction(3, -3))