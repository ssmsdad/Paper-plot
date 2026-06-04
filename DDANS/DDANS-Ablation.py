import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体和样式
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'pdf.fonttype': 42,
    'ps.fonttype': 42
})

# 设置数据
datasets = ['Alibaba', 'Amazon', 'Yelp2018']
methods = ['DDANS', 'w/o C', 'w/o A']
metrics = ['Recall@20', 'NDCG@20']
labels = ['DDANS', 'w/o C', 'w/o A']  # 对应横坐标标签

# 你的新数据，替换这里的值
ddans_data = {
    'Alibaba': {
        'Recall@20': [0.07727, 0.07677, 0.0664],  # 替换为DDANS的实际数据
        'NDCG@20': [0.03572, 0.03621, 0.0315],
    },
    'Amazon': {
        'Recall@20': [0.04983, 0.048, 0.0439],
        'NDCG@20': [0.02291, 0.0216, 0.0201],
    },
    'Yelp2018': {
        'Recall@20': [0.07394, 0.07318, 0.0694],
        'NDCG@20': [0.06061, 0.06005, 0.0574],
    }
}

# 更新颜色方案 - 新的三个颜色
colors = ["#87CEEB", "#F0E68C", "#DDA0DD"]  # 天蓝色、卡其色、紫罗兰色

# 为每个数据集和指标创建单独的图表
for dataset in datasets:
    for metric in metrics:
        fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
        values = ddans_data[dataset][metric]

        # 绘制柱状图 - 调整边框颜色和宽度
        bars = ax.bar(labels, values, width=0.65, color=colors, 
                     edgecolor='darkgray', linewidth=1.0, zorder=3)

        # 设置Y轴范围（不从0开始，突出差异）
        min_val = min(values)
        max_val = max(values)
        y_padding = (max_val - min_val) * 0.4  # 稍微调小padding
        ax.set_ylim(min_val - y_padding * 0.4, max_val + y_padding * 0.3)

        # 设置较少的y轴刻度
        yticks = np.linspace(min_val, max_val, num=4)
        ax.set_yticks(yticks)
        ax.set_yticklabels([f'{tick:.4f}' for tick in yticks], fontsize=26)

        # 设置网格线 - 调整透明度和样式
        ax.grid(axis='both', linestyle=':', alpha=0.4, zorder=0, color='gray')
        ax.yaxis.set_ticks_position('none')
        ax.tick_params(axis='y', length=0)
        ax.tick_params(axis='x', labelsize=30, length=0)
        ax.xaxis.set_ticks_position('none')

        # 设置标签和标题，字体调大 - 改回黑色
        ax.set_ylabel(metric, fontsize=30, color='black')
        
        # 设置背景色为浅灰色
        ax.set_facecolor('#FAFAFA')

        # 调整布局
        plt.tight_layout(pad=2.0)

        # 保存为PDF
        filename = f"./ablation/ddans-ablation-{dataset.replace(' ', '_')}-{metric.replace('@', '')}.pdf"
        plt.savefig(filename, format='pdf', bbox_inches='tight')
        plt.close(fig)

print("成功生成6个DDANS消融实验PDF图表文件！")