#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

print("Hello world")

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba

from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator

d = path.dirname(__file__)

#读取要生成词云的文件
o_text = open(path.join(d, 'mytext.txt'),"r",encoding="utf-8").read()
#通过jieba分词进行分词并通过空格分隔
seg_list = jieba.cut(o_text, cut_all=True)
text = " ".join(seg_list)
# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "sjl.jpg")))

stopwords = set(STOPWORDS)
stopkey_selonsy = {'今天','没有','哈哈','这个','不是','可以','还是','什么','表情','图片','视频','实时','网页消息'}
stopkey_hit=[line.strip() for line in open('hit-stopwords.txt',"r",encoding="utf-8").readlines()]
stopwords.update(stopkey_selonsy)
stopwords.update(stopkey_hit)

font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(background_color="white",
               font_path=font, 
               max_words=8000, 
               mask=alice_mask,
               stopwords=stopwords,
               max_font_size=40,
               #random_state=42,
               width=1920,
               height=1080
               #scale=0.5
               )

# generate word cloud
wc.generate(text)

# create coloring from image
#image_colors = ImageColorGenerator(alice_mask)

# store to file
wc.to_file(path.join(d, "sjl1.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()

# 我们还可以直接在构造函数中直接给颜色
# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
#plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#plt.axis("off")
#plt.figure()

plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
