import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取csv文件
csv_file = 'data/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(csv_file, names=column_names, header=None)

# 定义不同种类鸢尾花的颜色和标签
colors = ['blue', 'red', 'green']
species_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# 创建绘图画布
plt.figure(figsize=(10, 10))

# 根据不同种类绘制散点图
for a, b in enumerate(species_labels):
    subset = df[df['species'] == b]
    plt.scatter(subset['petal_length'], subset['petal_width'], label=b, color=colors[a], marker='.', s=100)

# 添加图例
plt.figtext(0.5, 0.9, '蓝色--setosa | 红色-versicolor | 绿色-virginica')
plt.xlabel('Petal Length') # x轴标签
plt.ylabel('Petal Width') # y轴标签

plt.show() # 展示图形