import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
# ================= 字体设置 =================

# 英文：Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 中文字体单独指定（宋体）
# font_simsun = FontProperties(fname="C:/Windows/Fonts/simsun.ttc")  # Windows路径
# font_simsun = FontProperties(
#     fname=r"C:\Windows\Fonts\simsun.ttc"
# )
font_hei = FontProperties(
    fname=r"C:\Windows\Fonts\simhei.ttf",
    weight='bold'
)
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

datasets = ['ali', 'amazon', 'yelp2018']

methods = ['MixGCF', 'DINS', 'RNS']

# 日志路径
log_dir = 'loss_performance_plot/Adam'

# 输出路径
output_dir = 'figures/stable/Adam'

method_colors = {
    'MixGCF': 'tab:blue',
    'DINS': 'tab:orange',
    'StabCF': 'tab:green',
    'RNS': 'tab:red'
}

for dataset in datasets:

    dataset_output_dir = os.path.join(output_dir, dataset)
    os.makedirs(dataset_output_dir, exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax2 = ax1.twinx()

    lines = []
    labels = []

    for method in methods:

        # ================= Loss =================

        loss_file = os.path.join(
            log_dir,
            f'{method}/{dataset}_batchloss.log'
        )

        if os.path.exists(loss_file):

            with open(loss_file, 'r') as f:

                line = f.readline()

                batch_losses = [
                    float(x)
                    for x in line.strip().split(',')
                    if x != ''
                ]

                l1, = ax1.plot(
                    batch_losses,
                    label=f'{method} Loss',
                    color=method_colors[method],
                    linestyle='-',
                    linewidth=2
                )

                lines.append(l1)
                labels.append(f'{method} Loss')

        else:
            print(f'File not found: {loss_file}')

        # ================= Recall@20 =================

        recall_file = os.path.join(
            log_dir,
            f'{method}/{dataset}_batchrecall20.log'
        )

        if os.path.exists(recall_file):

            with open(recall_file, 'r') as f:

                line = f.readline()

                batch_recalls = [
                    float(x)
                    for x in line.strip().split(',')
                    if x != ''
                ]

                l2, = ax2.plot(
                    batch_recalls,
                    label=f'{method} Recall@20',
                    color=method_colors[method],
                    linestyle='--',
                    linewidth=2
                )

                lines.append(l2)
                labels.append(f'{method} Recall@20')

        else:
            print(f'File not found: {recall_file}')

    # ================= 坐标轴 =================

    ax1.set_xlabel(
        '训练批次',
        fontsize=30,
        fontproperties=font_hei,
        fontweight='bold'
    )

    ax1.set_ylabel(
        '损失值（Loss）',
        fontsize=30,
        fontproperties=font_hei,
        fontweight='bold'
    )

    ax2.set_ylabel(
        'Recall@20',
        fontsize=30
    )

    # ================= 刻度 =================

    ax1.tick_params(labelsize=22, length=0)
    ax2.tick_params(labelsize=22, length=0)

    # ================= 图例 =================

    fig.legend(
        lines,
        labels,
        loc='lower right',
        bbox_to_anchor=(0.88, 0.28),
        fontsize=16
    )

    # ================= 网格 =================

    plt.grid(True)

    plt.tight_layout()

    # ================= 保存 =================

    save_path = os.path.join(
        dataset_output_dir,
        'loss_recall20_without_dcans.pdf'
    )

    plt.savefig(
        save_path,
        dpi=330,
        bbox_inches='tight'
    )

    plt.close()

    print(f'Saved plot: {save_path}')