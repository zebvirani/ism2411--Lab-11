#reflection questions
#1.  i would use get when im not sure if a dictionary has a key to avoid errors
# i would use brackets when i know for sure a key exists
#2. it reminds me of a spreadsheet.. I dont use excel that much yet
#python may be more useful for bigger sets of data because of its ability to automate and process
#exercise 1

customer = {
    "name": "zeb",
    "email": "zebawesome@gmail.com",
    "tier": "gold",
    "ytd_spend": 1000
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

#exercise2

customer["phone"] = "123-456-7890"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

#exercise 3
email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("keyerror!: Email doesnt exist")

#exercise4
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)
#without items(), the loops only returns the keys

#exercise5
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final Price: ${final_price:.2f}")

#exercise6

# Exercise 6 - List of Dicts

customers = [
    {"name": "zeb", "tier": "platinum"},
    {"name": "zebjr", "tier": "gold"},
    {"name": "zebsr", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * rate

    print(f"{name} , {tier} , Discount: ${discount_amount:.2f}")

#exercise7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} left")

#exercise8
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
