import requests
import re
import json
import shutil
import mysecret
import time
import instatools

#username = 'vintage_bmore_graffiti'
#username = 'cannibal_corpse_limericks'
username = 'bugbobbie'
#username = 'brewersart'
#username = 'dont_fear_the_millimeter'

secret = mysecret.Mysecret()
sessionid = secret.sid

my_user = instatools.Instauser()
my_user.get_user_from_web(username,sessionid)
my_user_appid = my_user.get_app_id(username)
my_user_followers = my_user.get_followers_list_set(username,my_user_appid,sessionid,12,0)
my_user_following = my_user.get_following_list_set(username,my_user_appid,sessionid,12,0)

print()

for user in my_user_followers:
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)

for user in my_user_following:
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)

print(len(my_user_followers))
print(len(my_user_following))

