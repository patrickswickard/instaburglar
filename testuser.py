import instatools

username = 'bugbobbie'

my_user = instatools.Instauser()
my_user.get_user_from_web(username)

print(my_user.dumps())
