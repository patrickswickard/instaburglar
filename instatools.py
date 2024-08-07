"""Tools for reading information about Instagram users and posts"""
import json
import re
import time
import requests
import mysecret

class Instauser:
  """Creates a new object corresponding to a particular Instagram user"""
  def __init__(self):
    self.ai_agent_type = ''
    self.biography = ''
    self.bio_links = []
    self.fb_profile_biolink = ''
    self.blocked_by_viewer = False
    self.restricted_by_viewer = False
    self.country_block = False
    self.eimu_id = ''
    self.external_url = ''
    self.external_url_linkshimmed = ''
    self.followed_by_count = 0
    self.fbid = 0
    self.followed_by_viewer = False
    self.follow_count = 0
    self.follows_viewer = False
    self.full_name = ''
    self.group_metadata = ''
    self.has_ar_effects = False
    self.has_clips = False
    self.has_guides = False
    self.has_channel = False
    self.has_blocked_viewer = False
    self.highlight_reel_count = 0
    self.has_requested_viewer = False
    self.hide_like_and_view_count = False
    self.id = ''
    self.is_business_account = False
    self.is_professional_account = False
    self.is_supervision_enabled = False
    self.is_guardian_of_viewer = False
    self.is_supervised_by_viewer = False
    self.is_supervised_user = False
    self.is_embeds_disabled = False
    self.is_joined_recently = False
    self.guardian_id = ''
    self.business_address_json = ''
    self.business_contact_method = ''
    self.business_phone_number = ''
    self.business_category_name = ''
    self.overall_category_name = ''
    self.category_enum = ''
    self.category_name = ''
    self.is_private = False
    self.is_verified = False
    self.is_verified_by_mv4b = False
    self.is_regulated_c18 = False
    self.mutual_followed_by_count = 0
    self.mutual_followed_by_list = []
    self.pinned_channels_list_count = 0
    self.profile_pic_url = ''
    self.profile_pic_url_hd = ''
    self.requested_by_viewer = False
    self.should_show_category = False
    self.should_show_public_contacts = False
    self.show_account_transparency_details = False
    self.transparency_label = ''
    self.transparency_product = ''
    self.username = ''
    self.connected_fb_page = ''
    self.pronouns = []
    # special
    self.sessionid = Instauser.get_sessionid()
    self.app_id = '936619743392459' # hopefully this is hard-coded, leaving unused method just in case

  def dumph(self):
    """Method which creates a hash from an Instagram user's current attributes"""
    thishash = {}
    thishash['ai_agent_type'] = self.ai_agent_type
    thishash['biography'] = self.biography
    thishash['bio_links'] = self.bio_links
    thishash['fb_profile_biolink'] = self.fb_profile_biolink
    thishash['blocked_by_viewer'] = self.blocked_by_viewer
    thishash['restricted_by_viewer'] = self.restricted_by_viewer
    thishash['country_block'] = self.country_block
    thishash['eimu_id'] = self.eimu_id
    thishash['external_url'] = self.external_url
    thishash['external_url_linkshimmed'] = self.external_url_linkshimmed
    thishash['followed_by_count'] = self.followed_by_count
    thishash['fbid'] = self.fbid
    thishash['followed_by_viewer'] = self.followed_by_viewer
    thishash['follow_count'] = self.follow_count
    thishash['follows_viewer'] = self.follows_viewer
    thishash['full_name'] = self.full_name
    thishash['group_metadata'] = self.group_metadata
    thishash['has_ar_effects'] = self.has_ar_effects
    thishash['has_clips'] = self.has_clips
    thishash['has_guides'] = self.has_guides
    thishash['has_channel'] = self.has_channel
    thishash['has_blocked_viewer'] = self.has_blocked_viewer
    thishash['highlight_reel_count'] = self.highlight_reel_count
    thishash['has_requested_viewer'] = self.has_requested_viewer
    thishash['hide_like_and_view_count'] = self.hide_like_and_view_count
    thishash['id'] = self.id
    thishash['is_business_account'] = self.is_business_account
    thishash['is_professional_account'] = self.is_professional_account
    thishash['is_supervision_enabled'] = self.is_supervision_enabled
    thishash['is_guardian_of_viewer'] = self.is_guardian_of_viewer
    thishash['is_supervised_by_viewer'] = self.is_supervised_by_viewer
    thishash['is_supervised_user'] = self.is_supervised_user
    thishash['is_embeds_disabled'] = self.is_embeds_disabled
    thishash['is_joined_recently'] = self.is_joined_recently
    thishash['guardian_id'] = self.guardian_id
    thishash['business_address_json'] = self.business_address_json
    thishash['business_contact_method'] = self.business_contact_method
    thishash['business_phone_number'] = self.business_phone_number
    thishash['business_category_name'] = self.business_category_name
    thishash['overall_category_name'] = self.overall_category_name
    thishash['category_enum'] = self.category_enum
    thishash['category_name'] = self.category_name
    thishash['is_private'] = self.is_private
    thishash['is_verified'] = self.is_verified
    thishash['is_verified_by_mv4b'] = self.is_verified_by_mv4b
    thishash['is_regulated_c18'] = self.is_regulated_c18
    thishash['mutual_followed_by_count'] = self.mutual_followed_by_count
    thishash['mutual_followed_by_list'] = self.mutual_followed_by_list
    thishash['pinned_channels_list_count'] = self.pinned_channels_list_count
    thishash['profile_pic_url'] = self.profile_pic_url
    thishash['profile_pic_url_hd'] = self.profile_pic_url_hd
    thishash['requested_by_viewer'] = self.requested_by_viewer
    thishash['should_show_category'] = self.should_show_category
    thishash['should_show_public_contacts'] = self.should_show_public_contacts
    thishash['show_account_transparency_details'] = self.show_account_transparency_details
    thishash['transparency_label'] = self.transparency_label
    thishash['transparency_product'] = self.transparency_product
    thishash['username'] = self.username
    thishash['connected_fb_page'] = self.connected_fb_page
    thishash['pronouns'] = self.pronouns
    return thishash

  def dumps(self):
    """Method which creates a json string from a hash based on Instagram user's current attributes"""
    thishash = self.dumph()
    return json.dumps(thishash)

  def reads(self,thisjson):
    """Method which reads in an Instagram user's attributes from a json string in same format created by Instauser.dumps"""
#    thishash = json.loads(thisjson)
#    postobject = self.Instauser()
#    postobject.readh(thishash)
#    return postobject
    thishash = json.loads(thisjson)
    self.readh(thishash)

  def readh(self,thishash):
    """Method which reads in an Instagram user's attributes from a hash in same format created by Instauser.dumph"""
    self.ai_agent_type = thishash['ai_agent_type']
    self.biography = thishash['biography']
    self.bio_links = thishash['bio_links']
    self.fb_profile_biolink = thishash['fb_profile_biolink']
    self.blocked_by_viewer = thishash['blocked_by_viewer']
    self.restricted_by_viewer = thishash['restricted_by_viewer']
    self.country_block = thishash['country_block']
    self.eimu_id = thishash['eimu_id']
    self.external_url = thishash['external_url']
    self.external_url_linkshimmed = thishash['external_url_linkshimmed']
    self.followed_by_count = thishash['followed_by_count']
    self.fbid = thishash['fbid']
    self.followed_by_viewer = thishash['followed_by_viewer']
    self.follow_count = thishash['follow_count']
    self.follows_viewer = thishash['follows_viewer']
    self.full_name = thishash['full_name']
    self.group_metadata = thishash['group_metadata']
    self.has_ar_effects = thishash['has_ar_effects']
    self.has_clips = thishash['has_clips']
    self.has_guides = thishash['has_guides']
    self.has_channel = thishash['has_channel']
    self.has_blocked_viewer = thishash['has_blocked_viewer']
    self.highlight_reel_count = thishash['highlight_reel_count']
    self.has_requested_viewer = thishash['has_requested_viewer']
    self.hide_like_and_view_count = thishash['hide_like_and_view_count']
    self.id = thishash['id']
    self.is_business_account = thishash['is_business_account']
    self.is_professional_account = thishash['is_professional_account']
    self.is_supervision_enabled = thishash['is_supervision_enabled']
    self.is_guardian_of_viewer = thishash['is_guardian_of_viewer']
    self.is_supervised_by_viewer = thishash['is_supervised_by_viewer']
    self.is_supervised_user = thishash['is_supervised_user']
    self.is_embeds_disabled = thishash['is_embeds_disabled']
    self.is_joined_recently = thishash['is_joined_recently']
    self.guardian_id = thishash['guardian_id']
    self.business_address_json = thishash['business_address_json']
    self.business_contact_method = thishash['business_contact_method']
    self.business_phone_number = thishash['business_phone_number']
    self.business_category_name = thishash['business_category_name']
    self.overall_category_name = thishash['overall_category_name']
    self.category_enum = thishash['category_enum']
    self.category_name = thishash['category_name']
    self.is_private = thishash['is_private']
    self.is_verified = thishash['is_verified']
    self.is_verified_by_mv4b = thishash['is_verified_by_mv4b']
    self.is_regulated_c18 = thishash['is_regulated_c18']
    self.mutual_followed_by_count = thishash['mutual_followed_by_count']
    self.mutual_followed_by_list = thishash['mutual_followed_by_list']
    self.pinned_channels_list_count = thishash['pinned_channels_list_count']
    self.profile_pic_url = thishash['profile_pic_url']
    self.profile_pic_url_hd = thishash['profile_pic_url_hd']
    self.requested_by_viewer = thishash['requested_by_viewer']
    self.should_show_category = thishash['should_show_category']
    self.should_show_public_contacts = thishash['should_show_public_contacts']
    self.show_account_transparency_details = thishash['show_account_transparency_details']
    self.transparency_label = thishash['transparency_label']
    self.transparency_product = thishash['transparency_product']
    self.username = thishash['username']
    self.connected_fb_page = thishash['connected_fb_page']
    self.pronouns = thishash['pronouns']

  @staticmethod
  def get_sessionid():
    """Method that reads in a sessionid from mysecret.py .  This could be handled smoother."""
    secret = mysecret.Mysecret()
    sessionid = secret.sid
    return sessionid

  # method to get app id parameter which is probably static but maybe not?
  # in any case it is parsable at least for now
  # if this breaks try hard-coding it
  @staticmethod
  def get_app_id(username):
    """One-off method to read and report the hopefully static app id from Instagram website, this is generally hard-coded elsewhere."""
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/' + username + '/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    responselines = response.text.splitlines()
    app_id = 'UNDEFINED'
    for thisline in responselines:
      hit = re.search(r"APP_ID",thisline)
      if hit:
        jsonthisline = re.findall(r"<script[^>]*>\s*(.*?)\s*</script>",thisline)
        if jsonthisline:
          jsontext = jsonthisline[0]
          # this json is so disorganized it's not even worth parsing
          #thishash = json.loads(jsontext)
          app_id_hits = re.findall(r"\"APP_ID\":\"(.*?)\"",jsontext)
          app_id = app_id_hits[0]
          # returning first we see
          return(app_id)
    # FIXME
    return 'WTF!!!'

  # this method gets the first set of a user's posts
  def get_first_set(self,username):
    """Method to get the first set of a user's posts"""
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/api/v1/users/web_profile_info/?username=' + username
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + self.sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = self.app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    response_hash = json.loads(response.text)
    return response_hash

  # this method gets the first set of posts a user is tagged in
  # note the weird hard-coded doc_id which I am unsure about...
  def get_first_set_tagged(self):
    """Method to get the first set of posts a user is tagged in"""
    doc_id = '17946422347485809'
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables={%22id%22%3A%22' + self.id + '%22%2C%22first%22%3A12}'
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + self.sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = self.app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    response_hash = json.loads(response.text)
    return response_hash

  def get_next_followers(self,count,max_id):
    """Method to get followers of a user beyond the first set"""
    time.sleep(1)
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/api/v1/friendships/' + str(self.id) + '/followers/?count=' + str(count) + '&max_id=' + str(max_id) + '&search_surface=follow_list_page'
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + self.sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = self.app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    response_hash = json.loads(response.text)
    return response_hash

  def get_next_following(self,count,max_id):
    """Method to get Instagram users a user is following beyond the first set"""
    time.sleep(1)
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/api/v1/friendships/' + str(self.id) + '/following/?count=' + str(count) + '&max_id=' + str(max_id) + ''
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + self.sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = self.app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    response_hash = json.loads(response.text)
    return response_hash

  def get_followers_list(self):
    """Method to get a list of Instagram users who follow a particular user"""
    followers_list = []
    count = 100
    max_id = 0
    response_hash = self.get_next_followers(count,max_id)
    nextlist = response_hash['users']
    followers_list += nextlist
    next_max_id = response_hash.get('next_max_id','')
    while next_max_id:
      print('Followers: trying ' + 'next_max_id ' + str(next_max_id))
      response_hash = self.get_next_followers(count,next_max_id)
      nextlist = response_hash['users']
      followers_list += nextlist
      next_max_id = response_hash.get('next_max_id','')
    return followers_list

  def get_following_list(self):
    """Method to get a list of Instagram users who are followed by a particular user"""
    following_list = []
    count = 100
    max_id = 0
    response_hash = self.get_next_following(count,max_id)
    nextlist = response_hash['users']
    following_list += nextlist
    next_max_id = response_hash.get('next_max_id','')
    while next_max_id:
      print('Following: trying ' + 'next_max_id ' + str(next_max_id))
      response_hash = self.get_next_following(count,next_max_id)
      nextlist = response_hash['users']
      following_list += nextlist
      next_max_id = response_hash.get('next_max_id','')
    return following_list

  def get_followers_list_set(self,username):
    """Method to get a set of Instagram users who follow a particular user.  Because of Instagram's flakiness, it retrieves the list of followers three times and aggregates results.  Note this can take some time to complete."""
    followers_set = set()
    followers_lists = []
    for _ in range(3):
      thislist = self.get_followers_list()
      followers_lists.append(thislist)
    for thislist in followers_lists:
      for user in thislist:
        username = user.get('username','')
        #userid = user.get('pk','')
        #full_name = user.get('full_name','')
        #profile_pic_url = user.get('profile_pic_url','')
        #is_private = user.get('is_private',False)
        if username in followers_set:
          pass
        else:
          followers_set.add(username)
    return followers_set

  def get_following_list_set(self,username):
    """Method to get a set of Instagram users who are followed by a particular user.  Because of Instagram's flakiness, it retrieves the list of followers three times and aggregates results.  Note this can take some time to complete."""
    following_set = set()
    following_lists = []
    for _ in range(3):
      thislist = self.get_following_list()
      following_lists.append(thislist)
    for thislist in following_lists:
      for user in thislist:
        username = user.get('username','')
        #userid = user.get('pk','')
        #full_name = user.get('full_name','')
        #profile_pic_url = user.get('profile_pic_url','')
        #is_private = user.get('is_private',False)
        if username in following_set:
          pass
        else:
          following_set.add(username)
    return following_set

  def get_user_from_response_hash(self,response_hash):
    """Method to parse user information from the response hash from an http query to instagram about that user."""
    data = response_hash.get('data')
    if data:
      thisuser = data.get('user')
      if thisuser:
        self.ai_agent_type = thisuser.get('ai_agent_type','')
        self.biography = thisuser.get('biography','')
        self.bio_links = thisuser.get('bio_links',[])
        self.fb_profile_biolink = thisuser.get('fb_profile_biolink','')
        self.blocked_by_viewer = thisuser.get('blocked_by_viewer',False)
        self.restricted_by_viewer = thisuser.get('restricted_by_viewer',False)
        self.country_block = thisuser.get('country_block',False)
        self.eimu_id = thisuser.get('eimu_id','')
        self.external_url = thisuser.get('external_url','')
        self.external_url_linkshimmed = thisuser.get('external_url_linkshimmed','')
        # derived
        followed_by_count = 0
        edge_followed_by = thisuser.get('edge_followed_by',{})
        if edge_followed_by:
          followed_by_count = edge_followed_by.get('count',0)
        self.followed_by_count = followed_by_count
        #######
        self.fbid = thisuser.get('fbid',0)
        self.followed_by_viewer = thisuser.get('followed_by_viewer',False)
        self.follow_count = thisuser.get('follow_count',0)
        # derived
        follow_count = 0
        edge_follow = thisuser.get('edge_follow',{})
        if edge_follow:
          follow_count = edge_follow.get('count',0)
        self.follow_count = follow_count
        self.followed_by_count = followed_by_count
        #######
        self.follows_viewer = thisuser.get('follows_viewer',False)
        self.full_name = thisuser.get('full_name','')
        self.group_metadata = thisuser.get('group_metadata','')
        self.has_ar_effects = thisuser.get('has_ar_effects',False)
        self.has_clips = thisuser.get('has_clips',False)
        self.has_guides = thisuser.get('has_guides',False)
        self.has_channel = thisuser.get('has_channel',False)
        self.has_blocked_viewer = thisuser.get('has_blocked_viewer',False)
        self.highlight_reel_count = thisuser.get('highlight_reel_count',0)
        self.has_requested_viewer = thisuser.get('has_requested_viewer',False)
        self.hide_like_and_view_count = thisuser.get('hide_like_and_view_count',False)
        self.id = thisuser.get('id','')
        self.is_business_account = thisuser.get('is_business_account',False)
        self.is_professional_account = thisuser.get('is_professional_account',False)
        self.is_supervision_enabled = thisuser.get('is_supervision_enabled',False)
        self.is_guardian_of_viewer = thisuser.get('is_guardian_of_viewer',False)
        self.is_supervised_by_viewer = thisuser.get('is_supervised_by_viewer',False)
        self.is_supervised_user = thisuser.get('is_supervised_user',False)
        self.is_embeds_disabled = thisuser.get('is_embeds_disabled',False)
        self.is_joined_recently = thisuser.get('is_joined_recently',False)
        self.guardian_id = thisuser.get('guardian_id','')
        self.business_address_json = thisuser.get('business_address_json','')
        self.business_contact_method = thisuser.get('business_contact_method','')
        self.business_phone_number = thisuser.get('business_phone_number','')
        self.business_category_name = thisuser.get('business_category_name','')
        self.overall_category_name = thisuser.get('overall_category_name','')
        self.category_enum = thisuser.get('category_enum','')
        self.category_name = thisuser.get('category_name','')
        self.is_private = thisuser.get('is_private',False)
        self.is_verified = thisuser.get('is_verified',False)
        self.is_verified_by_mv4b = thisuser.get('is_verified_by_mv4b',False)
        self.is_regulated_c18 = thisuser.get('is_regulated_c18',False)
        # derived
        mutual_followed_by_count = 0
        edge_mutual_followed_by = thisuser.get('mutual_followed_by',{})
        if edge_mutual_followed_by:
          mutual_followed_by_count = edge_mutual_followed_by.get('count',0)
        self.mutual_followed_by_count = mutual_followed_by_count
        #######
        mutual_followed_by_list = []
        edge_mutual_followed_by = thisuser.get('mutual_followed_by',{})
        if edge_mutual_followed_by:
          thisedgelist = edge_mutual_followed_by.get('edges',[])
          mutual_followed_by_list = []
          for thisedge in thisedgelist:
            thisnode = thisedge.get('node','')
            if thisnode:
              mutual_followed_by_list.append(thisnode)
        self.mutual_followed_by_list = mutual_followed_by_list
        #######
        self.pinned_channels_list_count = thisuser.get('pinned_channels_list_count',0)
        self.profile_pic_url = thisuser.get('profile_pic_url','')
        self.profile_pic_url_hd = thisuser.get('profile_pic_url_hd','')
        self.requested_by_viewer = thisuser.get('requested_by_viewer',False)
        self.should_show_category = thisuser.get('should_show_category',False)
        self.should_show_public_contacts = thisuser.get('should_show_public_contacts',False)
        self.show_account_transparency_details = thisuser.get('show_account_transparency_details',False)
        self.transparency_label = thisuser.get('transparency_label','')
        self.transparency_product = thisuser.get('transparency_product','')
        self.username = thisuser.get('username','')
        self.connected_fb_page = thisuser.get('connected_fb_page','')
        self.pronouns = thisuser.get('pronouns',[])

  def get_user_from_web(self,username):
    """Method to perform an http query for an Instagram user and return an Instauser object for that user."""
    response_hash = self.get_first_set(username)
    self.get_user_from_response_hash(response_hash)

  def get_all_data_list(self,username):
    """Method to retrieve all available posts by a particular Instagram user."""
    all_data_list = []
    response_hash = self.get_first_set(username)
    this_list = Instauser.list_data_from_response_hash(response_hash)
    all_data_list = all_data_list + this_list

    # hard-coded, hopefully always the same
    doc_id = '17991233890457762'
    user_id = Instauser.get_user_id_from_response_hash(response_hash)
    num = '50'
    has_next_page = Instauser.get_has_next_page_from_response_hash(response_hash)
    end_cursor = Instauser.get_end_cursor_from_response_hash(response_hash)

#    while end_cursor:
    while has_next_page:
      next_response_hash = self.get_next_response_hash(doc_id,user_id,end_cursor,num)
      this_list = Instauser.list_data_from_response_hash(next_response_hash)
      all_data_list = all_data_list + this_list
      has_next_page = Instauser.get_has_next_page_from_response_hash(next_response_hash)
      end_cursor = Instauser.get_end_cursor_from_response_hash(next_response_hash)
    return all_data_list

  def get_all_data_list_tagged(self):
    """Method to retrieve all available posts in which a particular Instagram user is tagged."""
    all_data_list_tagged = []
    response_hash = self.get_first_set_tagged()
    this_list = Instauser.list_data_from_response_hash_tagged(response_hash)
    all_data_list_tagged = all_data_list_tagged + this_list

    # hard-coded, hopefully always the same
    doc_id = '17946422347485809'
    user_id = self.id
    num = '50'
    end_cursor = Instauser.get_end_cursor_from_response_hash_tagged(response_hash)
    has_next_page = Instauser.get_has_next_page_from_response_hash_tagged(response_hash)
#    while end_cursor:
    while has_next_page:
      next_response_hash = self.get_next_response_hash_tagged(doc_id,user_id,end_cursor,num)
      this_list = Instauser.list_data_from_response_hash_tagged(next_response_hash)
      all_data_list_tagged = all_data_list_tagged + this_list
      end_cursor = Instauser.get_end_cursor_from_response_hash_tagged(next_response_hash)
      has_next_page = Instauser.get_has_next_page_from_response_hash_tagged(next_response_hash)
    return all_data_list_tagged

  @staticmethod
  def list_data_from_response_hash(response_hash):
    """Utility method to parse all post data from a query listing a user's posts."""
    batch_list = []
    data = response_hash['data']
    user = data['user']
    edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
    edges = edge_owner_to_timeline_media['edges']
    for thisedge in edges:
      node = thisedge['node']
      post_object = Instapost()
      post_object.process_post(node)
      if post_object.sidecar_to_children_list:
        for my_post_object in post_object.sidecar_to_children_list:
          batch_list.append(my_post_object.dumph())
      else:
        batch_list.append(post_object.dumph())
    return batch_list

  @staticmethod
  def list_data_from_response_hash_tagged(response_hash):
    """Utility method to parse all post data from a query listing the posts a user is tagged in."""
    batch_list = []
    data = response_hash['data']
    user = data['user']
    edge_owner_to_timeline_media = user['edge_user_to_photos_of_you']
    edges = edge_owner_to_timeline_media['edges']
    for thisedge in edges:
      node = thisedge['node']
      post_object = Instapost()
      post_object.process_post(node)
      if post_object.sidecar_to_children_list:
        for my_post_object in post_object.sidecar_to_children_list:
          batch_list.append(my_post_object.dumph())
      else:
        batch_list.append(post_object.dumph())
    return batch_list

  @staticmethod
  def get_user_id_from_response_hash(response_hash):
    """Utility method to parse a user's user_id from a response hash."""
    data = response_hash['data']
    user = data['user']
    user_id = user['id']
    return user_id

  @staticmethod
  def get_has_next_page_from_response_hash(response_hash):
    """Utility method to parse has_next_page from a response hash."""
    data = response_hash['data']
    user = data['user']
    edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
    page_info = edge_owner_to_timeline_media['page_info']
    has_next_page = page_info['has_next_page']
    return has_next_page

  @staticmethod
  def get_end_cursor_from_response_hash(response_hash):
    """Utility method to parse the end cursor from a response hash to get to next page of results of a user's posts."""
    data = response_hash['data']
    user = data['user']
    edge_owner_to_timeline_media = user['edge_owner_to_timeline_media']
    page_info = edge_owner_to_timeline_media['page_info']
    has_next_page = page_info['has_next_page']
    end_cursor = ''
    if has_next_page:
      end_cursor = page_info['end_cursor']
    return end_cursor

  @staticmethod
  def get_has_next_page_from_response_hash_tagged(response_hash):
    """Utility method to parse has_next_page from a response hash to get to next page of results a user is tagged in."""
    data = response_hash['data']
    user = data['user']
    edge_owner_to_timeline_media = user['edge_user_to_photos_of_you']
    page_info = edge_owner_to_timeline_media['page_info']
    has_next_page = page_info['has_next_page']
    return has_next_page

  @staticmethod
  def get_end_cursor_from_response_hash_tagged(response_hash):
    """Utility method to parse the end cursor from a response hash to get to next page of results a user is tagged in."""
    data = response_hash['data']
    user = data['user']
    edge_owner_to_timeline_media = user['edge_user_to_photos_of_you']
    page_info = edge_owner_to_timeline_media['page_info']
    has_next_page = page_info['has_next_page']
    end_cursor = ''
    if has_next_page:
      end_cursor = page_info['end_cursor']
    return end_cursor

  def get_next_response_hash(self,doc_id,user_id,end_cursor,num):
    """Utility method to fetch next page of results of a user's posts."""
    # note that end_cursor may be empty string
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables=%7B%22id%22%3A%22' + user_id + '%22%2C%22after%22%3A%22' + end_cursor + '%22%2C%22first%22%3A' + num + '%7D'
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + self.sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = self.app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    response_hash = json.loads(response.text)
    outfilename = 'NEXTSET.json'
    with open(outfilename,'w',encoding="utf-8") as thisoutfile:
      thisoutfile.write(response.text)
    return response_hash

  def get_next_response_hash_tagged(self,doc_id,user_id,end_cursor,num):
    """Utility method to fetch next page of results of posts a user is tagged in."""
    # note that end_cursor may be empty string though never seen it for tagged in posts...
    debug = False
    if not debug:
      proxies = {}
      verify = True
    else:
      proxies = {
        'http' : 'http://localhost:8888',
        'https' : 'http://localhost:8888',
      }
      verify = False
    request_url = 'https://www.instagram.com/graphql/query/?doc_id=' + doc_id + '&variables=%7B%22id%22%3A%22' + user_id + '%22%2C%22after%22%3A%22' + end_cursor + '%22%2C%22first%22%3A' + num + '%7D'
    header_hash = {
    }
    header_hash['Cookie'] = 'sessionid=' + self.sessionid + '; ds_user_id=CAFE'
    header_hash['x-ig-app-id'] = self.app_id
    headers = header_hash
    response = requests.get(request_url, headers=headers, proxies=proxies, verify=verify)
    response_hash = json.loads(response.text)
    outfilename = 'NEXTSET.json'
    with open(outfilename,'w',encoding="utf-8") as thisoutfile:
      thisoutfile.write(response.text)
    return response_hash

class Instapost:
  """Creates an object corresponding to a particular Instagram post"""
  def __init__(self):
    self.id = ''
    self.shortcode = ''
    self.width = 0
    self.height = 0
    self.display_url = ''
    self.tagged_user_list = []
    self.fact_check_overall_rating = ''
    self.fact_check_information = ''
    self.gating_info = ''
    self.sharing_friction_info = ''
    self.media_overlay_info = ''
    self.media_preview = ''
    self.userid = ''
    self.username = ''
    self.is_video = False
    self.has_upcoming_event = False
    self.accessibility_caption = ''
    self.tagged_user_list = []
    self.caption = ''
##############################################################################
    self.number_of_comments = ''
    self.comments_disabled = False
    self.timestamp = 0
    self.number_of_likes = ''
##############################################################################
    self.location = ''
    self.sidecar_to_children_list = []
    # special
    self.sessionid = Instapost.get_sessionid()
    self.app_id = '936619743392459' # hopefully this is hard-coded, leaving unused method just in case

  @staticmethod
  def get_sessionid():
    """Utility method to get the session id from mysecret.py"""
    secret = mysecret.Mysecret()
    sessionid = secret.sid
    return sessionid

  def get_common_values(self,thisnode):
    """Utility method to get values that may vary over various images attached to a particular Instagram post"""
    self.id = thisnode.get('id','')
    self.shortcode = thisnode.get('shortcode','')
    #subfields
    height = ''
    width = ''
    dimensions = thisnode.get('dimensions',{})
    if dimensions:
      width = dimensions.get('width','')
      height = dimensions.get('height','')
    self.width = width
    self.height = height
    self.display_url = thisnode.get('display_url','')
    self.tagged_user_list = thisnode.get('edge_media_to_tagged_user',[])
    self.fact_check_overall_rating = thisnode.get('fact_check_overall_rating','')
    self.fact_check_information = thisnode.get('fact_check_information','')
    self.gating_info = thisnode.get('gating_info','')
    self.sharing_friction_info = thisnode.get('sharing_friction_info','')
    self.media_overlay_info = thisnode.get('media_overlay_info','')
    self.media_preview = thisnode.get('media_preview','')
    # subfields
    userid = ''
    username = ''
    owner = thisnode.get('owner',{})
    if owner:
      userid = owner.get('id','')
      username = owner.get('username','')
    self.userid = userid
    self.username = username
    self.is_video = thisnode.get('is_video',False)
    self.has_upcoming_event = thisnode.get('has_upcoming_event',False)
    self.accessibility_caption = thisnode.get('accessibility_caption','')

  def process_post(self,thisnode):
    """Process all metadata from a particular node/post"""
    self.get_common_values(thisnode)
    # after this point everything is attached only to the main post
    caption = ''
    if thisnode.get('edge_media_to_caption',''):
      captionlist = thisnode['edge_media_to_caption']['edges']
      if captionlist:
        caption = captionlist[0]
    self.caption = caption
##############################################################################
    number_of_comments = 0
    if thisnode.get('edge_media_to_comment',{}):
      if thisnode['edge_media_to_comment'].get('count',0):
        number_of_comments = thisnode['edge_media_to_comment']['count']
    self.number_of_comments = number_of_comments
    self.comments_disabled = thisnode.get('comments_disabled', False)
    self.timestamp = thisnode.get('taken_at_timestamp',0)
    number_of_likes = ''
    if thisnode.get('edge_media_preview_like',{}):
      if thisnode['edge_media_preview_like'].get('count',0):
        number_of_likes = thisnode['edge_media_preview_like']['count']
    self.number_of_likes = number_of_likes
##############################################################################
    self.location = thisnode.get('location','')
    # after this point these values only exist if we have subposts
    my_sidecar_to_children_list = []
    sidecar_to_children = thisnode.get('edge_sidecar_to_children',{})
    if sidecar_to_children:
      sidecar_to_children_list = sidecar_to_children.get('edges',[])
      if sidecar_to_children_list:
        for childthing in sidecar_to_children_list:
          thissubnode = childthing.get('node',{})
          if thissubnode:
            # create new post object
            mysubpost = Instapost()
            # grab the stuff only attached to main
            mysubpost.caption = self.caption
            mysubpost.location = self.location
            mysubpost.get_common_values(thissubnode)
            my_sidecar_to_children_list.append(mysubpost)
    self.sidecar_to_children_list = my_sidecar_to_children_list

  def dumph(self):
    """Method to convert post attributes to a hash"""
    posthash = {}
    posthash['id'] = self.id
    posthash['shortcode'] = self.shortcode
    posthash['width'] = self.width
    posthash['height'] = self.height
    posthash['display_url'] = self.display_url
    posthash['tagged_user_list'] = self.tagged_user_list
    posthash['fact_check_overall_rating'] = self.fact_check_overall_rating
    posthash['fact_check_information'] = self.fact_check_information
    posthash['gating_info'] = self.gating_info
    posthash['sharing_friction_info'] = self.sharing_friction_info
    posthash['media_overlay_info'] = self.media_overlay_info
    posthash['media_preview'] = self.media_preview
    posthash['userid'] = self.userid
    posthash['username'] = self.username
    posthash['is_video'] = self.is_video
    posthash['has_upcoming_event'] = self.has_upcoming_event
    posthash['accessibility_caption'] = self.accessibility_caption
    posthash['tagged_user_list'] = self.tagged_user_list
    posthash['caption'] = self.caption
##############################################################################
    posthash['number_of_comments'] = self.number_of_comments
    posthash['comments_disabled'] = self.comments_disabled
    posthash['timestamp'] = self.timestamp
    posthash['number_of_likes'] = self.number_of_likes
##############################################################################
    posthash['location'] = self.location
    sidecar_to_children_list_data = []
    for this_child in self.sidecar_to_children_list:
      thishash = this_child.dumph()
      sidecar_to_children_list_data.append(thishash)
    posthash['sidecar_to_children_list'] = sidecar_to_children_list_data
    return posthash

  def dumps(self):
    """Method to convert post attributes to a json string for easy storage"""
    thishash = self.dumph()
    return json.dumps(thishash)

  # TODO this is WRONG
  def reads(self,thisjson):
    """Method to read in post attributes from a json string and create a post object"""
    #thishash = json.loads(thisjson)
    #postobject = self.Instapost()
    #postobject.readh(thishash)
    #return postobject
    thishash = json.loads(thisjson)
    self.readh(thishash)

  def readh(self,posthash):
    """Method to read in post attributes from a json string and create a hash corresponding to those"""
    self.id = posthash['id']
    self.shortcode = posthash['shortcode']
    self.width = posthash['width']
    self.height = posthash['height']
    self.display_url = posthash['display_url']
    self.tagged_user_list = posthash['tagged_user_list']
    self.fact_check_overall_rating = posthash['fact_check_overall_rating']
    self.fact_check_information = posthash['fact_check_information']
    self.gating_info = posthash['gating_info']
    self.sharing_friction_info =  posthash['sharing_friction_info']
    self.media_overlay_info = posthash['media_overlay_info']
    self.media_preview = posthash['media_preview']
    self.userid = posthash['userid']
    self.username = posthash['username']
    self.is_video = posthash['is_video']
    self.has_upcoming_event = posthash['has_upcoming_event']
    self.accessibility_caption = posthash['accessibility_caption']
    self.tagged_user_list = posthash['tagged_user_list']
    self.caption = posthash['caption']
##############################################################################
    self.number_of_comments = posthash['number_of_comments']
    self.comments_disabled = posthash['comments_disabled']
    self.timestamp = posthash['timestamp']
    self.number_of_likes = posthash['number_of_likes']
##############################################################################
    self.location = posthash['location']
    sidecar_to_children_list_posts = []
    for this_child in posthash['sidecar_to_children_list']:
      thispost = this_child.readh()
      sidecar_to_children_list_posts.append(thispost)
    self.sidecar_to_children_list = posthash['sidecar_to_children_list']
