# 手法とその結果

## 1回目 0.772
basic,ipynbのやつ
### 前処理
- Name, Ticket, PassangerIDを除外
- Cabin, Embarkedを最頻値で補完
- Age, Fareを中央値で補完
- Sex, Cabin, EmbarkedをLabelEncoderでラベルエンコーディング
### モデル作成
- 学習用データを学習用データとvalidデータに7:3に分割
- ランダムフォレストで学習( n_estimators=100, max_depth=5, random_state=2025)
### 特徴量エンジニアリング
- 「SibSp」と「Parch」から「家族の人数」を作る  
- 「SibSp」と「Parch」から「一人で乗船したかどうか」を作る

## 2回目 0.769
### 前処理
- Name, Ticket, PassangerIDを除外
- Age, Fareを中央値で補完
- Cabin, Embarkedを最頻値で補完
  (Cabinは頭文字だけを抽出している C123 -> C)
- Sex, Cabin, EmbarkedをLabelEncoderでラベルエンコーディング
- ### モデル作成
- 学習用データを学習用データとvalidデータに8:2に分割
- ランダムフォレストで学習(n_estimators=100, max_depth=None, random_state=42)

### 変更点：
- 学習データ分割を 7:3 → 8:2 に変更
- random_stateを 2025 → 42 に変更
- max_depthを 5 → None に変更（木の深さ制限を解除）
- Cabinの前処理を追加（頭文字抽出）

### 考察：
- max_depthを解除したが精度はほぼ変化なし。過学習の可能性は低い。
- 分割を8:2にしたことで検証データが少なくなり、スコアが安定したかもしれない。
- Cabinの頭文字抽出は効果が薄い可能性。


## 3回目   79.7
### 前処理
- Name, Ticket, PassangerIDを除外
- Age, Fareを中央値で補完
- Cabin, Embarkedを最頻値で補完
  (Cabinは頭文字だけを抽出している C123 -> C)
- Sex, Cabin, EmbarkedをLabelEncoderでラベルエンコーディング
- Fareをlog変換で上書き ⇒ 右偏対策
- Age × Sex の特徴量追加 ⇒ 高齢の男性ほど死にやすいを反映
- ### モデル作成
- 学習用データを学習用データとvalidデータに8:2に分割
- ランダムフォレストで学習( n_estimators=200,  max_depth=5, random_state=43)
  <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/d0e30713-e19e-4ef0-809b-6ca82ca73a74" />

### 変更点：
1. **Fareをlog変換に変更**  
   - 外れ値の影響を抑え、料金分布を圧縮してモデルの安定性を向上。
2. **Age × Sex の特徴量を追加**  
   - 「男性の高齢者ほど死亡しやすい」というTitanic特有の非線形関係を1つの特徴量で表現。

### 考察：
- **Fareのlog変換**により、右に大きく偏った分布が滑らかになり、モデルが高額チケットの影響を適切に扱えるようになった。  
- **Age × Sex** の追加が大きく寄与。Titanicデータの本質である「女性と子供は優先的に救助」「特に高齢男性は生存率が低い」という構造を1本の特徴量で捉えることができたため、木の分岐精度が向上した。  
- **Cabinの圧縮処理**により、元の膨大で欠損だらけのカテゴリを整理でき、Deck階層という有効情報だけを活かせた。  
- 過学習を防ぐために **max_depth を浅めに設定**したことで、validスコアとLBスコアが安定し、汎化性能が改善された。  
- 全体として、今回の改善は「ノイズ除去」と「本質的相互作用の抽出」に寄与し、LB79.7% までスコアが向上したと考えられる。

## 4回目
### 前処理
- Name, Ticket, PassangerIDを除外
- Age, Fareを中央値で補完
- Cabin, Embarkedを最頻値で補完
  (Cabinは頭文字だけを抽出している C123 -> C)
- Sex, Cabin, EmbarkedをLabelEncoderでラベルエンコーディング
- Fareをlog変換で上書き ⇒ 右偏対策
- Age × Sex の特徴量追加 ⇒ 高齢の男性ほど死にやすいを反映
- ### モデル作成
- 学習用データを学習用データとvalidデータに8:2に分割
- ランダムフォレストで学習( n_estimators=200,  max_depth=5, random_state=43)
  <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/d0e30713-e19e-4ef0-809b-6ca82ca73a74" />

### 変更点：
1. 

### 考察：
- **Fareのlog変換**により、右に大きく偏った分布が滑らかになり、モデルが高額チケットの影響を適切に扱えるようになった。  
- **Age × Sex** の追加が大きく寄与。Titanicデータの本質である「女性と子供は優先的に救助」「特に高齢男性は生存率が低い」という構造を1本の特徴量で捉えることができたため、木の分岐精度が向上した。  
- **Cabinの圧縮処理**により、元の膨大で欠損だらけのカテゴリを整理でき、Deck階層という有効情報だけを活かせた。  
- 過学習を防ぐために **max_depth を浅めに設定**したことで、validスコアとLBスコアが安定し、汎化性能が改善された。  
- 全体として、今回の改善は「ノイズ除去」と「本質的相互作用の抽出」に寄与し、LB79.7% までスコアが向上したと考えられる。


