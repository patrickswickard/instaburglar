"""Testing get user from web functionality"""
import instatools

USERNAME = 'bugbobbie'

my_user = instatools.Instauser()
my_user.get_user_from_web(USERNAME)

print(my_user.dumps())
