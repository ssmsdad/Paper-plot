import matplotlib.pyplot as plt

# 数据集（negs的4个值对应的结果）
datasets = {
    "ali": {
        "recall20": [0.07585, 0.07092, 0.07727, 0.07557],  # 对应negs=8,16,32,64
        "ndcg20": [0.03523, 0.03588, 0.03592, 0.03629],
    },
    "amazon": {
        "recall20": [0.04351, 0.04685, 0.04873, 0.04983],
        "ndcg20": [0.02229, 0.02222, 0.02324, 0.02339],
    },
    "yelp2018": {
        "recall20": [0.07200, 0.07300, 0.07400, 0.07450],  # 请替换为实际数据
        "ndcg20": [0.05900, 0.06000, 0.06100, 0.06150],   # 请替换为实际数据
    }
}

# 自定义刻度标签（negs 值）
x = [1, 2, 3, 4]
negs_labels = ['8', '16', '32', '64']

def plot_single_metric(dataset_name, metric):
    """为单个数据集绘制指定指标随 negs 变化的图表，并保存为 PDF 文件"""
    
    if dataset_name not in datasets:
        print(f"数据集 {dataset_name} 不存在！")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 按指标划分颜色和marker
    if metric == "recall20":
        color = "#87CEEB"  # 钢蓝色 - 稳重大气
        mark = "*"
        markersize = 44 
        ylabel = "Recall@20"
    else:
        color = "#FF6B9D"  # 金黄色 - 温暖明亮
        mark = "s"
        markersize = 34
        ylabel = "NDCG@20"
    
    # 绘制数据
    ax.plot(x, datasets[dataset_name][metric], label=ylabel, 
            marker=mark, color=color, linewidth=16, markersize=markersize)
    
    # 设置 x 轴和 y 轴
    ax.set_xticks(x)
    ax.set_xticklabels(negs_labels, fontsize=30)
    ax.set_xlabel(r"$M$", fontsize=44)
    ax.set_ylabel(ylabel, fontsize=44)
    
    # 设置图例
    # ax.legend(loc="lower right", fontsize=40)
    
    # 添加网格
    ax.grid(True, alpha=0.5)
    
    # 去掉刻度线
    ax.tick_params(axis="both", which="both", length=0)
    
    # 设置刻度标签大小
    ax.tick_params(axis="y", labelsize=30)
    
    # 保存图表到指定目录
    plt.savefig(f"./sensitivity/negs/{metric}_vs_negs_{dataset_name}.pdf", bbox_inches="tight")
    plt.close()

# 调用函数分别绘制所有组合
for dataset_name in ["ali", "amazon"]:
    for metric in ["recall20"]:
        plot_single_metric(dataset_name, metric)

print("成功生成2个negs敏感度分析PDF图表文件！")