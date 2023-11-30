import instatools
import json

username = 'corvid_phalanges'

my_user = instatools.Instauser()
my_user.get_user_from_web(username)

all_data_list = my_user.get_all_data_list(username)

print(json.dumps(all_data_list))
outfilename = username + '_all_data_list.json'
thisoutfile = open(outfilename, 'w')
thisoutfile.write(json.dumps(all_data_list))
