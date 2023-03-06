from main import Product
try:
    product_name =input("product name \n")
    product_quantity =input("product quantity \n")
    product_description =input("product description")
    product_colour =input("product colour \n")

    Product.create(prod_name=product_name, prod_quantity=product_quantity, prod_description=product_description,prod_colour=product_colour)
    print("Product Created Successfully")
except:
    print("Failed to Create Product")