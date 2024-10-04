# Product list
product_id = [1, 2, 3, 4, 5]
product_name = ["Apple", "Carrots", "CornBeef", "Pork", "Oishi"]
product_category = ["Fruits", "Vegetables", "Canned Goods", "Meat", "Snacks"]
product_quantity = [10, 10, 20, 5, 3]
product_price = [40, 30, 60, 80, 15]

# Product management system
print("Welcome to the Product Management System \n1. Add new product \n2. Search product")
choose = int(input("Only number: \nEx. 1 or 2\nEnter here: "))

if choose == 1:
    id = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    print("Available categories:")
    for i, category in enumerate(product_category):
        print(f"{i+1}. {category}")
    category_choice = int(input("Enter the number of your chosen category: "))
    category = product_category[category_choice - 1]
    quantity = int(input("Enter product quantity: "))
    price = int(input("Enter product price: "))
    product_id.append(id)
    product_name.append(name)
    product_category.append(category)
    product_quantity.append(quantity)
    product_price.append(price)
    print("Product added successfully!")
    print(product_id)
    print(product_name)
    print(product_category)
    print(product_quantity)
    print(product_price)
elif choose == 2:
    search = int(input("Search product ID: "))
    if search in product_id:
        index = product_id.index(search)
        print("Product found!")
        print("ID:", product_id[index])
        print("Name:", product_name[index])
        print("Category:", product_category[index])
        print("Quantity:", product_quantity[index])
        print("Price:", product_price[index])
    else:
        print("Product not found")
else:
    print("Please try again")