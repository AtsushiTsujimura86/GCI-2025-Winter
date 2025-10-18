# 回帰まとめ

## DataFrame操作
### 基本操作
``` python
#モジュールのインポート
import pandas as pd

#csvファイルの読み込み、dfはDataFrame
df = pd.read_csv('name_of_csv_file')

# CSVに保存
df.to_csv("output.csv", index=False)

# 先頭・末尾の確認
df.head()      # 先頭5行
df.tail(n)     # 末尾n行

# 情報の確認
df.info()      # 型や欠損確認
df.describe()  # 統計量（平均・分散など）

# 列の抽出
df["col1"]               # Series（1列）
df[["col1", "col2"]]     # DataFrame（複数列）

# 列を削除
df = df.drop("height", axis=1)        # axis=1 は「列方向」

# 行を削除
df = df.drop(0, axis=0)               # axis=0 は「行方向」
```

## 図の描画
### 散布図
```python
import matplotlib.pypolot as plt
plt.scatter(x,y)
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.show()
```
### 箱ひげ図
```python
import matplotlib.pypolot as plt
import seaborn as sns
plt.figure(figsize=(4,6))
sns.boxplot(y=df['engine_size')
plt.ylabel('engine_size')
plt.show()
```
<br>

## データの前処理
### 欠損値の削除
```python
# 欠損値の確認
df.isnull().sum()
#欠損値の削除
df_drop = df.dropna()
```
### 標準化
データの分布を、平均値0、標準偏差(分散)1に変換する処理。
体重と身長という二つの説明変数があったときに、体重は平均50、身長は平均170なら、身長の方が学習における影響が大きくなってしまう。だから標準化することでスケールをそろえる。
標準化をする必要のあるモデルは、線形回帰、ロジスティクス回帰、SVM(サポートベクターマシン)、KNN(k近傍法)、PCA(主成分分析)
```python
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

# データの学習（平均と標準偏差を覚える）
# ※ fit()には2次元配列（DataFrameやdf[['col']]）を渡す必要がある
ss.fit(df['engine_size']) # 二次元配列(DataFrameを渡す)

#学習したデータから、標準化
x_std = ss.transform(x)

#よく使われる書き方
x_std = scaler.fit_transform(df[['engine_size']])
```
