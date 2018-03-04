# -*- coding: utf-8 -*-
import pandas as pd

neg_file = "meidi_jd_neg_cut.txt"
pos_file = "meidi_jd_pos_cut.txt"
stoplist = "stoplist.txt"

neg = pd.read_csv(neg_file, encoding='utf-8', header=None)
pos = pd.read_csv(pos_file, encoding='utf-8', header=None)
stop = pd.read_csv(stoplist, encoding='utf-8', header=None, sep='tipdm')
stop = [' ', ''] + list(stop[0])

neg[1] = neg[0].apply(lambda s: s.split(' '))
neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop])

pos[1] = pos[0].apply(lambda s: s.split(' '))
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])

