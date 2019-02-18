"""
# 对文档进行分词

# 英文
import nltk
word_list = nltk.word_tokenize(text)
nltk.pos_tag(word_list)

# 中文
import jinba
word_list = jieba.cut(text)
"""

"""
# 加载停用词表

import io
stop_words = [line.strip().decode('utf-8') for line in io.open('stop_words.txt').readlines()]
"""

"""
# 计算单词的权重

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(stop_words=stop_words,max_df=0.5)
features = tf.fit_transform(train_contents)
"""

"""
# 朴素贝叶斯分类器

from sklearn.naive_bayes import MultinomialNB
# alpha 平滑参数 
clf = MultinomialNB(alpha=0.001).fit(train_features,train_labels)
"""

"""
# 使用生成的分类器做预测

test_tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=train_vocabulary)
test_features=test_tf.fit_transform(test_contents)

predicted_labels=clf.predict(test_features)
"""

"""
# 计算准确率

from sklearn import metrics
print(metrics.accuracy_score(test_labels,predicted_labels))
"""

