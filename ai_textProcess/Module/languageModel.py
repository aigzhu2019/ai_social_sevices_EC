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
import numpy as np

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


# 自定义方法，获取分好词的文本中p(s_i)，
def get_pSen(lst_ngram, d_countNgrams, d_countN_1grams):
    lst_p = []

    for l in lst_ngram:
        p = 1  # p初始化
        for ng in l:
            if ng[0] == '*':
                bi = ng[1:]
            else:
                bi = ng[0:2]
            #             print(ng, bi)
            mol, deno = d_countNgrams.get(ng, None), d_countN_1grams.get(bi, None)
            #             print('```',mol, deno)
            if mol != None and deno != None:
                p *= round(mol / deno, 5)
            #                 print('\t',ng,bi ,mol/deno, p)
            else:
                p = 0
                break

        #         print(lst_ngram.index(l), p)
        lst_p.append(p)
    return lst_p


# 自定义方法，计算测试集迷惑度
def get_perplexity(l_p, M):
    perp = 0
    for p in l_p:
        if not p:
            perp += 0
            continue
        perp += np.log2(p)
    perp /= M

    return 2 ** (-perp)
if __name__ == '__main__':
    pass