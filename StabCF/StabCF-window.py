import matplotlib.pyplot as plt


apegnn_datasets = {
    "ali": {
        "recall20": [0.06347, 0.06296, 0.0648, 0.06516, 0.06652, 0.06517, 0.06872, 0.06747, 0.06734, 0.07006],
        "ndcg20": [0.02988, 0.02975, 0.03082, 0.03108, 0.03198, 0.03109, 0.0326, 0.03259, 0.03254, 0.03365]
    },
    "amazon": {
        "recall20": [0.04353, 0.04369, 0.04414, 0.04369, 0.04429, 0.04446, 0.04483, 0.04433, 0.04453, 0.04504],
        "ndcg20": [0.02044, 0.02059, 0.02073, 0.02058, 0.021, 0.02109, 0.02107, 0.02096, 0.02091, 0.02106]
    },
    "yelp2018": {
        "recall20": [0.07027, 0.07071, 0.07153, 0.07219, 0.0728, 0.07322, 0.07354, 0.0735, 0.07338, 0.07371],
        "ndcg20": [0.05764, 0.05814, 0.05885, 0.05941, 0.05985, 0.06034, 0.06031, 0.06029, 0.06032, 0.06053]
    }
}

lightgcn_datasets = {
    "ali": {
        "recall20": [0.07662, 0.07701, 0.0781, 0.07788, 0.07906, 0.08005, 0.08068, 0.08, 0.07938, 0.07996],
        "ndcg20": [0.03565, 0.0361, 0.03681, 0.03688, 0.03729, 0.03758, 0.03791, 0.03766, 0.03743, 0.03754]
    },
    "amazon": {
        "recall20": [0.05114, 0.05122, 0.05163, 0.05164, 0.0518, 0.05143, 0.05144, 0.05103, 0.05106, 0.05087],
        "ndcg20": [0.02386, 0.02396, 0.02416, 0.0241, 0.02408, 0.02391, 0.02406, 0.02367, 0.02378, 0.0237]
    },
    "yelp2018": {
        "recall20": [0.07455, 0.07473, 0.07477, 0.07494, 0.07517, 0.07508, 0.075, 0.07497, 0.07486, 0.07493],
        "ndcg20": [0.06125, 0.0615, 0.06155, 0.06178, 0.06192, 0.06193, 0.06171, 0.06166, 0.06152, 0.06152]
    }
}

ngcf_datasets = {
    "ali": {
        "recall20": [0.04959, 0.05985, 0.0564, 0.05923, 0.06197, 0.0586, 0.06046, 0.06067, 0.06353, 0.06274],
        "ndcg20": [0.02264, 0.02795, 0.02619, 0.0276, 0.02914, 0.02701, 0.02835, 0.02847, 0.02993, 0.02943]
    },
    "amazon": {
        "recall20": [0.03455, 0.03499, 0.0363, 0.03694, 0.03634, 0.03563, 0.03533, 0.03633, 0.0354, 0.03447],
        "ndcg20": [0.01529, 0.01552, 0.01602, 0.01657, 0.01633, 0.01613, 0.01599, 0.01593, 0.01581, 0.0154]
    },
    "yelp2018": {
        "recall20": [0.0665, 0.06871, 0.06927, 0.07024, 0.07047, 0.07, 0.07013, 0.06983, 0.0666, 0.06905],
        "ndcg20": [0.05461, 0.05665, 0.05717, 0.05776, 0.0579, 0.05763, 0.05764, 0.05743, 0.05457, 0.05696]
    }
}


# 自定义刻度标签（window length 值）
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # window length 的值
window_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # 对应的标签


# 直接画 recall20 和 ndcg20 的图，一次画六张 PDF
def plot_metric(dataset_name, metric):
    """为单个数据集绘制 metric 随 window length 变化的图表，并保存为 PDF 文件"""
    if metric not in ["recall20", "ndcg20"]:
        print(f"不支持的指标: {metric}")
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    # 按指标划分颜色和marker
    if metric == "recall20":
        # color = "#b41f4e"
        color = "#d62728"
        mark = "*"
        markersize = 44 
    else:
        color = "#6a51a3"
        mark = "s"
        markersize = 34 

    ax.plot(x, lightgcn_datasets[dataset_name][metric], label=metric, marker=mark, color=color, linewidth=16, markersize=markersize)
    ax.set_xticks(x)
    ax.set_xticklabels(window_labels, fontsize=32)
    ax.set_xlabel(r"Historical Positives $N$", fontsize=42)
    ylabel = "Recall@20" if metric == "recall20" else "NDCG@20"
    ax.set_ylabel(ylabel, fontsize=42)
    # ax.legend(loc="lower right", fontsize=40)
    ax.grid(True, alpha=0.5)
    ax.tick_params(axis="both", which="both", length=0)
    ax.tick_params(axis="y", labelsize=24)
    # plt.savefig(f"./sensitivity/window/apegnn-{metric}_vs_window_{dataset_name}.pdf", bbox_inches="tight")
    plt.savefig(f"./sensitivity/window/ngcf-{metric}_vs_window_{dataset_name}.pdf", bbox_inches="tight")
    # plt.savefig(f"./sensitivity/window/lightgcn-{metric}_vs_window_{dataset_name}.pdf", bbox_inches="tight")
    plt.close()

# 依次画六张 PDF

for dataset in lightgcn_datasets.keys():
    plot_metric(dataset, "recall20")
    plot_metric(dataset, "ndcg20")

print("All plots saved successfully.")