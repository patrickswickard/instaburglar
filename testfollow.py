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
#username = 'dont_fear_the_millimeter'

secret = mysecret.Mysecret()
sessionid = secret.sid

my_user = instatools.Instauser()
my_user.get_user_from_web(username,sessionid)
my_user_appid = my_user.get_app_id(username)
my_user_followers_response = my_user.get_followers_list_set(username,my_user_appid,sessionid,12,0)
my_user_following_response = my_user.get_following_list_set(username,my_user_appid,sessionid,12,0)
my_user_followers_more_response = my_user.get_next_followers(username,my_user_appid,sessionid,100,300)
my_user_following_more_response = my_user.get_next_following(username,my_user_appid,sessionid,100,100)

all_data_list = my_user.get_all_data_list(username, sessionid)

#print(json.dumps(all_data_list))
outfilename = 'all_data_list.json'
thisoutfile = open(outfilename, 'w')
thisoutfile.write(json.dumps(all_data_list))

#for entry in all_data_list:
#  print('******************************************************')
#  print('******************************************************')
#  print(entry['display_url'])


#myprintoutput = my_user_followers_response
myprintoutput = my_user_following_response
#myprintoutput = my_user_followers_more_response
#myprintoutput = my_user_following_more_response

#print(json.dumps(my_user_followers_response))
#print(json.dumps(my_user_following_response))
#print(json.dumps(my_user_followers_more_response))
#print(json.dumps(my_user_following_more_response))
print(myprintoutput)

#mylist = json.loads(myprintoutput)
#mylist = myprintoutput['users']
mylist = myprintoutput
#next_max_id = myprintoutput.get('next_max_id','')
#next_max_id = 37
print(str(len(mylist)))

print(my_user.id)
#print('NMI:' + str(next_max_id))

for user in mylist:
  print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
