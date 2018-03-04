'''
@author Sam 
@date 2018-03-04
@desc 金蝶数据开发工程师笔试题：购物篮数据分析测试
'''
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
# 加载数据
df = pd.read_excel("D://DataSet.xlsx")
# 数据预处理
# df = df.loc[:, ["order_id", "item_code", "category_id", "simple_name", "category_name","Quantity"]]
df = df.loc[:, ["order_id", "item_code", "category_id", "simple_name", "category_name", "Quantity"]]
df["simple_name"] = df["simple_name"].str.strip()
df = df.loc[:, ["order_id", "category_id", "Quantity"]]
# 构建满足算法使用的购物篮数据集
basket = (df.groupby(['order_id', 'category_id'])['Quantity']
          .sum().unstack().reset_index().fillna(0).set_index('order_id'))
# print(basket.head())
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
basket_set = basket.applymap(encode_units)
# 执行关联挖掘算法Apriori
frequent_itemsets = apriori(basket_set, min_support=0.07, use_colnames=True)
# print(frequent_itemsets.head())
# 输出频繁项集
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(rules)
rules = rules[(rules['lift'] >= 1) &(rules['confidence'] >= 0.8)]
print(rules)