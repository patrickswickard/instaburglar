"""Test functionality to get app id"""
import instatools

USERNAME = 'USERNAME'

my_user = instatools.Instauser()
my_user_appid = my_user.get_app_id(USERNAME)
print('app id is ' + my_user_appid)
#################
print('one more time...')
my_user_appid2 = instatools.Instauser.get_app_id(USERNAME)
print('app id 2 is ' + my_user_appid2)
