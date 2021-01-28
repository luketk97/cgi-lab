#!/usr/bin/env python3
import cgi, cgitb
import os 
import json
from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie

cgitb.enable()

'''
print("Content-Type: text/plain")
print()
print(os.environ)
'''
'''
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))
'''
'''
print("Content-Type: text/html")
print()
print(templates.login_page())
'''

s = cgi.FieldStorage()

username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None

if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_username = c.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.password

if cookie_ok:
    username = c_username
    password = c_password

print("Content-Type: text/html")
if form_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())