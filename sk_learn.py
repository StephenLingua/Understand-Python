# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sk_learn
   Description：
   Author :       stephen
   date：          2019/6/5
-------------------------------------------------
   Change Activity:
                   2019/6/5:
-------------------------------------------------
"""
# 找出相似的词人
# 根据词预测作者
import numpy as np
from sklearn.preprocessing import Imputer, MinMaxScaler, StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# 降维
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

# 特征抽取




def vector():
    """
    数组数据抽取(中文需要用jieba 先分词等)
    向量化
    :return:
    """
    # 实例化
    vector_ = CountVectorizer()
    # 调用fit_transform 输入并转化数据
    res = vector_.fit_transform(["life is short, i use python", "hello python, hello world"])
    print(vector_.get_feature_names())
    print(res)
    """ csr_matrix
    (0, 3)	1
    (0, 5)	1
    (0, 4)	1
    (0, 1)	1
    (0, 2)	1
    (1, 6)	1
    (1, 0)	2
    (1, 3)	1
    """
    print(type(res.toarray()))
    """ ndarray
    ['hello', 'is', 'life', 'python', 'short', 'use', 'world']
    [[0 1 1 1 1 1 0]
    [2 0 0 1 0 0 1]]
    """
    return None


def dictvec():
    """
    字典数据抽取
    :return:
    """
    # 实例化
    dict = DictVectorizer(sparse=False)
    data = dict.fit_transform([{'city': '北京', 'temperature': 100},
                               {'city': '上海', 'temperature': 60},
                               {'city': '深圳', 'temperature': 30}])
    print(dict.get_feature_names())
    print(dict.inverse_transform(data))
    print(data)
    return None


def tfidfvec():
    """
    TF-IDF feature
    评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度
    对文本进行特征值化
    :return: None
    """
    tf = TfidfVectorizer()
    corpus = ['This is the first document.',
              'This document is the second document.',
              'And this is the third one.',
              'Is this the first document?'
              ]

    data = tf.fit_transform(corpus)
    print(tf.get_feature_names())
    print(data.toarray())
    return None

# 预处理


def mm():
    """
    归一化处理
    :return: None
    """
    mm = MinMaxScaler(feature_range=(2, 3))
    data = mm.fit_transform([[80, 3, 21, 31], [70, 31, 3, 13], [75, 4, 24, 2]])
    print(data)
    return None


def standard():
    """
    标准化缩放
    :return:
    """
    std = StandardScaler()
    data = std.fit_transform([[1., -1., 3.], [2., 4., 2.], [4., 6., -1.]])
    print(data)
    return None


def im():
    """
    # 缺失值处理
    :return:
    """
    # nan NanN
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)
    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])
    print(data)
    return None

# 降维


def var():
    """
    特征选择-删除低方差的特征
    :return: None
    """
    var = VarianceThreshold(threshold=0.0)
    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)
    return None


def pca_data():
    """
    主成分分析进行降维
    :return:  None
    """
    pca = PCA(n_components=0.95)
    data = pca.fit_transform([[28, 2, 3, 5], [2, 3, 51, 1], [2, 42, 1, 1]])
    print(data)
    return None


if __name__ == '__main__':
    var()

