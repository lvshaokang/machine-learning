# 分类
from sklearn.neighbors import KNeighborsClassifier
# 回归
from sklearn.neighbors import KNeighborsRegressor

"""
n_neighbors K值
weights 用来确定邻居的权重
    uniform 所有邻居权重相同
    distance 权重是距离的倒数
algorithm 规定计算邻居的方法
    auto 根据数据情况自动选择合适算法
    kd_tree KD树
    ball_tree 球树
    brute 暴力搜索
leaf_size 构造KD/球树时的叶子树,默认30

"""
KNeighborsClassifier(n_neighbors=5,weights='uniform',algorithm='auto',leaf_size=30)