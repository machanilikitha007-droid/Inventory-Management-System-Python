products = {}

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    products[product_id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    print("Product added successfully!")


def view_products():
    if not products:
        print("No products found.")
        return

    print("\n===== INVENTORY =====")

    for product_id, product in products.items():
        print("Product ID:", product_id)
        print("Name:", product["name"])
        print("Quantity:", product["quantity"])
        print("Price: ₹", product["price"])
        print("--------------------")


def search_product():
    product_id = input("Enter Product ID to search: ")

    if product_id in products:
        product = products[product_id]

        print("\nProduct Found!")
        print("Product ID:", product_id)
        print("Name:", product["name"])
        print("Quantity:", product["quantity"])
        print("Price: ₹", product["price"])
    else:
        print("Product not found.")


def delete_product():
    product_id = input("Enter Product ID to delete: ")

    if product_id in products:
        del products[product_id]
        print("Product deleted successfully!")
    else:
        print("Product not found.")


while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
