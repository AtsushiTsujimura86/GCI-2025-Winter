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


##特徴量とは
特徴量とは、機械学習モデルが予測のために使う情報（データの項目）のことです。 たとえば今回のデータでは、以下のようなものが特徴量になります：  
- Age
- Fare
- Pclass  
こうした特徴量をモデルに入力して、「この人は助かったか？」を予測していくわけです。数値の特徴量をグラフにして見てみることで、値のばらつきはあるか？極端に大きな値や小さな値（外れ値）はあるか？そもそもどういう分布になっているか？などのポイントを確認できます。


