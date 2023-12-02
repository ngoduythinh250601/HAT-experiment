from matplotlib import pyplot as plt
import pandas as pd

# Visualizing the data in DataFrame df with values on the bars
data = {
    'Players': ['Original', 'Patch-Mosaic', 'Perceptual Loss', 'MixLosses Loss'],
    'Goals': [0.7659, 0.7604, 0.5419, 0.7666]
}

df = pd.DataFrame(data)

plt.figure(figsize=[6, 4])
plt.ylim(0.3, 0.9)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

col_map = plt.get_cmap('tab20')

# Creating a bar chart from the DataFrame df
pl = plt.bar(df.Players, df.Goals, width=0.3, color=col_map.colors, zorder=3)

# Annotating each bar with its height (value)
for bar in pl:
    plt.annotate(f'{bar.get_height():.4f}',  # Format the value to two decimal places
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom',
                 fontsize=12, color='black')
    
plt.grid(axis='y', color = 'black', linestyle = '-', zorder=2)
plt.title('x8 SR on Manga109', fontsize=24)
plt.ylabel("SSIM scores", fontsize=12)

plt.show()
