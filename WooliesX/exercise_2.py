import json
import os
import urllib2
from operator import itemgetter

# Sort data function
def sortData(action, productData):
    # Wish Python had switch statements
    if action == 'low':
        sortedData = sorted(productData, key=itemgetter('price'))
    elif action == 'high':
        sortedData = sorted(productData, key=itemgetter('price'), reverse=True)
    elif action == 'ascending':
        sortedData = sorted(productData, key=itemgetter('name'))
    elif action == 'descending':
        sortedData = sorted(productData, key=itemgetter('name'), reverse=True)
    elif action == 'recommended':
        # Create empty list for ordering later on
        orderDict = []
        
        # Loop through product data
        for block in productData:
            # For each customer order, grab quantity purchased
            for product in block['products']:
                name = product['name']
                price = product['price']
                quantity = product['quantity']

                newlist = {}
                newlist['name'] = name
                newlist['price'] = price
                newlist['quantity'] = quantity
                
                if any(d['name'] == name for d in orderDict):
                    for index,item in enumerate(orderDict):
                        if orderDict[index].get('name') == name:
                            orderDict[index]['quantity'] = orderDict[index]['quantity'] + quantity
                else:
                    orderDict.append(newlist)
        # Sort the data
        sortedData = orderDict
        sortedData = sorted(orderDict, key=itemgetter('quantity'), reverse=True)

    return sortedData
    
def lambda_handler(event, context):
    # Products url and token are environment vars
    baseUrl = str(os.environ['baseUrl'])
    token = str(os.environ['token'])
    productsUri = str(os.environ['productsUri'])
    shopperhistoryUri = str(os.environ['shopperhistoryUri'])
    
    productsUrl = baseUrl + productsUri + "?token=" + token
    shopperhistoryUrl = baseUrl + shopperhistoryUri + "?token=" + token
    
    # Default sortAction if none passed
    sortAction = 'low'

    if 'queryStringParameters' in event:    
        if event['queryStringParameters'] is not None:
            if 'sortOption' in event['queryStringParameters']:
                querytest = event['queryStringParameters']['sortOption']
    
                if querytest is not None:
                    sortAction = str(event['queryStringParameters']['sortOption']).lower()

    # Change uri to hit if sortAction == Recommended
    if sortAction == 'recommended':
        uri = shopperhistoryUrl
    else:
        uri = productsUrl

    # Open the connection to the api endpoint and read the data.
    # Load as json object for parsing.
    request = urllib2.Request(uri)
    response = urllib2.urlopen(request)
    data = response.read()
    productData = json.loads(data)
    
    sortedProductData = sortData(sortAction, productData)
    
    # Response
    if sortedProductData is not None:
        return {
            "statusCode": 200,
            "body": json.dumps(sortedProductData)
        }