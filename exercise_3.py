import json

# Find total price of products function
def findProductTotal(products, quantity):
    totalPrice = 0
    
    for product in products:
        price = product['price']
        productPrice = price * quantity
        totalPrice = totalPrice + productPrice
    
    return totalPrice

# Find totoal number of specials function   
def findSpecialsTotal(specials):
    totalSpecials = 0
    
    for special in specials:
        total = special['total']
        totalSpecials = totalSpecials + total

    return totalSpecials

def lambda_handler(event, context):
    # Get the data
    data = event['body']
    
    # Load as json
    event = json.loads(data)

    # Parse data
    products = event['products']
    specials = event['specials'][0]
    quantities = event['quantities']
    
    Total = 0
    
    # Loop through orders, looking for specials
    for product in products:
        name = product['name']
        price = product['price']
        
        if specials['total'] != 0:
            total = specials['total']

            for quantity in specials['quantities']:
                if quantity['name'] == name:
                    quantity = quantity['quantity']
                    price = price - quantity
            
            price = price * total
        else:
            for quantity in quantities:
                if quantity['name'] == name:
                    quantity = quantity['quantity']
                    price = price * quantity
    
        Total = Total + price

    # Response
    return {
        "statusCode": 200,
        "body": json.dumps(Total)
    }