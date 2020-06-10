"""
Auth0 Authorize Link
The complete documentation for the authorization code flow can be found in Auth0's Documentation. It may help to fill in the url in
the textbox below before copying it into your browser:

https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}

Integrating Auth0 With Your Frontend
To integrate Auth0 with your frontend you simply need to redirect your user to your Auth0 hosted login page and include a url to redirect them to upon completion. This can be done using a simple html anchor link:

<a href="{{AUTH0_AUTHORIZE_URL}}">Login</a>
"""
# Import Python Package
import jwt
import base64
# Init our Data
payload = {'school':'udacity'}
algo = 'HS256' #HMAC-SHA 256
secret = 'learning'
# Encode a JWT
encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)
# Decode a JWT
decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True)
print(decoded_jwt)
# Decode with Simple Base64 Encoding
decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
print(decoded_base64)