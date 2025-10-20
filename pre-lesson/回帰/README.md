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



## 回帰とは
- **目的**：入力（説明変数）から、**連続値の出力（目的変数）**を予測する。
- **例**：
  - 身長 → 体重を予測  
  - 広告費 → 売上を予測  

---

## ⚙️ 1. 必要なライブラリ
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
```

---

## 📊 2. データの準備
```python
# サンプルデータ
data = {
    "height": [150, 160, 170, 180, 190],
    "weight": [50, 55, 65, 75, 85]
}
df = pd.DataFrame(data)

# 説明変数（X）と目的変数（y）
X = df[["height"]]  # DataFrame型（2次元）
y = df["weight"]    # Series型（1次元）
```

---

## ✂️ 3. 学習用とテスト用に分割
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 🧮 4. モデルの学習（訓練）
```python
model = LinearRegression()
model.fit(X_train, y_train)  # ← fitで学習
```

---

## 🔍 5. 予測と評価
```python
# 予測
y_pred = model.predict(X_test)

# 評価指標
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("平均二乗誤差:", mse)
print("決定係数 R^2:", r2)
```

---

## 🧩 6. 学習結果の確認
```python
print("傾き（係数）:", model.coef_)
print("切片:", model.intercept_)
```

---

## 📉 7. グラフで可視化（任意）
```python
import matplotlib.pyplot as plt

plt.scatter(X, y, color="blue", label="data")
plt.plot(X, model.predict(X), color="red", label="regression line")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()
plt.show()
```

---

## ✅ 要約

| 概念 | 関数/メソッド | 意味 |
|------|----------------|------|
| データ分割 | `train_test_split()` | 学習・評価を分ける |
| 学習 | `fit(X, y)` | 回帰式の係数を求める |
| 予測 | `predict(X)` | 学習した式で予測 |
| 評価 | `mean_squared_error`, `r2_score` | モデルの精度を測る |

---

## 💡 線形回帰モデルの式
学習の結果、モデルは次の形で表されます：

\[
\hat{y} = a x + b
\]

- \( a = \) `model.coef_`（傾き）
- \( b = \) `model.intercept_`（切片）
- \( \hat{y} = \) `model.predict(x)`（予測値）

