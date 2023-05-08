import httpx

# Set the OAuth2 endpoint URL
auth_url = 'https://example.com/oauth2/token'

# Set the client ID and secret
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set the username and password
username = 'your_username'
password = 'your_password'

# Set the grant type
grant_type = 'password'

# Create the request payload
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password,
    'grant_type': grant_type
}

# Send the authentication request
with httpx.Client() as client:
    response = client.post(auth_url, data=payload)

# Check if the response is successful
if response.status_code == httpx.codes.OK:
    # Get the access token
    access_token = response.json()['access_token']
    print('Access Token:', access_token)
else:
    # Handle the error
    print('Authentication failed:', response.text)
