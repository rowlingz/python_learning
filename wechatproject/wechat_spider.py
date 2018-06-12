# -*- coding:utf-8 -*-
import wechatsogou
import pandas as pd
import time

ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)


def get_articles(gzh_name):
    """
    根据公众号名称 查找出近期的文章，及其相关信息
    :param gzh_name: 公众号 名称  str
    :return:  公众号文章汇总信息  dataframe
    """

    recent_article = ws_api.get_gzh_article_by_history(gzh_name)

    df_article = pd.DataFrame(recent_article['article'])

    article_num = len(recent_article['article'])

    df_gzh_info = pd.DataFrame([recent_article['gzh']] * article_num)

    df = pd.concat([df_gzh_info, df_article], axis=1)

    df['datetime'] = df['datetime'].apply(lambda x: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x)))

    # print(df)
    df.to_csv('article_content.csv', encoding='utf-8_sig', index=False, mode='a')
    return df


if __name__ == "__main__":
    # get_articles('CSDN')
    pass


