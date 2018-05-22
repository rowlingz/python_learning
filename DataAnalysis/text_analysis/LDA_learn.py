# -*- coding:utf-8 -*-
import jieba
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


def extract_words(text):
    """提取文字"""
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filter_data = re.findall(pattern, text)
    return ''.join(filter_data)


def chinese_word_cut(text):
    """去除停用词/文本分词"""
    tags = jieba.lcut(text)
    tags_df = pd.DataFrame({'tags': tags})
    stopwords = pd.read_csv('stopwords.txt', header=None, names=['words'], encoding='utf-8')
    tags_df = tags_df[~tags_df['tags'].isin(stopwords.words)]
    tags_list = tags_df['tags'].tolist()
    return ' '.join(tags_list)


def print_top_words(model, feature_names, n_top_words):
    """把每个主题里面的前n_top_words个关键词显示出来"""
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d" % topic_idx)
        print(' '.join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1: -1]]))
        print()


if __name__ == "__main__":
    # # 加载自定义词典
    # jieba.load_userdict("newdic.txt")
    #
    # df = pd.read_csv("datascience.csv", encoding='gb18030')
    # df['text'] = df['content'].apply(extract_words)
    # df["content_cutted"] = df['text'].apply(chinese_word_cut)
    #
    # df.to_csv("filter_datascience.csv", encoding='utf_8_sig', index_label=False)

    df = pd.read_csv("filter_datascience.csv", encoding='utf-8')
    print(df.dtypes)

    # 文本向量化
    # 关键词提取和向量转换过程
    features = 1000  # 只从文本中提取1000个最重要的特征关键词
    tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                    max_features=features,
                                    stop_words='english',
                                    max_df=0.5,
                                    min_df=10)
    tf = tf_vectorizer.fit_transform(df['content_cutted'].values.astype('U'))

    # 应用LDA方法
    n_topics = 5  # 人为设定主题的数量
    lda = LatentDirichletAllocation(n_components=n_topics,
                                    max_iter=50,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)
    lda.fit(tf)

    tf_feature_name = tf_vectorizer.get_feature_names()

    # 获取各主题前n_top_words个关键词
    n_top_words = 20
    print_top_words(lda, tf_feature_name, n_top_words)
    print("end")
