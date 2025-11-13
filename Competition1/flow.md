# コンペの流れ
## ライブラリのインポート
## データの指定、読み込み
## データの確認
```python
train.head()
train.info()
```
## データ分析・EDA
EDA（Exploratory Data Analysis）＝探索的データ分析とは、機械学習のモデルを作る前に、データの中身をよく観察して理解する作業のこと。  
EDAを行うことで、データにどんな特徴があるのかを見つけることができます。
たとえば、以下のようなポイントをチェックします：
- 変な値（外れ値）が入っていないか
- 抜けているデータ（欠損値）がどれくらいあるか
- 特定のグループや数字に偏りがないか
- データの値がどんな分布をしているか（例：ばらつきが大きい？小さい？）
 ### 欠損値の確認
 ```python
train.isnull().sum()
test.isnull().sum()
```
### データの可視化
```python
# 生存の値カウント（0=生存, 1=死亡）
drafted_counts = train['Perished'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(drafted_counts.index.astype(str), drafted_counts.values)

# ラベルとタイトル
plt.title('生存者の分布', fontsize=16)
plt.xlabel('生存状況（0：生存、1：死亡）', fontsize=14)
plt.ylabel('人数', fontsize=14)

# グリッド線
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
```
<img width="300" height="250" alt="image" src="https://github.com/user-attachments/assets/98332bd0-5ac7-4831-bcbd-c69e58a34b2e" />


## 補足1 `.value_counts()` とは？

`Series`（＝1列のデータ）に対して使うと、  
**「値ごとの出現回数」を数えてくれるメソッド** です。

### 🔹 例

```python
import pandas as pd

train = pd.DataFrame({
    "Age": [22, 38, 26, 35, 35, 22, 22]
})

a = train["Age"].value_counts()
print(a)
```

### 🔹 出力

```
22    3
35    2
38    1
26    1
Name: Age, dtype: int64
```

- 「22」は3回出現  
- 「35」は2回出現  
- 「38」と「26」はそれぞれ1回

→ **降順（多い順）で並ぶ** のがデフォルト。

つまり、  
`value_counts()` は「何がどのくらい出てくるか」を要約した `Series` を返します。

---

## 補足2 `.index` とは？

`index` は **SeriesやDataFrameの「行ラベル」** のこと。  
つまり、「何を数えたか」という“値の一覧”を取り出せます。

上の例で：

```python
print(a.index)
```

を実行すると、

```
Int64Index([22, 35, 38, 26], dtype='int64')
```

と出ます。

- `.index` → `[22, 35, 38, 26]` という **値そのもの（順序付き）**
- `.values` → `[3, 2, 1, 1]` という **出現回数**

---

### 🔹 組み合わせるとこうなる

```python
for age, count in zip(a.index, a.values):
    print(f"{age}歳: {count}人")
```

出力：
```
22歳: 3人
35歳: 2人
38歳: 1人
26歳: 1人
```

---

## 3️⃣ まとめ

| メソッド | 返すもの | よく使う目的 |
|-----------|-----------|--------------|
| `.value_counts()` | 値ごとの出現回数を数えたSeries | カテゴリ分布や頻度分析 |
| `.index` | SeriesやDataFrameの行ラベル | 何を数えたか（＝ユニークな値）を取得 |
| `.values` | 実際の値（数値部分） | 回数などの生データを取り出す |


## 特徴量とは
特徴量とは、機械学習モデルが予測のために使う情報（データの項目）のことです。 たとえば今回のデータでは、以下のようなものが特徴量になります：  
- Age
- Fare
- Pclass  
こうした特徴量をモデルに入力して、「この人は助かったか？」を予測していくわけです。数値の特徴量をグラフにして見てみることで、値のばらつきはあるか？極端に大きな値や小さな値（外れ値）はあるか？そもそもどういう分布になっているか？などのポイントを確認できます。

## 特徴量の可視化
```python
num_cols = ["Age", "SibSp", "Parch", "Fare"]

# サブプロットの行数
n_rows = len(num_cols)

fig, axes = plt.subplots(n_rows, 2, figsize=(10, 4 * n_rows))

for i, col in enumerate(num_cols):
    # 共通のx軸範囲を計算
    min_val = min(train[col].min(), test[col].min())
    max_val = max(train[col].max(), test[col].max())

    # 左: train
    axes[i, 0].hist(train[col].dropna(), bins=30, color="skyblue", edgecolor="black")
    axes[i, 0].set_title(f"Train - {col}")
    axes[i, 0].set_xlim(min_val, max_val)

    # 右: test
    axes[i, 1].hist(test[col].dropna(), bins=30, color="salmon", edgecolor="black")
    axes[i, 1].set_title(f"Test - {col}")
    axes[i, 1].set_xlim(min_val, max_val)

plt.tight_layout()
plt.show()
```


##  `fig` と `axes` の正体

### 1️⃣ matplotlibの構造をざっくり言うと…

matplotlibでは、  
**1枚の「図（Figure）」の中に、いくつもの「グラフ（Axes）」が並んでいる**  
という階層構造になっています。

```
Figure（全体のキャンバス）
 ├── Axes[0,0]（グラフ1）
 ├── Axes[0,1]（グラフ2）
 ├── Axes[1,0]（グラフ3）
 └── Axes[1,1]（グラフ4）
```

つまり：

| 変数名 | 意味 | 役割 |
|---------|------|------|
| `fig` | Figure（フィギュア） | グラフ全体を入れる「キャンバス」 |
| `axes` | Axes（アクシーズ） | 実際に描く「個々のグラフ（サブプロット）」 |

---

### 2️⃣ 具体的な例

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
```

これで：

- `fig` → 1つの全体キャンバス（Figure）
- `axes` → 2×2の「小さなグラフ（Axes）」が入った配列（numpyの2次元配列のようなもの）

```
axes[0,0]  axes[0,1]
axes[1,0]  axes[1,1]
```

このようなレイアウトで4つのグラフを置けます。

---

### 3️⃣ 1つずつ描くときの使い方

```python
axes[0,0].plot(x, y1)
axes[0,0].set_title("グラフ1")

axes[1,0].plot(x, y2)
axes[1,0].set_title("グラフ2")
```

こうすると、「それぞれの小さいグラフ」に対して個別の描画や設定ができます。  
（`axes[i, j]` のようにインデックス指定）

---

### 4️⃣ よくあるパターン

| コード | 説明 |
|--------|------|
| `fig, ax = plt.subplots()` | グラフ1つだけ → `ax`（単数） |
| `fig, axes = plt.subplots(2, 2)` | グラフ複数 → `axes`（配列） |
| `figsize=(w, h)` | 全体サイズを指定（単位はインチ） |


## カテゴリデータとは
カテゴリデータとは、数ではなく「グループ」や「ラベル」などで表されるデータのことです。 今回のデータの中では、以下のようなものがカテゴリデータに当たります：  
- Sex（male / female）
- Embarked（C / Q / S）
- Pclass（1 / 2 / 3）  
こういったデータは、「数の大小」で比較するのではなく、どのグループに属しているかが重要になります。カテゴリデータも、棒グラフなどを使って可視化することで、どのカテゴリが多いのか少ないのか（データの偏り）、予測に使えそうな特徴量はどれかといったことが見えてきます。

```python
# 可視化するカテゴリ列
cat_cols = ["Sex", "Embarked", "Pclass"]

# サブプロットの行数
n_rows = len(cat_cols)

fig, axes = plt.subplots(n_rows, 2, figsize=(10, 4 * n_rows))

for i, col in enumerate(cat_cols):
    # 左: train
    train_counts = train[col].value_counts(dropna=False)
    axes[i, 0].bar(train_counts.index.astype(str), train_counts.values, color="skyblue", edgecolor="black")
    axes[i, 0].set_title(f"Train - {col}")

    # 右: test
    test_counts = test[col].value_counts(dropna=False)
    axes[i, 1].bar(test_counts.index.astype(str), test_counts.values, color="salmon", edgecolor="black")
    axes[i, 1].set_title(f"Test - {col}")

    # 横軸ラベルを揃える
    axes[i, 0].set_xticks(range(len(train_counts.index)))
    axes[i, 0].set_xticklabels(train_counts.index.astype(str), rotation=45)

    axes[i, 1].set_xticks(range(len(test_counts.index)))
    axes[i, 1].set_xticklabels(test_counts.index.astype(str), rotation=45)

plt.tight_layout()
plt.show()

```

## 欠損値の補完とエンコーディング
- 欠損値の補完：データの中で抜けている部分（欠損値）を、平均値や最頻値などを使って埋める作業です。
- エンコーディング：文字（例：Sexの「male」「female」）で書かれた情報を、機械学習で使えるように数字に変換する作業です。

欠損値補完には中央値(median)、平均値(mean)、最頻値(mode)、外れ値で補完、モデルの予測結果で補完などがある。  
`fillna(補完する値)`で欠損値(NaN)を補完できる。
```python
# 最頻値で補完する対象の列
cols_to_fill = ["Cabin", "Embarked"]

# train の最頻値で train/test 両方を補完
for col in cols_to_fill:
    mode_value = train[col].mode()[0]
    train[col] = train[col].fillna(mode_value)
    test[col] = test[col].fillna(mode_value)
```

#### エンコーディングの代表的な手法
- One-hot Encoding：カテゴリごとに新しい列を作り、0か1で表す方法
- Label Encoding：カテゴリに順番をつけて、0, 1, 2…と数字に置き換える方法
今回は、 Label Encoding を使います。 Label Encodingは「男性 → 0、女性 → 1」のように、カテゴリをシンプルに数字に置き換える方法で、手軽に使えるのが特徴です。
```python
# カテゴリデータをラベルエンコーディング
from sklearn.preprocessing import LabelEncoder 
label_encoders = {}
for c in ["Sex", "Cabin", "Embarked"]:
    label_encoders[c] = LabelEncoder()
    label_encoders[c].fit(pd.concat([train[c], test[c]]).astype(str))
    train[c] = label_encoders[c].transform(train[c].astype(str))
    test[c] = label_encoders[c].transform(test[c].astype(str))
```
