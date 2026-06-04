import numpy as np
import matplotlib.pyplot as plt

# 设置数据
datasets = ['Alibaba', 'Amazon', 'Yelp2018']
methods = ['POMNS', '-NO', '-HM']
metrics = ['Recall@20', 'NDCG@20']

# 真实数据
data = {
    'Alibaba': {
        'Recall@20': [0.0854, 0.0642, 0.0443],
        'NDCG@20': [0.0401, 0.0310, 0.0231],
    },
    'Amazon': {
        'Recall@20': [0.0491, 0.0412, 0.0321],
        'NDCG@20': [0.0261, 0.0201, 0.0143],
    },
    'Yelp2018': {
        'Recall@20': [0.0726, 0.0689, 0.0493],
        'NDCG@20': [0.0598, 0.0504, 0.0336],
    }
}

# 设置全局样式
plt.style.use('classic')
plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 20,
    'axes.titlesize': 25,
    'axes.labelsize': 25,
    'xtick.labelsize': 25,
    'ytick.labelsize': 25,
    'legend.fontsize': 25,
    'axes.linewidth': 1,
    'axes.edgecolor': 'black',
    'grid.color': 'black',
    'grid.linestyle': '-',
    'grid.alpha': 0.2,
    'grid.linewidth': 1.5
})

# 创建图形
fig, axs = plt.subplots(1, 2, figsize=(14, 6), dpi=300)
plt.subplots_adjust(wspace=0.4)

# 设置颜色
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# 自定义y轴刻度 (可以根据需要修改)
y_ticks = {
    'Recall@20': np.arange(0, 0.11, 0.02),  # 0到0.1，步长0.02
    'NDCG@20': np.arange(0, 0.07, 0.01)     # 0到0.06，步长0.01
}

# 绘制每个指标
for i, metric in enumerate(metrics):
    ax = axs[i]
    
    # 调整x轴位置
    x = np.arange(len(datasets)) * 1.5
    width = 0.3
    
    # 设置白色背景
    ax.set_facecolor('white')
    
    # 添加网格线
    ax.grid(True, which='both', axis='both', zorder=0)
    
    # 绘制柱状图
    for j, method in enumerate(methods):
        values = [data[dataset][metric][j] for dataset in datasets]
        ax.bar(x + j*width, values, width, label=method, color=colors[j],
               edgecolor='black', linewidth=0.5, zorder=3)
    
    # 设置轴标签
    ax.set_ylabel(metric)
    ax.set_xticks(x + width)
    ax.set_xticklabels(datasets)
    
    # 设置自定义y轴刻度
    ax.set_yticks(y_ticks[metric])
    ax.set_ylim([y_ticks[metric][0], y_ticks[metric][-1]])  # 根据刻度自动设置范围
    
    # 添加子图标签
    ax.text(0.5, -0.15, f'({chr(97+i)}) Performance on {metric}', transform=ax.transAxes,
            fontsize=25, ha='center')
    
    # 设置边框
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)
        spine.set_zorder(1)

# 添加图例
handles, labels = axs[0].get_legend_handles_labels()
legend = fig.legend(handles, labels, loc='upper center', ncol=3,
           bbox_to_anchor=(0.5, 1.15), frameon=True)
legend.get_frame().set_linewidth(1)
legend.get_frame().set_edgecolor("black")

plt.tight_layout()
plt.savefig('./POMNS/ablation.pdf', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()