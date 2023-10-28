import re

file = 'instapost3.txt'
with open(file) as fd:
  lines = fd.read().splitlines()

# find and report
for thisline in lines:
  branch = re.findall(r"\"http[^\"]*\",\s+\"(?:width|height)\"",thisline)
  branch = re.findall(r"\"(http[^\"]*)\",\s*\"(?:width|height)\"",thisline)
  if branch:
#    print(branch.group(1))
    for url in branch:
      newurl = re.sub(r"\\/","/",url)
      print(newurl)


# find and report
for thisline in lines:
  newline = re.sub(r"\W","",thisline)
#  print(newline)
