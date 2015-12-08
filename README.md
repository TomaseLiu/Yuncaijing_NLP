分为几个模块：
1. 从ycj获取带主题tag的新闻数据；(Scrapy)
2. 对新闻中的标签做关系分析，并绘制主题关系图；(networkx)
3. 对新闻文本做TF-IDF分析，获得每个主题的描述词；（TF-IDF）
4. 对新闻做word2vec分析，获得每个主题的关联词集合；(word2vec)
