# EDA
## W社の人事データ
- カラム数：44
- データ数：1470
- 欠損値無し

## 打ち手となる変数を絞る
- **目的変数：attrition（退職したかどうか）、これは確定でよい**

以下では打ち手視点でカラムをグループ化する。

### 1. 個人属性（基本属性）

従業員個人の属性を表す特徴量群。  
企業側が直接変更・介入することは難しいが、  
**離職傾向の把握やセグメント分析の基礎情報**として重要。

- Age  
  年齢

- Gender  
  性別

- Education  
  最終学歴レベル

- EducationField  
  専攻分野

- MaritalStatus  
  婚姻状況 (議論の余地あり、結婚したから退職するという可能性もあり、産後に復帰を許容)

- DistanceFromHome  
  自宅から職場までの距離

---

### 2. キャリア・評価（施策に使える）

従業員のキャリア段階や評価状況に関する特徴量群。  
配置転換、評価制度の見直し、育成施策など  
**企業側が直接介入可能な施策**に結びつけやすい。

- JobLevel  
  職位レベル（数値が大きいほど上位職）

- JobRole  
  職種（研究職、営業職、管理職など）

- PerformanceIndex  
  生産性を数値化した指標（100点満点）

- PerformanceRating  
  人事評価による業績評価（Low〜Outstanding）

- YearsSinceLastPromotion  
  前回昇進からの経過年数

- YearsAtCompany  
  勤続年数

---

### 3. ストレス・満足度（最重要）

従業員の心理状態や職場に対する満足度を表す特徴量群。  
離職との関連が強く、**事業提案の主軸になりやすい領域**。

- StressRating  
  上司・人事・産業医などによる客観的ストレス評価

- StressSelfReported  
  本人申告によるストレス評価

- JobSatisfaction  
  業務内容に対する満足度

- EnvironmentSatisfaction  
  職場環境に対する満足度

- RelationshipSatisfaction  
  上司・同僚との人間関係満足度

- WorkLifeBalance  
  仕事と私生活のバランス評価

- OverTime  
  残業時間・残業負荷を示す指標

---

### 4. 制度利用（打ち手そのもの）

企業が提供している制度・福利厚生の利用状況を示す特徴量群。  
**「制度が離職抑制に本当に効いているのか」を検証可能**であり、  
施策提案に直結する。

- RemoteWork  
  リモートワーク利用度

- FlexibleWork  
  フレックスタイム・時短勤務など柔軟な働き方制度の利用有無

- ExtendedLeave  
  育児休暇・産休・リフレッシュ休暇など長期休暇取得有無

- WelfareBenefits  
  福利厚生制度の利用頻度

- InHouseFacility  
  社内施設（ジム・カフェ等）の利用有無

- ExternalFacility  
  社外提携施設（語学学校等）の利用有無

  ---
  <br>

## 重要そうなカラムとattritionとの関係
対象： 'StressRating',
    'StressSelfReported',
    'JobSatisfaction',
    'WorkLifeBalance',
    'RemoteWork'
### StressRating
<img width="759" height="458" alt="image" src="https://github.com/user-attachments/assets/d85b199c-d1fd-4d71-beca-5c3cb947ebf6" />

#### 在職者（Attrition = No）
- StressRating = 2, 3 が 約81%
- StressRating = 4, 5 は 約8%
#### 離職者（Attrition = Yes）
- StressRating = 2, 3 が 約58%
- StressRating = 4, 5 が 約31%
#### 考察
在職者はstressratingが2,3が81％をしめ、おおむねストレスは少なく働けている。また、離職者は4,5が31％を占め、在職者の8パーセントに比べてストレスを感じている割合が多いことがうかがえる。
このことから、離職者は在職者よりもストレスを感じ、離職していったのではないかと推測できる。


### StressSelfReported
<img width="742" height="451" alt="image" src="https://github.com/user-attachments/assets/239e5850-6aa2-4a5c-958e-8fbb4b97887a" />

#### 考察
StressSelfReported は Attrition との直接的な関係は弱かった。
一方で、StressRating では離職者において高ストレス層の割合が高く、
自己申告と客観評価の乖離が存在する可能性が示唆された。
これは、従業員がストレスを正確に申告できていない、
あるいは組織内で申告しにくい風土が存在する可能性を示す。

#### StressGap の導入と結果・考察

StressRating（客観評価）と StressSelfReported（自己申告）の差分として  
**StressGap = StressRating − StressSelfReported** を定義し、  
自己認識と客観評価の乖離に着目した分析を行った。

分析の結果、StressGap が大きい従業員（StressGap ≥ 2）では、  
離職率が約30%と、乖離が小さい従業員（約15%）と比較して  
**約2倍高い**ことが確認された。

また、Attrition 別の分布を比較すると、離職者では  
正の StressGap（客観評価の方が高い）が相対的に多く、  
本人が自覚・申告していない高ストレス状態が  
離職リスクと関連している可能性が示唆された。

この結果から、自己申告に依存したストレス把握には限界があり、  
客観評価との乖離を考慮した従業員モニタリングや  
早期介入施策の必要性が示された。

| HighStressGap | Attrition = No (%) | Attrition = Yes (%) |
|--------------|-------------------:|--------------------:|
| 0            | 85.29              | 14.71               |
| 1            | 70.14              | 29.86               |

| HighStressGap | Attrition = No (%) | Attrition = Yes (%) |
|--------------|-------------------:|--------------------:|
| 0            | 91.80              | 81.93               |
| 1            | 8.20               | 18.07               |


<img width="770" height="452" alt="image" src="https://github.com/user-attachments/assets/1b800a7f-b7bb-4b0d-80e6-1280974a81b1" />


### JobSatisfaction
<img width="997" height="546" alt="image" src="https://github.com/user-attachments/assets/2c7b9bc6-be2d-4396-97f6-53b0eccbdfd0" />

### WorkLifeBalance
<img width="912" height="547" alt="image" src="https://github.com/user-attachments/assets/e2409025-99e0-42f5-99ef-1b4d1a50fbb4" />

WorkLifeBalance と Attrition の関係を構成比で比較したところ、両者の分布に大きな差は見られなかった。このことから、WorkLifeBalance 単体では離職を強く説明する要因にはなっていない可能性が示唆される。
一方で、分布が全体的に「Better（3）」に集中していることから、ワークライフバランス施策自体は一定程度浸透しており、離職要因としては他の要素（ストレスの認識ギャップや評価要因）がより重要である可能性が考えられる。

### RemoteWork
<img width="949" height="537" alt="image" src="https://github.com/user-attachments/assets/7afd7e84-9e9c-4580-91bd-10bb598ba00c" />

<img width="672" height="411" alt="image" src="https://github.com/user-attachments/assets/d32f7804-ad18-4b7d-9686-65f00212f823" />


RemoteWork と Attrition の関係を構成比で比較したところ、リモートワーク利用度が低い従業員では離職割合が高く、一方で利用度が高い層では在職割合が高い傾向が確認された。このことから、主観的な WorkLifeBalance 評価よりも、
具体的な働き方制度の利用状況の方が、離職行動により直接的な影響を与えている可能性が示唆される。


### Age
<img width="283" height="320" alt="image" src="https://github.com/user-attachments/assets/7201e6e5-e683-4c78-ab45-06ccf4f69a82" />

<img width="945" height="437" alt="image" src="https://github.com/user-attachments/assets/6ae4062c-24b5-4337-994d-151e9e2942ab" />

年代別に離職率を算出した結果、18–24歳および25–29歳において離職率が他年代と比較して顕著に高いことが確認された。特に18–24歳では約4割が離職しており、キャリア初期層における定着がW社の固有課題であると考えられる。一方で30代後半から40代にかけては離職率が10%前後で安定しており、
全社一律施策よりも、若年層に焦点を当てた施策の方が効果的である可能性が示唆された。

#### AgeGroupの分布
<img width="692" height="490" alt="image" src="https://github.com/user-attachments/assets/a93add44-3dd1-46d5-bff5-88fb625287d7" />


### AgeGroupごとのHowToEmploy
<img width="801" height="437" alt="image" src="https://github.com/user-attachments/assets/ea3c96e8-8311-4d43-b2d0-4927a36764fd" />

年代ごとに差はほとんどない。

### AgeGroupごとのRemoteWork
<img width="862" height="417" alt="image" src="https://github.com/user-attachments/assets/8776179a-d3cc-472d-b37a-cd2bb3c8d337" />


### AgeGroup * RemoteWork ごとの離職率

<img width="925" height="438" alt="image" src="https://github.com/user-attachments/assets/3071511f-76a7-40ee-a84c-d7be361e907e" />


### HowToEmployごとのAttrition率
<img width="813" height="592" alt="image" src="https://github.com/user-attachments/assets/a996562f-557e-43be-8a25-672beca9ca2e" />

いずれの雇用方法でも、離職率に差はほとんどなく20%程

### 在籍年数別離職率
<img width="917" height="437" alt="image" src="https://github.com/user-attachments/assets/4c59c6f9-340e-44f4-bbbd-875c2f6fb311" />

<img width="928" height="441" alt="image" src="https://github.com/user-attachments/assets/a33fa897-cb23-495b-99df-d1b120d861e2" />

### 通勤距離ごとのリモートワーク構成
<img width="906" height="438" alt="image" src="https://github.com/user-attachments/assets/30d66add-ec8c-4867-bd02-9fea91a1e38d" />

---

### 職種別インセンティブ

<img width="411" height="384" alt="image" src="https://github.com/user-attachments/assets/2d33e44f-f9a7-44b1-abd3-47c7cfd51484" />
<img width="1163" height="426" alt="image" src="https://github.com/user-attachments/assets/2d6a5299-2cc6-4b16-95f0-08f52e40f778" />
<img width="1105" height="441" alt="image" src="https://github.com/user-attachments/assets/ce846031-ec3b-4f10-933e-444797d84982" />

考察：職種別に分析した結果、Sales Representative およびLaboratory Technician において離職率が高く、かつ離職者のインセンティブ水準が非離職者と比較して低い傾向が確認された。一方、Manager や Research Director では
インセンティブ水準が高く、離職率も低いことから、職種によって評価・報酬制度の機能度に差がある可能性が示唆される。







## データセットのカラム一覧（ユニーク値整理版）

- Age（年齢）、int  
  - 値：18〜60（※ユニーク値多数のため省略）

- Attrition（離職の有無）、object  
  - Yes：離職  
  - No：在職  

- BusinessTravel（出張頻度）、object  
  - Travel_Rarely  
  - Travel_Frequently  
  - Non-Travel  

- Department（所属部署）、object  
  - Sales  
  - Research & Development  
  - Human Resources  

- DistanceFromHome（自宅から職場までの距離）、int  
  - 値：1〜29（※ユニーク値多数のため省略）

- Education（最終学歴レベル）、int  
  - 1: Below College  
  - 2: College  
  - 3: Bachelor  
  - 4: Master  
  - 5: Doctor  

- EducationField（専攻分野）、object  
  - Life Sciences  
  - Medical  
  - Marketing  
  - Technical Degree  
  - Human Resources  
  - Other  

- EmployeeCount（従業員数）、int  
  - 1（全従業員で固定値）

- EmployeeNumber（従業員ID）、int  
  - 値：1〜2068（※識別子のため省略）

- EnvironmentSatisfaction（職場環境満足度）、int  
  - 1: Low  
  - 2: Medium  
  - 3: High  
  - 4: Very High  

- Gender（性別）、object  
  - Male  
  - Female  

- PerformanceIndex（生産性指標スコア）、int  
  - 値：30〜100（※ユニーク値多数のため省略）

- JobInvolvement（仕事への関与度）、int  
  - 1: Low  
  - 2: Medium  
  - 3: High  
  - 4: Very High  

- JobLevel（職位レベル）、int  
  - 1  
  - 2  
  - 3  
  - 4  
  - 5  

- JobRole（職種）、object  
  - Sales Executive  
  - Sales Representative  
  - Research Scientist  
  - Research Director  
  - Laboratory Technician  
  - Manufacturing Director  
  - Healthcare Representative  
  - Manager  
  - Human Resources  

- JobSatisfaction（業務満足度）、int  
  - 1: Low  
  - 2: Medium  
  - 3: High  
  - 4: Very High  

- MaritalStatus（婚姻状況）、object  
  - Single  
  - Married  
  - Divorced  

- MonthlyAchievement（月次業績指標）、int  
  - 値：多数（※ユニーク値が非常に多いため省略）

- NumCompaniesWorked（これまでに勤めた企業数）、int  
  - 0  
  - 1  
  - 2  
  - 3  
  - 4  
  - 5  
  - 6  
  - 7  
  - 8  
  - 9  

- Over18（18歳以上かどうか）、object  
  - Y  

- OverTime（残業時間・残業負荷指標）、int  
  - 値：0〜61（※ユニーク値多数のため省略）

- PerformanceRating（人事評価スコア）、int  
  - 1: Low  
  - 2: Good  
  - 3: Excellent  
  - 4: Outstanding  

- RelationshipSatisfaction（人間関係満足度）、int  
  - 1: Low  
  - 2: Medium  
  - 3: High  
  - 4: Very High  

- StandardHours（標準労働時間）、int  
  - 40（全従業員で固定値）

- StockOptionLevel（ストックオプション付与レベル）、int  
  - 0  
  - 1  
  - 2  
  - 3  

- TotalWorkingYears（総就業年数）、int  
  - 値：0〜40（※ユニーク値多数のため省略）

- TrainingTimesLastYear（前年の研修受講回数）、int  
  - 0  
  - 1  
  - 2  
  - 3  
  - 4  
  - 5  
  - 6  

- WorkLifeBalance（ワークライフバランス評価）、int  
  - 1: Bad  
  - 2: Good  
  - 3: Better  
  - 4: Best  

- YearsAtCompany（勤続年数）、int  
  - 値：0〜40（※ユニーク値多数のため省略）

- YearsInCurrentRole（現職務での年数）、int  
  - 値：0〜18（※ユニーク値多数のため省略）

- YearsSinceLastPromotion（前回昇進からの年数）、int  
  - 0  
  - 1  
  - 2  
  - 3  
  - 4  
  - 5  
  - 6  
  - 7  
  - 8  
  - 9  
  - 10  
  - 11  
  - 12  
  - 13  
  - 14  
  - 15  

- YearsWithCurrManager（現上司との勤務年数）、int  
  - 値：0〜17（※ユニーク値多数のため省略）

- HowToEmploy（採用・雇用形態）、object  
  - intern  
  - New_graduate_recruitment  
  - direct_recruiting  
  - agent_A  
  - agent_B  
  - agent_C  

- Incentive（成果連動インセンティブ金額）、int  
  - 値：多数（※ユニーク値が非常に多いため省略）

- RemoteWork（リモートワーク形態）、int  
  - 0  : on-site-work
  - 1  
  - 2  
  - 3  
  - 4  
  - 5  : full remote

- MonthlyIncome（月収）、int  
  - 値：多数（※ユニーク値が多いため省略）

- StressRating（上司・人事によるストレス評価）、int  
  - 1: Very Low  
  - 2: Low  
  - 3: Average  
  - 4: High  
  - 5: Very High  

- WelfareBenefits（福利厚生利用頻度）、int  
  - 1: Rarely Used  
  - 2  
  - 3  
  - 4: Very Frequently Used  

- InHouseFacility（社内施設利用有無）、int  
  - 0: No  
  - 1: Yes  

- ExternalFacility（社外提携施設利用有無）、int  
  - 0: No  
  - 1: Yes  

- ExtendedLeave（長期休暇取得有無）、int  
  - 0: No  
  - 1: Yes  

- FlexibleWork（柔軟な働き方制度利用有無）、int  
  - 0: No  
  - 1: Yes  

- StressSelfReported（自己申告ストレス評価）、int  
  - 1: Very Low  
  - 2  
  - 3: Average  
  - 4  
  - 5: Very High  

- Year（データ取得年）、int  
  - 2023  
  - 2024  

  
