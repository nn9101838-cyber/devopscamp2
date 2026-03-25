print("Welcome to DevOps Camp 2 Project!")

def calculate_square(n):
    return n * n

def send_notification(message):
    print(f"Notification Sent: {message}")
    return True

if __name__ == "__main__":
    print(f"Square of 5 is {calculate_square(5)}")
    send_notification("Welcome to DevOps!")
