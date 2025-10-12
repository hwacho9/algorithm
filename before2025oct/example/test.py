#
def user_register():
    name = input("Enter your name: ")
    with open("userlist.txt", "a") as f:
        f.write(name + "\n")
    print(f"{name} registered successfully.")




def format_welcome_message(name: str) -> str:
    return f"{name} registered successfully."


def save_user(name: str, path: str):
    with open(path, "a") as f:
        f.write(name + "\n")


# actual usage (UI/input/output logic is only here)
def main():
    name = input("Enter your name: ")
    save_user(name, "userlist.txt")
    print(format_welcome_message(name))
