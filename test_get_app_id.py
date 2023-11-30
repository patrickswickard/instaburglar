import instatools

username = 'drought_season'

my_user = instatools.Instauser()
my_user_appid = my_user.get_app_id(username)
print('app id is ' + my_user_appid)
