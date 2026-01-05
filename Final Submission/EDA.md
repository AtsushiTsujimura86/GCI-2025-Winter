# EDA
## W社の人事データ
- カラム数：44
- データ数：1470
- 欠損値無し


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
  - 0  
  - 1  
  - 2  
  - 3  
  - 4  
  - 5  

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

  
