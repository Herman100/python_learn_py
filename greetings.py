def greetingUser(username):
    print(f"\nHello {username}, welcome back!")


user = input("Enter your name: ").strip().split()[0]
greetingUser(user)
