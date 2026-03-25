print("Welcome to DevOps Camp 2 Project!")

def calculate_square(n):
    return n * n

def login(username, password):
    if username == "admin" and password == "secret":
        return True
    return False

if __name__ == "__main__":
    print(f"Square of 5 is {calculate_square(5)}")
    print(f"Login result: {login('admin', 'secret')}")
