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
#my_user.get_user_from_web(username)
my_user_appid = my_user.get_app_id(username)
print('app id is ' + my_user_appid)
