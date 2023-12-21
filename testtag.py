import instatools
import json

username = 'drought_season'

my_user = instatools.Instauser()
my_user.get_user_from_web(username)
my_user_appid = my_user.get_app_id(username)
my_user.get_user_from_web(username)
response = my_user.get_first_set_tagged()
all_data_list_tagged = my_user.get_all_data_list_tagged()
print(all_data_list_tagged)
