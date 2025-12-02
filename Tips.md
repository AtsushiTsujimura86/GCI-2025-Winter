##  特徴量の要素が占める割合を見る
```python
drafted_percentage = train['Drafted'].value_counts(normalize=True) * 100

print(f"Percentage of 0: {drafted_percentage.get(0, 0):.2f}%")
print(f"Percentage of 1: {drafted_percentage.get(1, 0):.2f}%")
```
value_counts()で、それぞれの要素が何回登場するかがわかる。normalize=Trueとすることで、何回登場したかではなく、全体に占める割合がわかる。

## ユニーク数（カテゴリデータの要素の種類）
``` python
# 同じ意味
len(df[cat].unique())
df[cat].nunique()
```

## seabornでもsubplot
```python
# カラムごとの平均Drafted、率と数
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
# YearごとのDrafted率
mean_drafted_year = train.groupby("Age")["Drafted"].mean().reset_index()
sns.barplot(data=mean_drafted_year, x="Age", y="Drafted", ax=axes[0])

# YearごとのDrafted人数
count_drafted_year = train.groupby("Age")["Drafted"].sum().reset_index()
sns.barplot(data=count_drafted_year, x="Age", y="Drafted", ax=axes[1])

plt.tight_layout()
plt.show()
```
<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/2829b8db-1507-48bc-b141-816bb6153465" />
