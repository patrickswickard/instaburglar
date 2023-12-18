import base64
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_v1_5
import datetime
import struct
import requests

from Cryptodome.PublicKey import RSA

def main():
    print(encpass())

def encpass():
    password = "TESTPASSWORD"
    publickeyid, publickey = get_publickey_details("", "")
    session_key = get_random_bytes(32)
    iv = bytearray(12)
    time = str(int(datetime.datetime.now().timestamp()))
    decoded_publickey = base64.b64decode(publickey.encode())
    recipient_key = RSA.import_key(decoded_publickey)
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
    cipher_aes.update(time.encode())
    ciphertext, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
    payload = base64.b64encode((b"\x01\x00" + publickeyid.to_bytes(2, byteorder='big') + iv + len(enc_session_key).to_bytes(2, byteorder='big') + enc_session_key + tag + ciphertext))
    return f"#PWD_INSTAGRAM:4:{time}:{payload.decode()}"

def get_publickey_details(publickeyid, publickey):
    r = requests.get('https://i.instagram.com/api/v1/qe/sync/')
    publickeyid = int(r.headers['ig-set-password-encryption-key-id'])
    publickey = r.headers['ig-set-password-encryption-pub-key']
    return (publickeyid, publickey)



# method to get app id parameter which is probably static but maybe not?

# in any case it is parsable at least for now
# if this breaks try hard-coding it
def get_app_id(self,username):
  """One-off method to read and report the hopefully static app id from Instagram website, this is generally hard-coded elsewhere."""
  debug = true
  request_url = 'https://www.instagram.com/' + username + '/'
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0'}
  if not debug:
    proxies = {}
  else:
    proxies = {
      'http' : 'http://localhost:8888',
      'https' : 'http://localhost:8888',
    }
  response = requests.get(request_url, headers=headers, proxies=proxies, verify=False)
  raw_html = response.text
  responselines = response.text.splitlines()
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
        return app_id

print(encpass())
