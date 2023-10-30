import re

for i in range(11,70):
  filename = 'instapost' + str(i) + '.txt'
  outfilename = 'allurls' + str(i) + '.txt'
  print(filename)
  print(outfilename)

  with open(filename) as fd:
    lines = fd.read().splitlines()
    thisoutfile = open(outfilename, 'w')

  # find and report
  for thisline in lines:
    branch = re.findall(r"\"http[^\"]*\",\s+\"(?:width|height)\"",thisline)
    branch = re.findall(r"\"(http[^\"]*)\",\s*\"(?:width|height)\"",thisline)
    if branch:
  #    print(branch.group(1))
      for url in branch:
        newurl = re.sub(r"\\/","/",url) + "\n"
        print(newurl)
        thisoutfile.write(newurl)

  # find and report
  for thisline in lines:
    newline = re.sub(r"\W","",thisline)
  #  print(newline)
  print(filename)
