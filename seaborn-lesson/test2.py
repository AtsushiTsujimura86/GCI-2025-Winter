import matplotlib.pyplot as plt
import seaborn as sns

# データ読み込み
penguins = sns.load_dataset("penguins")

# 種類ごとに色を手動で定義
species_list = penguins["species"].unique()
colors = ["red", "green", "blue"]  # 自分で決める

plt.figure(figsize=(7, 5))

for species, color in zip(species_list, colors):
    sub = penguins[penguins["species"] == species]
    plt.scatter(sub["bill_length_mm"],
                sub["bill_depth_mm"],
                color=color,
                label=species)

plt.xlabel("bill_length_mm")
plt.ylabel("bill_depth_mm")
plt.legend(title="species")
plt.show()
