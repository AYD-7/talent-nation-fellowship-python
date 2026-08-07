class KitchenCalculator:
    def calculate_inventory(self):
        customers = 3
        cereal_per_customer = 2.5
        milk_per_customer = 1.25
        
        starting_cereal = 10.0
        starting_milk = 15.0
        
        # 1. Use multiplication to calculate the totals needed
        total_cereal = cereal_per_customer * float(customers)  
        total_milk = milk_per_customer * float(customers) 
        
        # 2. Use subtraction to calculate the remaining inventory
        remaining_cereal = starting_cereal - total_cereal 
        remaining_milk = starting_milk - total_milk   
        
        return remaining_cereal, remaining_milk


def test_calculator():
    # Do not modify this testing wrapper
    calc = KitchenCalculator()
    return list(calc.calculate_inventory())

print(test_calculator())


# Arithmetic Report
def solution1(name, a, b, c):
    sum = a + b + c
    average = round(sum / 3, 2)
    maximum = max(a, b, c)
    

    return f"Student: {name}\nSum: {sum}\nAverage: {average}\nMaximum: {maximum}"

print(solution1("Joshua", 5, 46, 10))
print(solution1("Ada",10,20,30))