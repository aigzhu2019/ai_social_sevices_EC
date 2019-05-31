#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :language_model.py
@Time       :2019/5/30 22:09
@Version    :
@Purpose    :隐马尔可夫模型、线性插值平滑、拉普拉斯平滑、Viterbi算法
"""

# 自定义方法，获得添加开始符号以及结束符号的分词结果
def get_ngramsModel(ary_cws, ngram):
    """
    :param ary_cws: array, cut-words array
    :param ngram:  int, n gram Markov model
    :return:tuple of cut-words model, dict of count n-gram models and total counts of n-gram models
    """
    ngrams_model, sen = [], []  # ngram总模型，ngram当前模型结果
    d_cmn = {}  # 模型数量统计
    i_tn = 0  # 文本分词总词数
    for sle_ary in ary_cws:
        sen = list(sle_ary)
        ## 在列表开头插入n-1个星号
        for i in range(ngram - 1):
            sen.insert(0, '*')
        ## 在列表末尾插入1个星号
        sen.append('#')

        # 自定义方法，获得ngram分组的列表
        get_ngramsLst = lambda lst_cws, n: zip(*[lst_cws[i:] for i in range(n)])

        sen = list(get_ngramsLst(sen, ngram))

        for m in sen:
            d_cmn[m] = d_cmn.get(m, 0) + 1
            i_tn += 1

        ngrams_model.append(sen)
    return ngrams_model, d_cmn, i_tn



if __name__ == '__main__':
    pass