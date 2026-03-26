import os
import sys
import datetime
import socket
import getpass

def main():
    print("---- SYSTEM INFO ----")
    
    # 1. Display current date & time
    now = datetime.datetime.now()
    print(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M')}")
    
    # 2. Show system hostname
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")
    
    # 3. Print Python version
    print(f"Python Version: {sys.version.split()[0]}")
    
    # 4. Show list of files in current directory
    print("Files in Directory:")
    try:
        files = os.listdir('.')
        for f in files:
            print(f"- {f}")
    except Exception as e:
        files = []
        print(f"Could not list files: {e}")
        
    # 5. Count number of files in directory
    file_count = len([f for f in files if os.path.isfile(os.path.join('.', f))])
    print(f"Number of Files: {file_count}")
    
    # 6. Show current user
    try:
        current_user = getpass.getuser()
    except Exception:
        current_user = os.environ.get('USER', 'unknown')
        
    print(f"Current User: {current_user}")
    
    # 7. Accept user input
    user_input = input("Enter any text to confirm: ")
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    main()
