#!/usr/bin/env python
# encoding: utf-8
"""
@Author     :xinbei
@Software   :Pycharm
@File       :text_preprocess.py
@Time       :2019/5/30 21:38
@Purpose    :处理非格式化的汉字数据
"""
import jieba

# 自定义方法，读取txt文本
def getTxtText(filepath):
    """
    :param filepath:  str, path of single file
    :return: str, text data of file
    """
    str_textO = ''
    with open(filepath, 'rb')as f:
        str_textO += f.read().decode('utf-8')
    return str_textO


# 自定义方法，断句
## 定义句子结束符号，遍历文本，如果当前字符是结束符号，则断句并附加到list
def getTextSenteces(text):
    """
    :param text: str, used to clause
    :return: list of str, clause result
    """
    lst_punt = "!?。！？\n\r"                                # 句子结束符号
    lst_senteces = []                                        # 储存断句结果
    start = 0                                                # 句子开头光标位置
    text += '#'
    for i in range(len(text)):
        if text[i] in lst_punt and text[i+1] not in lst_punt:
            lst_senteces.append(text[start:i+1].strip())
            start = i+1
    return lst_senteces


# 自定义方法，获得分好词的汉语词列表
def getCutWords(senLst):
    """
    :param senLst: list of str, sentences list
    :return:  list of list, list of word and many lists form a list
    """
    return [list(jieba.cut(sen)) for sen in senLst]

if __name__ == '__main__':
    pass