import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#code to get inbult dataset names from seaborn
print(sns.get_dataset_names())

#loading
tips = sns.load_dataset('tips')
print(tips.head())

#scatterplot
print(sns.scatterplot(data = tips, x = "total_bill", y = 'tip', palette = "deep", size = 'size', hue = 'time'))
plt.title(" Bill vs Tip")
plt.show()

#lineplot
print(sns.lineplot(data = tips, hue = 'sex', palette = 'deep', x = 'size', y = 'total_bill'))
plt.title("Female_bill vs Male_bill")
plt.show()