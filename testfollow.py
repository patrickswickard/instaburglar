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

secret = mysecret.Mysecret()
sessionid = secret.sid

my_user = instatools.Instauser()
my_user.get_user_from_web(username,sessionid)
my_user_appid = my_user.get_app_id(username)
# instagram gives a lot of duplicates for some reason doing this
# but running the search three times and eliminating dupes with
# set logic gives reasonably complete results
# note they will cut you off if you do this too often
my_user_followers1 = my_user.get_followers_list_set(username,my_user_appid,sessionid,12,0)
my_user_followers2 = my_user.get_followers_list_set(username,my_user_appid,sessionid,12,0)
my_user_followers3 = my_user.get_followers_list_set(username,my_user_appid,sessionid,12,0)
my_user_following1 = my_user.get_following_list_set(username,my_user_appid,sessionid,12,0)
my_user_following2 = my_user.get_following_list_set(username,my_user_appid,sessionid,12,0)
my_user_following3 = my_user.get_following_list_set(username,my_user_appid,sessionid,12,0)

print()

my_user_followers_set = set()
my_user_following_set = set()

count1 = 0
count1hash = {}
for user in my_user_followers1:
  count1 += 1
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)
  if username in my_user_followers_set:
    print('DUPE: ' + username)
  else:
    my_user_followers_set.add(username)
#  print(str(count1) + ' - ' + username)
for user in my_user_followers2:
  count1 += 1
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)
  if username in my_user_followers_set:
    print('DUPE: ' + username)
  else:
    my_user_followers_set.add(username)
#  print(str(count1) + ' - ' + username)
for user in my_user_followers3:
  count1 += 1
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)
  if username in my_user_followers_set:
    print('DUPE: ' + username)
  else:
    my_user_followers_set.add(username)
#  print(str(count1) + ' - ' + username)

count2 = 0
count2hash = {}
for user in my_user_following1:
  count2 += 1
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)
  if username in my_user_following_set:
    print('DUPE: ' + username)
  else:
    my_user_following_set.add(username)
#  print(str(count2) + ' - ' + username)
for user in my_user_following2:
  count2 += 1
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)
  if username in my_user_following_set:
    print('DUPE: ' + username)
  else:
    my_user_following_set.add(username)
#  print(str(count2) + ' - ' + username)
for user in my_user_following3:
  count2 += 1
  #print(user.get('username','') + ' ' + '(' + user.get('full_name','') + ')')
  username = user.get('username','')
  userid = user.get('pk','')
  full_name = user.get('full_name','')
  profile_pic_url = user.get('profile_pic_url','')
  is_private = user.get('is_private',False)
  if username in my_user_following_set:
    print('DUPE: ' + username)
  else:
    my_user_following_set.add(username)
#  print(str(count2) + ' - ' + username)

print(len(my_user_followers1))
print(len(my_user_following1))
print(len(my_user_followers2))
print(len(my_user_following2))

#print('*********************')
#print(my_user_followers_set)
#print('*********************')
#print(my_user_following_set)
#print('*********************')

print('mutuals:')
my_user_mutuals = my_user_followers_set.intersection(my_user_following_set)
#print(my_user_mutuals)
print(len(my_user_mutuals))
print('**********************')
print('Following not follower:')
my_user_following_not_followers = my_user_following_set.difference(my_user_followers_set)
print(len(my_user_following_not_followers))
print('**********************')
print('Follower not following:')
my_user_followers_not_following = my_user_followers_set.difference(my_user_following_set)
print(len(my_user_followers_not_following))
print('**********************')
print('union followers and following:')
my_user_union = my_user_following_set.union(my_user_followers_set)
print(len(my_user_union))
print('**********************')
print('Followers:')
print(len(my_user_followers_set))
print(len(my_user_followers1))
print(len(my_user_followers2))
print('Following:')
print(len(my_user_following_set))
print(len(my_user_following1))
print(len(my_user_following2))

print(my_user_union)
