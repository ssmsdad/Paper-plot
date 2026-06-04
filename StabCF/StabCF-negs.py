import matplotlib.pyplot as plt

# 数据集（根据需要调整 alpha 值和对应的 recall20 值）
apegnn_datasets = {
    "ali": {
        "recall@20": [0.05821, 0.05907, 0.06214],
        "ndcg@20": [0.02818, 0.02813, 0.02971]
    },
    "amazon": {
        "recall@20": [0.03717, 0.03729, 0.03891],
        "ndcg@20":  [0.01668, 0.01695, 0.01787]
    },
    "yelp2018": {
        "recall@20": [0.06729, 0.06946, 0.07016],
        "ndcg@20": [0.05536, 0.05726, 0.05789]
    },
}



# 自定义刻度标签
x = [1, 2, 3]  
window_labels = ['16', '32', '64']  # 对应的标签

# 画 Candidate Set Size 与 recall@20、ndcg@20 的图
def plot_metric_vs_candidate_size(dataset_name, metric):
    """为单个数据集绘制 metric 随 Candidate Set Size 变化的图表，并保存为 PDF 文件"""
    if dataset_name not in apegnn_datasets:
        print(f"数据集 {dataset_name} 不存在！")
        return
    if metric not in ["recall@20", "ndcg@20"]:
        print(f"不支持的指标: {metric}")
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    # 为三个数据集分配三个颜色
    color_map = {
        "ali": "#b41f4e",      # 蓝色
        "amazon": "#42f4df",   # 金色
        "yelp2018": "#a02c7d"  # 绿色
    }
    color = color_map.get(dataset_name, "#333333")
    mark = "*" if dataset_name == "ali" else ("s" if dataset_name == "amazon" else "o")
    markersize = 44 if dataset_name == "ali" else (38 if dataset_name == "amazon" else 34)
    loc = "upper right" if dataset_name == "ali" else ("lower right" if dataset_name == "amazon" else "best")
    ax.plot(x, apegnn_datasets[dataset_name][metric], label=metric, marker=mark, color=color, linewidth=16, markersize=markersize)
    ax.set_xticks(x)
    ax.set_xticklabels(window_labels, fontsize=32)
    ax.set_xlabel("Candidate Set Size", fontsize=42)
    ylabel = "Recall@20" if metric == "recall@20" else "NDCG@20"
    ax.set_ylabel(ylabel, fontsize=42)
    ax.legend(loc=loc, fontsize=40)
    ax.grid(True, alpha=0.5)
    ax.tick_params(axis="both", which="both", length=0)
    ax.tick_params(axis="y", labelsize=24)
    plt.savefig(f"./sensitivity/apegnn-{metric}_vs_Candidate_{dataset_name}.pdf", bbox_inches="tight")
    plt.close()

# 分别画 recall@20 和 ndcg@20 的图
for dataset in apegnn_datasets.keys():
    plot_metric_vs_candidate_size(dataset, "recall@20")
    plot_metric_vs_candidate_size(dataset, "ndcg@20")
