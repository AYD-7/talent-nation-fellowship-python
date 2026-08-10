def calculate_subtotal (price, quantity):
    return price * quantity

def apply_discount (total, discount_rate):
    return total * (1.0 - discount_rate)

def format_receipt(customer_name, final_amount):
    return f"Receipt for {customer_name} : ${final_amount:.2f}"

print(__name__) # returns __main__

# writing a logic that will only run when this file runs directly not as an importable module
if __name__ == "__main__":
    print("=== Running billing.py Diagnostics ===")
    test_total = calculate_subtotal(4.50, 2)
    print(f"Test calculation (4.50 * 2): ₦{test_total:.2f}")
    print("Diagnostics complete!")


