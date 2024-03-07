## Cookies
A cookies is stored on client's computer as a text file. Cookies present on the Client-side tracks and remember the user's information

Request object contains cookies attributes. It is a dictionary-like object that contains all the cookies that are present in the request. The cookies attribute is an instance of the SimpleCookie class. This class is used to manipulate the cookies.

HTTP is a stateless protocol, which means that the server can not distinguish whether a user is visiting the site for the first time or is a returning user. Cookies are used to solve this problem. Cookies are used to store the user's information on the client's computer. This information can be used to track the user's activity, remember the user's information, and store the user's preferences.

## Example: Setting uuid to identify subsequent visits 

```python
from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    # Check if the client has a "unique_id" cookie
    unique_id = request.cookies.get('unique_id')
    if unique_id:
        return 'Welcome back! Your unique id is ' + unique_id
    else:
        # Generate a unique id
        new_unique_id = str(uuid.uuid4())
        # Create a response and set a "unique_id" cookie
        response = make_response(f'Hello, your unique id is {new_unique_id}')
        response.set_cookie('unique_id', new_unique_id)
        return response

if __name__ == '__main__':
    app.run(debug=True)
```

## Session
Session is a time interval. In web development, a session is the time interval between the user logging into the system and logging out of the system. The session data is stored on the server. The session data is used to store the user's information, track the user's activity, and store the user's preferences.

Each client is assigned a unique session id. The session id is stored in a cookie on the client's computer. The session id is used to identify the client's session data on the server.

Session data is stored on top of cookies and server signs them cryptographically. This makes it difficult for the client to tamper with the session data.

## Example with Flask
```python
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

# To set a secret key for the session
app.secret_key = 'key'

# To set a session variable


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

# To login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
    </form>
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

```

## Session storage Use case
- Password Reset and Recovery
- User Sessions and Permissions
- Multi-Step Forms
- Security Tokens
- Shopping Cart

## JSON Web Tokens (JWT)
JSON Web Tokens (JWT) is a secure and compact way to transmit data between two parties with the help of a digital signature. It is used to securely transmit information between the client and the server. JWT is used to authenticate the user and to transmit the user's information securely.

## How do JSON Web Tokens (JWT) work?
When a user logs in, the server creates a JWT and sends it to the client. The client stores the JWT and sends it with every request. The server verifies the JWT and sends the response.

Whenever the user wants to access a protected route or resource, the user agent should send the JWT, typically in the Authorization header using the Bearer schema. The content of the header should look like the following:

```
Authorization : Bearer <token>
    - Bearer authentication is a security scheme that is used to authenticate the user.
    
```

