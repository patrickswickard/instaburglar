"""Test get all posts"""
import json
import instatools

USERNAME = 'drought_season'

my_user = instatools.Instauser()
my_user.get_user_from_web(USERNAME)

all_data_list = my_user.get_all_data_list(USERNAME)

print(json.dumps(all_data_list))
OUTFILENAME = USERNAME + '_all_data_list.json'
with open(OUTFILENAME,'w',encoding="utf-8") as thisoutfile:
  thisoutfile.write(json.dumps(all_data_list))
