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


## No.4 LB 0.81351 モデル（コード版の記録）

### 1. 使用した LightGBM パラメータ
```python
best_params = {
    "objective": "binary",
    "boosting_type": "gbdt",
    "learning_rate": 0.0864,
    "num_leaves": 56,
    "max_depth": 3,
    "min_data_in_leaf": 42,
    "feature_fraction": 0.6605,
    "bagging_fraction": 0.8603,
    "bagging_freq": 4,
    "lambda_l1": 2.7769,
    "lambda_l2": 3.6208,
    "n_estimators": 3000,
    "random_state": 42,
    "n_jobs": -1,
}
```

### 2. 使用した特徴量
- `Position_TE`（リークあり TE）
- `School_TE`（リークあり TE）
- `Speed = 1 / Sprint_40yd`
- `Power1 = Weight * Bench_Press_Reps`
- `Jump = Vertical_Jump * Weight`
- その他元データ（Height, Weight など）

### 3. 前処理
- `Position` を drop
- `School` を drop
- `Id`, `Year`, `Height` を drop（※この時点ではここはあまり効いてない）
- 特徴量の欠損処理はなし（データが綺麗なので）

### 4. 学習方法（KFold）
- StratifiedKFold(n_splits=5, shuffle=True)
- fold ごとに：
  - model.fit(..., eval_set=[(X_val, y_val)], eval_metric="auc")
  - early_stopping_round = 100
  - OOF に予測を入れる
  - test へ平均予測

### 5. 結果
- **Final OOF AUC ≈ 0.857〜0.858（リークにより高かった）**
- **LB（public leaderboard）：0.81351**

### 6. 提出ファイル
- 保存名：`lgbm_kfold_optuna_submission.csv`

### 7. Feature Importance を出力
- gain/split を DataFrame 化
- 上位20項目をバー図で可視化

---

## コメント
- このモデルは「リークあり TE（train の平均を直接使用）」だったため、  
  OOF が高く出て **0.858 → LB 0.8135** と **乖離が大きかった**。
- それでも基準として強いモデルだったため、提出時点では妥当な成果。
- 

## コンペ2：LB 0.83777 モデル（KFold Target Encoding 版）

### 1. 前処理（リークなし設計）
- Position → **KFold Target Encoding（n_splits=5）**
- School → **KFold Target Encoding（n_splits=5）**
- TE 作成後、元の `Position`、`School` は drop
- `Id`, `Year`, `Height` を drop
- データ欠損は特になし

### 2. 特徴量
- **Speed = 1 / Sprint_40yd**
- **Power1 = Weight × Bench_Press_Reps**
- **Jump = Vertical_Jump × Weight**
- **Small_Speed = Speed × Height**
- 上位の複合特徴量（筋力×速度×敏捷性の組み合わせ）
- Position_Type, Player_Type は drop（重要度が低かったため）

※ すべて train/test に同じ処理

### 3. Target Encoding（リークなし）
- 5-fold の内側平均で train を TE
- test は train 全体の平均で TE
- 未知カテゴリは train の Drafted 平均で補完

### 4. モデル構築（KFold 5fold）
- StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
- fold ごとに LightGBM を学習
- **early_stopping_round = 100**
- test は 5fold の平均予測

### 5. LightGBM（Optuna 最適パラメータ）
```python
{
    "learning_rate": 0.06220723694105511,
    "num_leaves": 70,
    "max_depth": 2,
    "min_data_in_leaf": 81,
    "feature_fraction": 0.8765080382766045,
    "bagging_fraction": 0.6497808211165161,
    "bagging_freq": 5,
    "lambda_l1": 3.779858381614759,
    "lambda_l2": 4.98951267041534,
    "n_estimators": 3000,
    "objective": "binary",
    "boosting_type": "gbdt",
    "random_state": 42,
    "n_jobs": -1
}
```

### 6. 結果
- **Final OOF AUC：0.8365 前後**
- **LB（public leaderboard）：0.83777**
- → CV と LB の一致度が非常に高く、モデルが正しく評価されている状態

### 7. 提出ファイル
- **lgbm_final_kfold_optuna_v2_submission.csv**

### 8. 所感（簡潔）
- KFold Target Encoding でリークを完全に抑えたことで  
  OOF ≈ LB となり、信頼性の高いスコアに改善。
- 特徴量（Speed系, Power系, Small_Speed）が特に効果的。
- Optuna のパラメータ最適化もリークなしデータにフィットしており、安定した精度を実現。

<br>
--- 

## モデル構築コードまとめ（Frequency Encoding + Target Encoding + 多モデルスタッキング）

本ドキュメントは、今回構築したモデルパイプライン全体を整理したものである。  
コード本文は省略し、**各パートで何をしているか** を簡潔にまとめる。

---

## 1. データ読み込みと基本前処理
- Google Drive をマウントし、train/test を読み込む。
- `Year`, `Id`, `Player_Type`, `Position_Type` など学習不要な列を削除。
- train/test の形状を確認する。

---

## 2. Frequency Encoding（件数エンコーディング）
- `School` と `Position` の登場回数を特徴量として追加。
- これは Target Encoding とは異なる「カテゴリの人気度」を学習させることで、多様性を増やす狙いがある。
- 特に今回のデータでは頻度が非常に効きやすく、LGBM depth=3 の AUC を大幅に改善した。

---

## 3. Target Encoding（Leak-Free）
- `Position` と `School` に対して KFold を用いたリーク防止の Target Encoding を実施。
- smoothing=30（固定）で、カテゴリの平均 Draft 率を特徴量化。
- 最後に `Position` と `School` の元列を削除する。

---

## 4. 特徴量エンジニアリング
主に身体能力指標の相互作用や組み合わせを特徴量として追加。
- Speed（40yd の逆数）
- Speed × Weight, Speed × Height
- Position_TE × Speed
- 40yd と Height の差
- Shuttle / Weight
- Age と Speed の組み合わせ
- BenchPress / Age など

これらによって非線形関係をモデルが学習しやすくなる。

---

## 5. LightGBM（depth=1,3,5）
3種類の LightGBM モデルを学習。
- depth=1 → 決定 stump。Age など強い一次境界を高速に捉える。
- depth=3 → Frequency Encoding の効果で大幅に性能改善した。
- depth=5 → より複雑な境界を学習させ、多様性を確保。

3つの LGBM は互いに異なる構造の決定境界を持ち、スタッキング時に補完し合う。

---

## 6. CatBoost
- デフォルトでカテゴリに強いモデル。
- 今回は数値化済みデータなので、補完的モデルとして利用。
- 頻度特徴量＋TE との相性が良く、0.84 付近の安定した AUC を示した。

---

## 7. XGBoost
- 深い木構造と強い正則化により、LGBM とは異なる境界を学習。
- AUC は単体で最強ではないが、スタッキングで多様性を生み出す役割を持つ。

---

## 8. スタッキング（Logistic Regression）
- LGBM（1,3,5）、CatBoost、XGBoost の oof 予測を縦に結合して学習。
- Meta モデルとしてロジスティック回帰を採用。
- 各モデルの強みを適切に重み付けでき、最終 AUC は **0.8439** を達成。

---

## 9. Submission 生成
- meta モデルの test 予測を CSV に書き出し、提出形式に整える。

---

## まとめ
本パイプラインの構成要点は以下の通り。

1. **Frequency Encoding** によりカテゴリの「人気度」を明示し、LGBM depth=3 の性能が劇的に改善した。  
2. **Leak-Free Target Encoding** により School/Position の Draft 傾向を安定的に表現。  
3. **複数の LGBM（depth違い）＋ CatBoost ＋ XGBoost** により決定境界の多様性を最大化。  
4. **ロジスティック回帰スタッキング** によって、モデルの強みを適切に統合。  
5. 最終的に **Stacking AUC ≈ 0.844** と、十分競争力のある水準に到達。

改善余地としては、**Target Encoding の smoothing 最適化** や  
**相互作用特徴量の自動生成** が挙げられるが、現状でも安定した高スコアが期待できる構成となっている。




