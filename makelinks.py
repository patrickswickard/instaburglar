import re

for i in range(11,70):
  infilename = 'allurls' + str(i) + '.txt'
  outfilename = 'spit_url' + str(i) + '.html'
  with open(infilename) as fd:
    thisoutfile = open(outfilename, 'w')
    lines = fd.read().splitlines()
    count = 0
    for line in lines:
      hit = re.findall(r"\?stp=dst-jpg_e35&",line)
      if hit:
        count += 1
        print("<a href=\"" + line + "\">LINK " + str(count) + "</a><br>")
        thisoutfile.write("<a href=\"" + line + "\">LINK " + str(count) + "</a><br>\n")


