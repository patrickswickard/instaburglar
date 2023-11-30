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

# method to download a single photo, takes url as source and dl target as filename
def download_single_photo(source,filename):
  source = source
  photo_filename = filename
  url_response = requests.get(source, stream=True)
  with open(photo_filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

my_user = instatools.Instauser()
my_user.get_user_from_web(username)

all_data_list = my_user.get_all_data_list(username)

print(json.dumps(all_data_list))
outfilename = username + '_all_data_list.json'
thisoutfile = open(outfilename, 'w')
thisoutfile.write(json.dumps(all_data_list))

for entry in all_data_list:
  print('******************************************************')
  print('******************************************************')
  print(entry['display_url'])
