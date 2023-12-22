"""Sample code to download a single photo"""
import shutil
import requests

MY_SOURCE = 'https://www.fakeurl.com/thisphoto.jpg'

MY_FILENAME = 'thumbnail.jpg'

# method to download a single photo, takes url as source and dl target as filename
def download_single_photo(source,filename):
  """Download photo with url source and download to target filename"""
  url_response = requests.get(source, stream=True)
  with open(filename, 'wb') as out_file:
    shutil.copyfileobj(url_response.raw, out_file)

download_single_photo(MY_SOURCE, MY_FILENAME)
