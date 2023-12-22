"""Test functionality of getting all posts a user is tagged in."""
import instatools

USERNAME = 'corvid_phalanges'

my_user = instatools.Instauser()
my_user.get_user_from_web(USERNAME)
my_user_appid = my_user.get_app_id(USERNAME)
my_user.get_user_from_web(USERNAME)
response = my_user.get_first_set_tagged()
all_data_list_tagged = my_user.get_all_data_list_tagged()
print(all_data_list_tagged)
