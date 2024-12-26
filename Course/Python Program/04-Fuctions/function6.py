# Write a Python function to calculate the cost of a product, including optional tax and
# shipping charges. Use default arguments appropriately.
# The function should accept the following parameters:
# product_cost: The base cost of the product.
# tax_rate (default: 0.07): The tax rate to be applied to the product cost.
# shipping_cost (default: 5.0): The cost of shipping.
# The function should return the total cost of the product, which is the sum of
# the product cost, tax, and shipping charges
def cost(product_cost,tax_rate=0.07,shipping_tax=5.0):
    tax=product_cost*tax_rate
    shipping_charges=product_cost*shipping_tax
    total=product_cost+tax+shipping_charges
    print(total)
n=int(input("product_cost= "))
cost(n)