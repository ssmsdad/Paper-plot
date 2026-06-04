# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

font = {'family': 'Times New Roman', }
matplotlib.rc("font", **font)
# ================== 数据 ==================
datasets = ['Gowalla', 'Beauty', 'Yelp']
models = ['DirectAU', 'GraphAU', 'MAWU', 'LightGCN', 'RAU']

Gowalla_memory = [918, 918, 2648, 668, 918]
Beauty_memory = [444, 444, 520, 364, 444]
Yelp_memory = [970, 970, 2698, 730, 970]

memory = np.array([
    Gowalla_memory,
    Yelp_memory,
    Beauty_memory
])

# ================== 配色 ==================
colors = [
    "#4697DE",
    '#F2A65A',
    "#4FA345",
    '#E07B7B',
    '#B999D2'
]

# ================== 字体 ==================
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 18,
    'axes.labelsize': 16,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14
})

# ================== 画图 ==================
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)  # 👈 加宽画布

x = np.arange(len(datasets))
width = 0.18   # 👈 减小柱宽（关键！原来0.15）

for i, model in enumerate(models):
    bars = ax.bar(
        x + (i - 2) * width,
        memory[:, i],
        width=width,
        color=colors[i],
        edgecolor='black',
        linewidth=1.2,
        label=model
    )

    # ================== 数值标注 ==================
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2,
                height + 40,
                f'{int(height)}',
                ha='center', va='bottom',
                fontsize=13)   # 👈 略微缩小字体（14 → 11）

# ================== 坐标轴 ==================
ax.set_xticks(x)
ax.set_xticklabels(datasets)

ax.set_xlabel('Datasets')
ax.set_ylabel('GPU Memory Consumption (MB)')

# ================== 图例 ==================
ax.legend(title='Models', loc='upper right')

# ================== 网格 ==================
ax.grid(axis='y', linestyle='--', alpha=0.3)

# ================== Y轴 ==================
ax.set_ylim(0, 3000)

# ================== 去边框 ==================
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('GPU_memory_grouped_fixed.pdf', dpi=300)
# plt.show()