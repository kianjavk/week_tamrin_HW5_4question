from soale_3 import *


def main():
    products = [] # List of products in the store
    cart = Cart() # Shopping cart

    while True:
        try:
            print("\n---- Online Store ----")
            print("1. Add new product to the store")
            print("2. Display total number of products")
            print("3. Add product to cart")
            print("4. View cart")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                # Adding a new product to the store
                name = input("name: ")
                price = float(input("Enter the product price: "))
                product = Product(name, price)
                products.append(product)

                print(f"Product {name} with price {price} added to the store.")
                with open('products.txt', 'a') as f:
                    f.write(product.__str__())
                    f.write('\n')

            elif choice == "2":
                # Displaying the total number of products in the store
                print(f"Total number of products available: {Product.get_total_products()}")

            elif choice == "3":
                # Displaying the list of products and adding to the cart
                if not products:
                    print("No products available in the store.")
                else:
                    print("List of products available in the store:")
                    for i, product in enumerate(products):
                        print(f"{i + 1}. {product.name}: {product.price} toman ")
                    while True:
                        prod_index = int(input("Enter the number of the product you want to add to the cart: ")) - 1

                        if 0 <= prod_index < len(products):
                            cart.add_product(products[prod_index])
                            print(f"{products[prod_index].name} added to the cart.")
                        else:
                            print("Invalid product number.")
                        print("Do you wanna exit system? Yes or No: ")
                        x = input().lower()
                        if x == "yes":
                            print("Have a nice day!")
                            break
            elif choice == "4":
                # Displaying the shopping cart
                cart.show_cart()

            elif choice == "5":
                # Exiting the program
                print("Exiting the store. Have a nice day!")
                break

            else:
                print("Invalid option. Please try again.")


        except ValueError as e:
            print(e)



if __name__ == "__main__":
    main()