import seaborn as sns 
import matplotlib.pyplot as plt
df = sns.load_dataset("penguins")

sns.scatterplot(data=df, x="flipper_length_mm", y="bill_length_mm", hue="species")
plt.show()