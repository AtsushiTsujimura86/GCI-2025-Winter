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
