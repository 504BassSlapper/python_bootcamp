class User:

    def __init__(self, user_id, username):
        print("init new user")
        self.id = user_id
        self.username = username
        self.followers = 0
        pass


user_1 = User("0001", "Balotelli")
user_2 = User("0002", "Messi")
# user_1.id = "0001"
# user_1.username = "Balotelli"

print(user_1.username)
print(user_2.username)
