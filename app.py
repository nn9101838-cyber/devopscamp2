print("Welcome to DevOps Camp 2 Project!")

def calculate_square(n):
    return n * n

tasks = []

def add_task(task):
    tasks.append(task)
    return tasks

if __name__ == "__main__":
    print(f"Square of 5 is {calculate_square(5)}")
    print(f"Tasks: {add_task('Learn Git Branching')}")
