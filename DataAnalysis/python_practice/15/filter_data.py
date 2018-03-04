# -*- coding: utf-8 -*-
import pandas as pd
import jieba


def filter_data(need):
    """删选出指定品牌的评论"""
    data = pd.read_csv(need['input_filename'], encoding='utf-8')
    filter_data = data[need['need_part']][data[u'品牌'] == need['need_condition']]
    filter_data.to_csv(need['output_filename'], index=False, sep=',', header=False)


def clean_same(input_filename, output_filename):
    """原始数据去重"""
    data = pd.read_csv(input_filename, encoding='utf-8', header=None)
    initial_length = len(data)
    data = pd.DataFrame(data[0].unique())
    after_length = len(data)
    data.to_csv(output_filename, index=False, header=False, encoding='utf-8')
    print("删除了%s条重复的数据。" % (initial_length - after_length))


def delet_prefixscore(input_filename, output_filename):
    """删除前缀评分"""
    f = open(input_filename, 'rb')
    data = pd.read_csv(f, encoding='utf-8', header=None)
    data1 = pd.DataFrame(data[0].str.replace('.*?\d+?\ \t ', ''))
    data1.to_csv(output_filename, index=False, header=False, encoding='utf-8')


def cut_word(input_filename, output_filename):
    """结巴分词"""
    data = pd.read_csv(input_filename, encoding='utf-8', header=None)
    mycut = lambda s: ' '.join(jieba.cut(s))        # 自定义简单分词函数
    data = data[0].apply(mycut)
    data.to_csv(output_filename, index=False, header=False, encoding='utf-8')


if __name__ == '__main__':

    need1 = {}
    need1['input_filename'] = "huizong.csv"
    need1['output_filename'] = "meidi_jd.txt"
    need1['need_part'] = u'评论'
    need1['need_condition'] = u'美的'

    # filter_data(need1)
    # clean_same("meidi_jd.txt", "meidi_jd_clean_same.txt")
    # delet_prefixscore('meidi_jd_process_end_负面情感结果.txt', 'meiji_jd_neg.txt')
    # delet_prefixscore('meidi_jd_process_end_正面情感结果.txt', 'meiji_jd_pos.txt')
    cut_word('meiji_jd_neg.txt', 'meiji_jd_neg_cut.txt')
    cut_word('meiji_jd_pos.txt', 'meiji_jd_pos_cut.txt')