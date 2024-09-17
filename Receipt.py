def create_receipt(items):
    total = 0

    print("==== Receipt ====")
    
    for item, price in items.items():
        print(f"{item}: ₱{price}")
        total += price
    
    print("=================")
    print(f"Total: ₱{total}")
    print("=================")

items = {
    "Jersey ": 300,
    "Infinix Note 40": 10_999,
    "Shoes": 999
}

create_receipt(items)
