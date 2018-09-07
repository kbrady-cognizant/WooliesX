import json

keys = ['name', 'token']

# Mock userlist
name0 = ['Kirk Brady', '1234-455662-22233333-3334']
name1 = ['test', '1234-455662-22233333-3333']
name2 = ['Craig', '1234-455662-22233333-3335']
name3 = ['Pamela', '1234-455662-22233333-3336']
name4 = ['Kunal', '1234-455662-22233333-3337']
name5 = ['Hamid', '1234-455662-22233333-3338']
name6 = ['Shekhar', '1234-455662-22233333-3339']
name7 = ['Rob', '1234-455662-22233333-3340']

# Create empty list and add mock users
userList = []
userList.append(dict(zip(keys, name0)))
userList.append(dict(zip(keys, name1)))
userList.append(dict(zip(keys, name2)))
userList.append(dict(zip(keys, name3)))
userList.append(dict(zip(keys, name4)))
userList.append(dict(zip(keys, name5)))
userList.append(dict(zip(keys, name6)))
userList.append(dict(zip(keys, name7)))

# Find user function
def finduser(username):
    print("Finding user "+ username)
    data = dictlookup(username)
    
    if data is None:
        print("Could not find user " + username)

    print("Found user " + username)
    return data

# Lookup user function
def dictlookup(username):
    for item in userList:
        if item['name']==username:
            print("Looked up user " + username)
            return item

def lambda_handler(event, context):
    # Default user name if none passed
    username='Kirk Brady'

    # Test if in Lambda console or API Gateway
    if 'queryStringParameters' in event:    
        if event['queryStringParameters'] is not None:
            if 'name' in event['queryStringParameters']:
                querytest = event['queryStringParameters']['name']
    
                if querytest is not None:
                    username = event['queryStringParameters']['name']
    
    # Find user
    userdata = finduser(username)
    
    # Response
    if userdata is not None:
        return {
            "statusCode": 200,
            "body": json.dumps(userdata)
        }
    else:
        errdata = {
            "Notification": {
                "Type": "Error",
                "Message": "Please check the username"
            }
        }
        return {
            "statusCode": 401,
            "body": json.dumps(errdata)
        }