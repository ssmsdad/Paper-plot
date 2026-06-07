import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

lightgcn_datasets_fp = {
    "ali": {
        "recall20": [0.0716, 0.0712, 0.0710, 0.0718, 0.0725, 0.0714, 0.0709, 0.0713, 0.0717, 0.0711],
    },
    "amazon": {
        "recall20": [0.0472, 0.0475, 0.0471, 0.0478, 0.0486, 0.0476, 0.0474, 0.0477, 0.0473, 0.0470],
    },
    "yelp2018": {
        "recall20": [0.0719, 0.0714, 0.0717, 0.0711, 0.0727, 0.0720, 0.0715, 0.0718, 0.0712, 0.0716],
    }
}

lightgcn_datasets_rew = {
    "ali": {
        "recall20": [0.0712, 0.0725, 0.0734, 0.0741, 0.0746, 0.0740, 0.0735, 0.0729, 0.0722, 0.0716],
    },
    "amazon": {
        "recall20": [0.0485, 0.0486, 0.0484, 0.0485, 0.0492, 0.0471, 0.0483, 0.0478, 0.0481, 0.0471],
    },
    "yelp2018": {
        "recall20": [0.0730, 0.0733, 0.0730, 0.0729, 0.0730, 0.0729, 0.0730, 0.0730, 0.0728, 0.0729],
    }
}

rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']  # 英文默认
rcParams['axes.unicode_minus'] = False        # 解决负号显示问题

# 中文字体单独指定（宋体）
font_simsun = FontProperties(fname="C:/Windows/Fonts/simsun.ttc")  # Windows路径

# 自定义刻度标签（window length 值）
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # window length 的值
window_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # 对应的标签


# 直接画 recall20 和 ndcg20 的图，一次画六张 PDF
def plot_metric(dataset_name, metric):

    if metric not in ["recall20", "ndcg20"]:
        print(f"不支持的指标: {metric}")
        return

    fig, ax = plt.subplots(figsize=(10, 4))

    # 数据集颜色
    color_map = {
        "ali": "#b41f4e",
        "amazon": "#ff7f0e",
        "yelp2018": "#2ca02c"
    }

    color = color_map.get(dataset_name, "#b41f4e")

    mark = "*"
    markersize = 26

    ax.plot(
        x,
        # lightgcn_datasets_fp[dataset_name][metric],
        lightgcn_datasets_rew[dataset_name][metric],
        label=metric,
        marker=mark,
        color=color,
        linewidth=4,
        markersize=markersize
    )

    ax.set_xticks(x)
    ax.set_xticklabels(window_labels, fontsize=18)

    ax.set_xlabel(r"$M$", fontsize=20)
    ax.set_ylabel("Recall@20", fontsize=20)

    ax.grid(True, alpha=0.5)

    ax.tick_params(axis="both", which="both", length=0)
    ax.tick_params(axis="y", labelsize=18)

    plt.savefig(
        # f"./sensitivity/fp/{metric}_vs_window_{dataset_name}.png",
        f"./sensitivity/rew/{metric}_vs_window_{dataset_name}.png",
        bbox_inches="tight",
        dpi=300
    )

    plt.close()
# def plot_metric(dataset_name, metric):
#     """为单个数据集绘制 metric 随 window length 变化的图表，并保存为 PDF 文件"""
#     if metric not in ["recall20", "ndcg20"]:
#         print(f"不支持的指标: {metric}")
#         return
#     fig, ax = plt.subplots(figsize=(10, 6))
#     # 按指标划分颜色和marker
#     if metric == "recall20":
#         # color = "#6a51a3"
#         color = "#b41f4e"
#         # color = "#d62728"
#         mark = "*"
#         markersize = 26 
#     else:
#         color = "#6a51a3"
#         mark = "s"
#         markersize = 34 

#     ax.plot(x, lightgcn_datasets[dataset_name][metric], label=metric, marker=mark, color=color, linewidth=4, markersize=markersize)
#     ax.set_xticks(x)
#     ax.set_xticklabels(window_labels, fontsize=18)
#     ax.set_xlabel(r"$M$", fontsize=20)
#     ylabel = "Recall@20" if metric == "recall20" else "NDCG@20"
#     ax.set_ylabel(ylabel, fontsize=20)
#     # ax.legend(loc="lower right", fontsize=40)
#     ax.grid(True, alpha=0.5)
#     ax.tick_params(axis="both", which="both", length=0)
#     ax.tick_params(axis="y", labelsize=18)
#     plt.savefig(f"./graduation/sensitivity/{metric}_vs_window_{dataset_name}.png", bbox_inches="tight", dpi=300)
#     plt.close()

# for dataset in lightgcn_datasets_fp.keys():
for dataset in lightgcn_datasets_rew.keys():
    plot_metric(dataset, "recall20")

print("All plots saved successfully.")