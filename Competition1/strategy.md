# 🎯 Titanic コンペティション攻略ガイド

## 🧭 目的
生存（`Survived`）を「予測」する分類問題。  
つまり、**特徴量（性別・年齢・階級など）から、生存 or 死亡を2値分類**するタスク。

---

## 🧠 1. 必要な知識（基礎理論）

### 1.1 機械学習の基本構造
- **入力 (features)** → `Pclass`, `Sex`, `Age`, `Fare`, etc.  
- **出力 (target)** → `Survived`（0:死亡, 1:生存）
- **モデル (model)** → 決定木, ランダムフォレスト, XGBoost, など
- **評価 (evaluation)** → 精度（`accuracy`）

### 1.2 前処理の基礎知識
| 手法 | 内容 | 例 |
|------|------|------|
| 欠損値処理 | 欠けたデータを補完 | `Age`を中央値で補完 |
| カテゴリ変換 | 文字を数値に変換 | `Sex` → `0/1` |
| 特徴量スケーリング | 値のスケールを揃える | 標準化、MinMaxなど |
| 特徴量エンジニアリング | 新しい特徴を作る | `FamilySize = SibSp + Parch + 1` |

### 1.3 分類モデルの基礎
主なモデル：
- **決定木（DecisionTree）**
- **ランダムフォレスト（RandomForest）**
- **XGBoost / LightGBM**
- **ロジスティック回帰**

特徴：
| モデル | 強み | 弱み |
|--------|------|------|
| DecisionTree | 解釈が簡単 | 過学習しやすい |
| RandomForest | 汎化性能が高い | 解釈しづらい |
| XGBoost | 精度が高い | パラメータ調整が必要 |
| LogisticRegression | シンプルで速い | 線形にしか対応できない |

---

## 🧩 2. ステップ別の進め方

### 🪜 Step 1: データ理解
1. `train.csv` と `test.csv` を読み込む
2. `df.info()`, `df.describe()`, `df.head()` で全体像を把握
3. 欠損値や分布を確認（`sns.heatmap(df.isnull())`など）

### 🪜 Step 2: 前処理（Data Cleaning）
- 欠損値補完（例: `Age`, `Cabin`, `Embarked`）
- カテゴリを数値化（`Sex` → `0/1`、`Embarked` → One-Hot）
- 不要列を削除（`Name`, `Ticket`, `Cabin` など）

```python
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Age'] = df['Age'].fillna(df['Age'].median())
df = pd.get_dummies(df, columns=['Embarked'])
```

### 🪜 Step 3: 特徴量エンジニアリング
例：
```python
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
```

- 他にも `Title`（Mr, Mrs, Missなど）を`Name`から抽出するのが定番。

```python
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Mlle','Ms'],'Miss').replace('Mme','Mrs')
```

### 🪜 Step 4: モデル学習
- 学習データを分割（`train_test_split`）
- モデルを学習・評価

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_val)
print("Accuracy:", accuracy_score(y_val, pred))
```

---

### 🪜 Step 5: モデル改善
- パラメータチューニング（GridSearchCV / Optunaなど）
- 重要特徴量の分析（`model.feature_importances_`）
- 不要特徴の削除や新特徴の追加

```python
from sklearn.model_selection import GridSearchCV

params = {
    'n_estimators': [100, 200],
    'max_depth': [4, 6, 8, None],
}
grid = GridSearchCV(RandomForestClassifier(random_state=42), params, cv=5)
grid.fit(X_train, y_train)
print("Best Params:", grid.best_params_)
```

---

### 🪜 Step 6: 提出（Submission）
- `test.csv` に同じ前処理を行い、予測結果をCSV出力

```python
test_pred = model.predict(test_df)
submission = pd.DataFrame({'PassengerId': test_df['PassengerId'], 'Survived': test_pred})
submission.to_csv('submission.csv', index=False)
```

Kaggleにアップロード → スコア（accuracy）が出る！

---

## 🧠 3. 上達のポイント

| ステップ | 改善の方向 |
|-----------|-------------|
| 前処理 | 欠損補完をより賢く（平均→グループ別中央値など） |
| 特徴量 | `Title`, `Deck`, `FamilySize`, `FarePerPerson` など創造的に |
| モデル | XGBoostやLightGBMを試す |
| チューニング | 交差検証で過学習を防ぐ |
| 分析 | 重要特徴を視覚化し、ドメイン理解を深める |

---

## 🧩 4. まとめ（学びの構造）

```
データ理解 → 前処理 → 特徴量設計 → モデル構築 → 改善 → 提出
```

Titanicは単なる「生存予測」ではなく、
- **前処理の重要性**
- **特徴量エンジニアリングの創造性**
- **モデル選定・チューニング**
を体系的に学べる最高の教材です。
