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
methods = ['StabCF', 'w/o_H', 'w/o_U']
metrics = ['Recall@20', 'NDCG@20']
labels = ['StabCF', 'w/o_H', 'w/o_U']  # 对应横坐标标签

lightgcn_data = {
    'Alibaba': {
        'Recall@20': [0.0800, 0.0762,  0.0772],
        'NDCG@20': [0.0375, 0.0358, 0.0377],
    },
    'Amazon': {
        'Recall@20': [0.0518, 0.0510, 0.0458],
        'NDCG@20': [0.0241, 0.0240, 0.0214],
    },
    'Yelp2018': {
        'Recall@20': [0.0752, 0.0746, 0.0736],
        'NDCG@20': [0.0619, 0.0613, 0.0608],
    }
}

apegnn_data = {
    'Alibaba': {
        'Recall@20': [0.0701, 0.0635, 0.0603],
        'NDCG@20': [0.0337, 0.0295, 0.0295],
    },
    'Amazon': {
        'Recall@20': [0.0450, 0.0432, 0.0317],
        'NDCG@20': [0.0211, 0.0200, 0.0147],
    },
    'Yelp2018': {
        'Recall@20': [0.0737, 0.0692, 0.0427],
        'NDCG@20': [0.0605, 0.0568, 0.0352],
    }
}

colors = ["#a178ff", "#5BB7F9", "#F6EF16"]  # 第一个不变，后两个为高级蓝和金黄

# 为每个数据集和指标创建单独的图表
for dataset in datasets:
    for metric in metrics:
        fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
        # values = lightgcn_data[dataset][metric]
        values = apegnn_data[dataset][metric]

        # 绘制柱状图
        bars = ax.bar(labels, values, width=0.7, color=colors, edgecolor='black', linewidth=0.8, zorder=3)

        # # 添加数据标签
        # for bar in bars:
        #     height = bar.get_height()
        #     ax.annotate(f'{height:.4f}',
        #                 xy=(bar.get_x() + bar.get_width() / 2, height),
        #                 xytext=(0, 3),  # 垂直偏移
        #                 textcoords="offset points",
        #                 ha='center', va='bottom',
        #                 fontsize=22)

        # 设置Y轴范围（不从0开始，突出差异）
        min_val = min(values)
        max_val = max(values)
        y_padding = (max_val - min_val) * 0.5
        ax.set_ylim(min_val - y_padding * 0.5, max_val + y_padding * 0.3)  # 最小值更小

        # 设置较少的y轴刻度
        yticks = np.linspace(min_val, max_val, num=4)
        ax.set_yticks(yticks)
        ax.set_yticklabels([f'{tick:.4f}' for tick in yticks], fontsize=26)

        # 设置网格线
        ax.grid(axis='both', linestyle='--', alpha=0.3, zorder=0)
        ax.yaxis.set_ticks_position('none')
        ax.tick_params(axis='y', length=0)
        ax.tick_params(axis='x', labelsize=30, length=0)
        ax.xaxis.set_ticks_position('none')

        # 设置标签和标题，字体调大
        ax.set_ylabel(metric, fontsize=30)
        # ax.set_xlabel('Methods', fontsize=20)
        # ax.set_title(f'{dataset}-{metric}', pad=15, fontsize=20)

        # 调整布局
        plt.tight_layout(pad=2.0)

        # 保存为PDF
        # filename = f"./ablation/lightgcn-ablation-{dataset.replace(' ', '_')}-{metric.replace('@', '')}.pdf"
        filename = f"./ablation/apegnn-ablation-{dataset.replace(' ', '_')}-{metric.replace('@', '')}.pdf"
        plt.savefig(filename, format='pdf', bbox_inches='tight')
        plt.close(fig)

print("成功生成6个PDF图表文件！")