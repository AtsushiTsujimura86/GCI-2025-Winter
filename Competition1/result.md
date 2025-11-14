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

