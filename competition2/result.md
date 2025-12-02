# モデル構築ログ（NFL Draft Prediction）

##  提出 No.1：LightGBM ベースライン
**提出ファイル**：`submission_baseline.csv`  
**モデル**：LightGBM（単一モデル）  
**評価指標**：AUC（Validation）

### 📌 今回やったこと
- School に Target Encoding を適用  
- Position / Position_Type / Player_Type を category 型に変換  
- 数値特徴量は LightGBM にそのまま投入  
- 欠損値処理は LightGBM に任せる（内部処理）  
- train/val（80/20）分割で学習  
- LightGBM ベースラインモデルで推論 → test に確率を出力  
- sample_submission の形式に合わせて提出ファイルを作成

### 🏆 結果
- **Validation AUC：0.8110**
- **Public LB：0.80321**

### 🔍 気づき・メモ
- School の TE が強く効いている  
- 身体能力系の特徴量は Drafted と綺麗に差がある  
- ベースラインでもそこそこ高いAUCを記録  
- ここからは「特徴量追加」「LGBMチューニング」で伸ばせそう

---

### 📝 今後の改善候補
- LightGBM のハイパーパラメータ調整  
- 身体能力の組み合わせ特徴量追加（40yd × Weight など）  
- Position ごとのTE  
- seed アンサンブル（複数モデルの平均化）  
- KFold による安定化

---

## 提出No.2

### 今回したこと
今回はEDA、特にカラム間の相関を見ながら特徴量の調整をした。

### 🏆 結果
- **Validation AUC：0.8199(向上)**
- **Public LB：0.79943（悪化）**

### 特徴量エンジニアリング
- BMIを追加
- Speedを追加

###  特徴量削除
- Id
- Year
- Height

### Feature Importance
順位（Gain）を見ると：
1. Age  
2. School_TE  
3. Agility_3cone  
4. Weight  
5. Sprint_40yd  
6. BMI  
7. Bench, Vertical, Shuttle, Broad  
8. Speed  
9. Position, Player_Type  
10. Position_Type（0）

### 高性能LightGBMで学習
今回のパラメータ：

- n_estimators=2000  
- learning_rate=0.03  
- num_leaves=128  
- max_depth=10  
- min_data_in_leaf=30  
- feature_fraction=0.8  
- bagging_fraction=0.7  
- lambda_l1=1.0, lambda_l2=1.0  

→ **高次非線形を学習する強力設定**

---

### 4. 今回の反省点

#### ① パラメータが強すぎてローカルに過学習

- num_leaves が128 → データ量の割に複雑すぎ
- n_estimators 2000 → 過学習のリスク上昇
- 一見改善しているが、汎化性能は落ちた

#### ② Position（ポジション）を活かせていない
- Position は本来 NFL で重要
- One-hot でなく **Target Encoding** が適切
- 今回はまだ導入していないため情報損失

#### ③ データ分割が1回のみ（train/val）
- StratifiedKFold がないためバリデーションが偏る
- 今回のバリデーションは運が良かった可能性がある

#### ④ 身体能力の複合特徴量が不足
- JumpPower, Explosion, StrengthScore などを試す前
- Speed だけでは情報が足りない

---

### 5. 次回の改善方針（重要度順）

#### ① Position の Target Encoding（最優先）
- Drafted と Position は深い関係がある
- School_TE と同じく安定して効く

#### ② LightGBM を「軽いパラメータ」に戻す
- num_leaves：31〜64  
- n_estimators：300〜800  
- feature_fraction：0.8  
- bagging_fraction：0.7  

#### ③ StratifiedKFold（5-fold）導入
- AUCの安定化
- LB との一貫性が向上する

#### ④ 特徴量を絞って強いものだけ残す
- Speed / BMI / School_TE / Age / Sprint / Agility / Weight  
→ NFL のドラフトではこの辺りが核

#### ⑤ 身体能力の複合指標を厳選して追加
- JumpPower（Vertical × Weight）
- Explosion（Broad × Weight）
- AgilityScore（Shuttle + 3cone）
- StrengthScore（Bench × Weight）

---

### 6. 今回の総評

- Validationは過去最高だった  
- LBは下がったが、これは「過学習 → 改善のサイン」
- EDA精度が飛躍的に上がり、特徴量の理解が深まった
- 次の改善方針が明確になったため、今回の回は非常に価値が高い

---

### 7. 次回やること（具体的行動）

1. Position を Target Encoding  
2. 特徴量を整理（本当に必要なものだけ残す）  
3. LightGBM を軽量パラメータにする  
4. StratifiedKFold（5-fold）を導入  
5. 本当に効く身体能力の複合特徴量だけ追加  
6. 再度 LB スコアを計測  

→ これで **LB 0.81〜0.83** は確実に狙える

