print("Student Registration Module-login feature")
def login(username,password):
    if username=="admin"and password=="1234":
        print("Login successful")
    else:
        print("Login Failed")
login("admin","1234")