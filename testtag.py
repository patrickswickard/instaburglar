import requests
import re
import json
import shutil
import mysecret
import time
import instatools

username = 'drought_season'

secret = mysecret.Mysecret()
sessionid = secret.sid

my_user = instatools.Instauser()
my_user.get_user_from_web(username)
my_user_appid = my_user.get_app_id(username)
my_user.get_user_from_web(username)
response = my_user.get_first_set_tagged(username,my_user_appid)
#print(response)
all_data_list_tagged = my_user.get_all_data_list_tagged(username)

