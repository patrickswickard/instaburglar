import json
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


json_file = open('all_data_list.json', 'r')
json_hash = json.load(json_file)
json_file.close()

post_list = json_hash

all_caption_list = []
for thispost in post_list:
  accessibility_caption = thispost.get('accessibility_caption','')
  #if accessibility_caption:
  #  print(accessibility_caption)
  caption = thispost.get('caption',{})
  if caption:
    caption_node = caption.get('node',{})
    if caption_node:
      caption_node_text = caption_node.get('text',{})
      if caption_node_text:
        all_caption_list.append(caption_node_text)

#print(all_caption_list)

for thiscaption in all_caption_list:
  if thiscaption:
    print(thiscaption)

allstring = ' '.join(all_caption_list)

#print(allstring)

tokens = allstring.split()

for i in range(len(tokens)):
  tokens[i] = tokens[i].lower()

caption_words = ""
caption_words += " ".join(tokens)+" "

stopwords = set(STOPWORDS)

wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(caption_words)
 
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()
