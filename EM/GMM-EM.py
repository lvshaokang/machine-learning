# from sklearn.mixture import GaussianMixture

# 创建GMM聚类
"""
n_components 高斯混合模型的个数,要聚类的个数
covariance_type 协方差类型
max_iter 最大迭代次数 
"""
# gmm = GaussianMixture(n_components=1,covariance_type='full',max_iter=100)

# prediction = gmm.predict(data)

import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

data_ori = pd.read_csv("EM/heros.csv",encoding='gb18030')
features = [u'最大生命',u'生命成长',u'初始生命',u'最大法力', u'法力成长',u'初始法力',u'最高物攻',u'物攻成长',u'初始物攻',u'最大物防',u'物防成长',u'初始物防', u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data_ori[features]

# 可视化
# 中文标签显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

# 热力图
corr = data[features].corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,annot=True)
plt.show()

# features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血',
#                   u'最大每5秒回蓝', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
# data = data_ori[features_remain]
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%'))/100)
data[u'攻击范围'] = data[u'攻击范围'].map({'远程':1,'近战':0})
ss = StandardScaler()
data = ss.fit_transform(data)
gmm = GaussianMixture(n_components=30,covariance_type='full')
gmm.fit(data)

#训练数据
prediction = gmm.predict(data)
print(prediction)

data_ori.insert(0,'分组',prediction)
data_ori.to_csv("EM/hero_out.csv",index=False,sep=',')

# 聚类结果的评估方法
from sklearn.metrics import calinski_harabaz_score
print(calinski_harabaz_score(data,prediction))