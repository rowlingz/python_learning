# -*- coding:utf-8 -*-
import pandas as pd

filename = "./pydata-book-master/ch09/P00000001-ALL.csv"
data = pd.read_csv(filename, low_memory=False)


def get_party(data):
    parties = {'Bachmann, Michelle': 'Republican',
               'Romney, Mitt': 'Republican',
               'Obama, Barack': 'Democrat',
               "Roemer, Charles E. 'Buddy' III": 'Republican',
               'Pawlenty, Timothy': 'Republican',
               'Johnson, Gary Earl': 'Republican',
               'Paul, Ron': 'Republican',
               'Santorum, Rick': 'Republican',
               'Cain, Herman': 'Republican',
               'Gingrich, Newt': 'Republican',
               'McCotter, Thaddeus G': 'Republican',
               'Huntsman, Jon': 'Republican',
               'Perry, Rick': 'Republican'}
    data['party'] = data['cand_nm'].map(parties)
    return data


if __name__ == '__main__':
    data = get_party(data)
    print(data.head())
    print(data.party.value_counts())