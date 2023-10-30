import re

file = 'allurls3.txt'
with open(file) as fd:
  lines = fd.read().splitlines()

count = 0
for line in lines:
  hit = re.findall(r"\?stp=dst-jpg_e35&",line)
  if hit:
    count += 1
    print("<a href=\"" + line + "\">LINK " + str(count) + "</a><br>")


