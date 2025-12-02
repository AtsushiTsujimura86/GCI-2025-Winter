# コンペ２

**AUC（Area Under the ROC Curve）＝  
「Drafted(1) を Not Drafted(0) より高い確率で予測できた割合」**
---
## 例
### ● 良い予測（成功 = 1点）
正解：
- A = 1  
- B = 0  

予測：
- A：**0.8**  
- B：0.3  

👉 1のA > 0のB → **成功（1点）**

---

### ● 悪い予測（失敗 = 0点）
正解：
- A = 1  
- B = 0  

予測：
- A：0.4  
- B：**0.7**  

👉 0のBが高い → **失敗（0点）**
---
これを「1の選手 × 0の選手」の全組み合わせで計算し、  
成功率（0〜1）にしたものが **AUC**。

## 前処理
### １．ユニーク数が少ないカテゴリ(Position / Position_Type / Player_Type)
  **ユニーク数が少ない＆情報力が高い**  ⇒  PandasのCategory型に変換するだけ(LightGBMがカテゴリ変数として扱ってくれる)

### ２. ユニーク数が多いカテゴリ(School)
- ユニーク数：236（多すぎ）
- one-hot：不可能
- しかし Drafted の分布に大きく関係する超重要特徴  
⇒ この1列だけ**Target Encoding を行う**

### Target Encodingとは？
カテゴリを、**そのカテゴリの目的変数の平均値に変換する**手法  
```
例：
Alabama: 0.82(Alabama大学に所属している選手のDraftedの平均値)
無名大学: 0.1
```
#### Target Encodingを使う理由（今回の場合）
- School が多すぎる（236種類）
- one-hot → 236列 → 過学習・次元爆発
- label encoding → 数字の大小に意味がない（無意味）  
⇒ School → Drafted に関連深いのに、そのままじゃ使いづらい！

### コード例
``` python
# 学校ごとのDrafted平均値
school_mean = train.groupby("School")["Drafted"].mean()

# trainに適用
train["School_TE"] = train["School"].map(school_mean)

# testに適用
# test側に未知の学校が出る可能性があるので、平均で埋める
global_mean = train["Drafted"].mean()
test["School_TE"] = test["School"].map(school_mean).fillna(global_mean)

# School列は LightGBM に入れないので削除 or category化
train.drop(columns=["School"], inplace=True)
test.drop(columns=["School"], inplace=True)
```
####  school_mean
`train.groupby("School")["Drafted"].mean()`  
を実行すると、実質的に **辞書のような mapping table** ができる。形式は Series だが、本質は
```
A → 0.30  
B → 0.90  
C → 0.10  
D → 0.50
```
という対応関係で辞書みたいなかんじ。

#### train["School_TE"] 
`train["School"].map(school_mean)`では、trainのSchool列の各大学名に対応するschool_mean(Draftedの平均値)を当てはめている


### map の動作：値ベースの置換を行う
`map` は **行の順番には関係なく、値そのものをキーにして置換**する。


## 4. map と apply の違い
| メソッド | できること | 特徴 |
|---------|------------|--------|
| **map** | 1つの値を1つの値に置換 | 辞書置換に最適・高速(Cレベル) |
| **apply** | 複雑な処理（if、正規表現など） | mapより遅い、lambdaと併用 |

今回ののmapをapplyで書くと、
`train["School"].apply(lambda x: school_mean(x))`で書けるがかなり遅い

Target Encoding は「値の置換」なので **map が最適**
---




## 使用モデル
✔ 方針1：LightGBM を主力モデルにするべき  
理由：  
1. 欠損が多い → 自動処理神
2. 数値が強い → 木モデルと相性最高
3. カテゴリも category 型で食える
4. 多重共線性を気にしなくていい（理由ではなく性質ね）

### パラメータ

### optuna
optunaとは？： **自動でLGBMの最適パラメータを見つける手法**  
- パラメータをランダムに提案し、そのパラメータでLGBMをKFoldで学習 ⇒ AUC計算  
- 単にランダムにパラメータを決定しているわけではなく、過去の良いパラメータの傾向を学習しながらより良い探索をしている。
これで算出されたパラメータをそのままモデルのパラメータとして使えばよい。
