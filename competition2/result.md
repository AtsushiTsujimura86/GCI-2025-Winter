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

# 🏷 次回提出予定（No.2）
（例：LightGBM パラメータ調整版 / 特徴量増強版 / KFold版）
ここに次に何をするかを書く。

### 🏆 結果
- **Validation AUC：0.8199**
- **Public LB：0.80321**
