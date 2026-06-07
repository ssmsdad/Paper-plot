import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

lightgcn_datasets_fp = {
    "ali": {
        "recall20": [0.0714, 0.0719, 0.0725, 0.0716, 0.0712, 0.0718, 0.0715, 0.0713, 0.0717, 0.0711],
    },
    "amazon": {
        "recall20": [0.0486, 0.0478, 0.0475, 0.0479, 0.0476, 0.0477, 0.0474, 0.0473, 0.0478, 0.0476],
    },
    "yelp2018": {
        "recall20": [0.0727, 0.0719, 0.0722, 0.0718, 0.0721, 0.0720, 0.0717, 0.0723, 0.0719, 0.0716],
    }
}

lightgcn_datasets_rew = {
    "ali": {
        "recall20": [0.0702, 0.0728, 0.0746, 0.0735, 0.0721, 0.0710, 0.0716, 0.0704, 0.0698, 0.0692],
    },
    "amazon": {
        "recall20": [0.0480, 0.0488, 0.0492, 0.0481, 0.0476, 0.0481, 0.0475, 0.0485, 0.0480, 0.0472],
    },
    "yelp2018": {
        "recall20": [0.0733, 0.0729, 0.0728, 0.0728, 0.0728, 0.0725, 0.0725, 0.0723, 0.0724, 0.0717],
    }
}


rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']  # 英文默认
rcParams['axes.unicode_minus'] = False        # 解决负号显示问题

# 中文字体单独指定（宋体）
font_simsun = FontProperties(fname="C:/Windows/Fonts/simsun.ttc")  # Windows路径

def plot_single_metric(dataset_name):

    # values = lightgcn_datasets_fp[dataset_name]["recall20"]
    values = lightgcn_datasets_rew[dataset_name]["recall20"]
    x_full = list(range(1, len(values) + 1))

    fig, ax = plt.subplots(figsize=(10, 4))

    color_map = {
        "ali": "#1f77b4",      # 蓝
        "yelp2018": "#F5A623", # 橙
        "amazon": "#2ca02c"    # 绿
    }

    markerfacecolor_map = {
        "ali": "#F5A623",      # 橙
        "yelp2018": "#1f77b4", # 蓝
        "amazon": "#17becf"    # 青色
    }

    color = color_map.get(dataset_name, "#0d0d0d")
    markerfacecolor = markerfacecolor_map.get(dataset_name, "#1f77b4")

    ax.plot(x_full, values, color=color, linewidth=4)

    # 标记最大值
    max_idx = values.index(max(values))
    ax.plot(
        x_full[max_idx],
        values[max_idx],
        marker="*",
        color=color,
        markersize=26,
        label="最大值",
        markerfacecolor=markerfacecolor,
        markeredgewidth=0
    )

    ax.set_xticks(x_full)
    ax.set_xticklabels([str(i) for i in x_full], fontsize=18)

    ax.set_xlabel(r"$\alpha$", fontsize=20)
    ax.set_ylabel("Recall@20", fontsize=20)

    legend = ax.legend(
    loc="upper right",
    fontsize=32,
    prop=FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=20),  # ⭐ 关键
    # markerscale=0.6   # ⭐ 控制图例中 marker（星星）大小
)

# ⭐ 让图例中的线宽和主图一致
    for line in legend.get_lines():
        line.set_linewidth(4)

    ax.grid(True, alpha=0.3)

    ax.tick_params(axis="both", which="both", length=0)
    ax.tick_params(axis="x", labelsize=18)
    ax.tick_params(axis="y", labelsize=18)

    # plt.savefig(f"./sensitivity/fp/recall_vs_alpha_{dataset_name}.png",
    plt.savefig(f"./sensitivity/rew/recall_vs_alpha_{dataset_name}.png",
                bbox_inches="tight",
                dpi=300)

    plt.close()


# 画三个数据集
# for dataset_name in lightgcn_datasets_fp.keys():
for dataset_name in lightgcn_datasets_rew.keys():
    plot_single_metric(dataset_name)