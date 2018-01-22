# coding = UTF-8


import requests
from bs4 import BeautifulSoup
import re
import jieba
import pandas as pd


def get_comment(comment_url):
    response = requests.get(comment_url)
    html_data = response.text.encode(response.encoding).decode('utf-8')
    bf = BeautifulSoup(html_data, "html.parser")
    comment_list = bf.find_all('div', class_='comment')

    each_comment_list = []
    file = open("comment.txt", 'w', encoding='utf-8')
    for comment in comment_list:
        if comment.find('p').string is not None:
            each_comment = comment.find('p').string
            each_comment_list.append(each_comment)
            file.write(each_comment + '\n')

    return each_comment_list


url = "https://movie.douban.com/subject/6874741/?from=showing"
comment_url = "https://movie.douban.com/subject/6874741/comments?status=P"
comments = get_comment(comment_url)


# 数据清洗
with open('comment.txt', 'r', encoding='utf-8') as file_obj:
    comments = file_obj.read()

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)

segment = jieba.lcut(cleaned_comments)
words_df = pd.DataFrame({'segment': segment})
print(words_df.head())
print(words_df.shape)

stopwords = pd.read_csv('chineseStopWords.txt', index_col=False, quoting=3,
                        sep='\t', names=['stopword'])
print(stopwords.head())
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
print("去除停用词——————————————————————————")
print(words_df.head())
print(words_df.shape)

with open('chineseStopWords.txt', 'r') as fi:
    # s = fi.read()
    print(fi.decode('utf-8'))
