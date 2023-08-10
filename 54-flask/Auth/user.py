class User: 
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_auth_decorator(function):
    def wrapper(**kwargs):
        if kwargs.get("user").is_logged_in == True:
            function(kwargs.get("user"))
    return wrapper

@is_auth_decorator
def post_tweet(user):
    print(f"tweet posted by {user.name} ")


tweeter_user = User("NOLAN")
tweeter_user.is_logged_in = True
post_tweet(user = tweeter_user)