usernames = ["admin", "will", "john", "mark", "james"]
for username in usernames:
    if username == "admin":
        print("hello admin. do you want a status report?")    
    else:
        print(f"hello {username} thanks for logging in.")

usernames = []
if usernames:
    for username in usernames:
        print(f"hello {username}")
else:
    print("we need to find more users.")


