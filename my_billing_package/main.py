# imports
import billing # local import

# using functions in the billing module with the module name as prefix
base_cost = billing.calculate_subtotal(24, 5)
final_price = billing.apply_discount(base_cost, 0.10)

receipt = billing.format_receipt("Ajeboye", final_price)
print(receipt)

print(billing.__name__) # returns billing