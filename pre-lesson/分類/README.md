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
