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
    specials = event['specials']
    quantity = event['quantities'][0]['quantity']
    
    # Find totals
    productTotal = findProductTotal(products, quantity)
    specialsTotal = findSpecialsTotal(specials)

    # Build empty list to hold values, and then append
    lowestTotal = []
    lowestTotal.append(productTotal)
    lowestTotal.append(specialsTotal)

    # Find lowest value in list
    lowest = map(float, lowestTotal)

    # Response
    return {
        "statusCode": 200,
        "body": json.dumps(int(min(lowest)))
    }