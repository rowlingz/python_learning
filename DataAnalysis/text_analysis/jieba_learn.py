# -*- coding:utf-8 -*-

import jieba
# import jieba.analyse
import pandas as pd
import re


# jieba.cut 生成generator
# 全模式分词
seg_list = jieba.cut("我来北京上学", cut_all=True)
print("Full Model " + '/'.join(seg_list))

# 精确模式 （默认）
seg_list = jieba.cut("我来北京上学", cut_all=False)

# 加载自定义词典
jieba.load_userdict("newdic.txt")

text = "故宫的著名景点包括乾清宫、太和殿和午门等。其中乾清宫非常很精美了，午门是紫禁城的正门，午门居中向阳"


# 数据清洗
# 正则表达式取中文字符
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filter_data = re.findall(pattern, text)
text = ''.join(filter_data)
print(text)


# 获取关键词
# tags = jieba.analyse.extract_tags(text, topK=3)
# jieba.lcut 生成List
tags = jieba.lcut(text)
tags_df = pd.DataFrame({'segment': tags})

# 去除停用词
stopword = pd.read_csv("stopwords.txt", header=None, names=['words'], encoding='utf-8')
tags_df = tags_df[~tags_df['segment'].isin(stopword.words)]
# tags_df.index =
print(tags_df)

# 词频计数
word_count = tags_df.groupby('segment')['segment'].count().sort_values(ascending=False)
print(word_count[:5])

