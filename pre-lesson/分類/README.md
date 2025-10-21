# 分類

## 決定木
### 決定木（Decision Tree）の基本

**決定木（Decision Tree）** とは、データの特徴量を利用して条件分岐を繰り返し、  
データの特徴とラベルの関係を学習する手法です。  
主に **ラベルの分類タスク** で利用されます。

---

## 🍄 例：キノコの有毒・無毒分類

次のような表を考えます。目的は、キノコの形的特徴（height, width）から  
**有毒か無毒か（poison）** を判定することです。

| ID | height (cm) | width (cm) | poison (Yes/No) |
|----|--------------|-------------|----------------|
| 001 | 5 | 4 | N |
| 002 | 3 | 2 | N |
| 003 | 4 | 3 | Y |
| 004 | 2 | 1 | N |
| 005 | 6 | 2 | Y |

---

### ステップ1：高さ4cm以下で分割

高さが4cm以下かどうかの条件でデータを分けます。

**【高さ4cm以下であるキノコ】 ⇒ グループ1（無毒キノコのみ）**

| ID | height | width | poison |
|----|---------|--------|--------|
| 002 | 3 | 2 | N |
| 004 | 2 | 1 | N |

**【高さ4cm以下でないキノコ】 ⇒ グループ2（有毒・無毒キノコを含む）**

| ID | height | width | poison |
|----|---------|--------|--------|
| 001 | 5 | 4 | N |
| 003 | 4 | 3 | Y |
| 005 | 6 | 2 | Y

### ステップ2：さらにグループ2を幅で分割

高さが4cm以下でないグループ2には、有毒と無毒が混在しています。  
次に「幅が3cm以下かどうか」で分けます。

**【高さ4cm以下でなく、幅3cm以下であるキノコ】 ⇒ グループ2-1（有毒キノコのみ）**

| ID | height | width | poison |
|----|---------|--------|--------|
| 003 | 4 | 3 | Y |
| 005 | 6 | 2 | Y |

**【高さ4cm以下でなく、幅3cm以下でないキノコ】 ⇒ グループ2-2（無毒キノコのみ）**

| ID | height | width | poison |
|----|---------|--------|--------|
| 001 | 5 | 4 | N |

<img width="550" height="250" alt="image" src="https://github.com/user-attachments/assets/fd847094-7a41-4892-a0c6-b023e2994476" />

``` python
from sklearn.tree import DecisionTreeClassifier, plot_tree

# ③ モデル作成
model = DecisionTreeClassifier(random_state=0)

# ④ 学習
model.fit(X_train, y_train)  # ← fit()：訓練データから木構造を学習

# ⑤ 評価
score = model.score(X_test, y_test)  # ← score()：正解率を返す
print("正解率:", score)

# ⑥ 決定木の可視化
plt.figure(figsize=(10, 6))
plot_tree(
    model,
    filled=True,                # クラスごとに色分け
    feature_names=iris.feature_names,  # 特徴量名
    class_names=iris.target_names      # クラス名
)
plt.show()
```

---

## 🧮 主なメソッド

| メソッド | 役割 | 説明 |
|-----------|------|------|
| `.fit(X, y)` | 学習 | 特徴量と正解ラベルから木構造を構築 |
| `.predict(X)` | 予測 | 新しいデータのクラスを予測 |
| `.score(X, y)` | 評価 | 正解率（Accuracy）を計算 |
| `plot_tree(model)` | 可視化 | 学習済みの木をグラフで描画 |


## 欠損値の補完
### 単純な最頻値による補完
<img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/39a41bbc-6711-4b95-b614-0a660d338af6" />

```python
print(df["bruises"].describe())
```
uniqueは種類の数、topは最頻値、frecは最頻値の数
<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/106aacb8-c4f9-4a42-bb32-d9388cf1feed" />
```python
#bruisesの最頻値を取得
 top = df["bruises"}.describe()['top']
  --> 'N'

#最頻値で欠損値補完
df_fill = df.fillna(top)
```
今回は、欠損しているのが"bruises"の列だけだったから、この書き方で行ける。この書き方はすべての欠損値を引数の値で埋める。  
複数列で欠損値がある場合は、```df.fillna({'name': 'XXX', 'age': 20, 'ZZZ': 100})```

上の例ではすべての欠損値を"bruises"の最頻値で補完したが、データによっては、特徴量同士に関係性を持つ可能性がある。
例えば、白いキノコであれば斑点ありの傾向があるなど  
--> 次はキノコの色ごとの"bruises"の最頻値を求め、それでそれぞれの欠損値を補完していく。

### キノコの色ごとの"bruises"の最頻値による補完
<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/9f85eaed-43a2-4fa3-9815-add723832821" />
<br>

```python
#"cap_color"でグループ分けして、それぞれの"cap_color"ごとの"bruises"の最頻値を取得
top = df.groupby(["cap_color"])["bruises"].describe()["top"]
```
<img width="130" height="310" alt="image" src="https://github.com/user-attachments/assets/d8c64661-f864-452b-beb3-76efa8091581" />
<br>

```python
#bruisesの欠損値のあるデータのみ取得
is_null = df['bruises'].isnull()
```
<img width="150" height="320" alt="image" src="https://github.com/user-attachments/assets/58c0b19e-fa53-4970-a149-a4151a52626b" />
<br>

欠損行を抽出するには、loc属性の[]の中に、欠損値の**真偽値**のSeriesオブジェクトを渡します
```python
df.loc[is_null]
```
<img width="150" height="120" alt="image" src="https://github.com/user-attachments/assets/614e8857-04dc-47ad-a41c-14980973cb49" />
<br>

欠損値に色のグループで分けた最頻値を代入する。代入する値は、変数topsに対して各インデックスを指定して参照した最頻値
```python
for color in df['cap_color'].unique():
  df.loc[(df['cap_color'] == color) & (is_null), 'bruises'] = tops[color]
```
補足：  
```df.loc[mask, 'bruises']```  → マスク(真偽の条件)で選んだ行の 'bruises' 列を指す。
``` python
# 形式
# df.loc[行ラベル or ブール配列, 列ラベル]
df.loc[3, 'bruises']                 # 行ラベル3の 'bruises' を取得
df.loc[df['cap_color']=='a', :]      # 条件で行抽出（全列）
df.loc[rows_mask, ['height','width']]# マスクで行、列名で列を指定
df.loc[:, 'bruises'] = 'N'           # 列全体を書き換え
df.loc[rows_mask, 'bruises'] = value # 条件行だけを安全に代入（推奨）
```





