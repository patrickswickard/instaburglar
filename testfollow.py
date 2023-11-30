import instatools
import json

username = 'drought_season'

#secret = mysecret.Mysecret()
#sessionid = secret.sid

my_user = instatools.Instauser()
my_user.get_user_from_web(username)
my_user_followers_set = my_user.get_followers_list_set(username)
my_user_following_set = my_user.get_following_list_set(username)

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
print('Following:')
print(len(my_user_following_set))

print('List of all followers and following:')
print(my_user_union)
