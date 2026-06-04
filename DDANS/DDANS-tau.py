import matplotlib.pyplot as plt

datasets = {
    "ali": {
        "recall20": [0.07517, 0.07438, 0.0754, 0.07539,0.07561,0.07596,0.07662,0.07728,0.07703,0.07727,0.07711],  # 对应tau=0.1,0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9,2.1
        "ndcg20": [0.03452, 0.03411, 0.03484, 0.03478,0.03485,0.03498,0.03532,0.03566,0.03573,0.03572,0.03558],
    },
    "amazon": {
        "recall20": [0.04784, 0.04784, 0.0481, 0.04805,0.048,0.04858,0.04819,0.04836,0.04857,0.04837,0.04842],
        "ndcg20": [0.02184, 0.02198, 0.02208, 0.02207,0.0221,0.02233,0.02224,0.02231,0.02239,0.02234,0.02239],
    },
    "yelp2018": {
        "recall20": [0.07200, 0.07300, 0.07400, 0.07450],  # 请替换为实际数据
        "ndcg20": [0.05900, 0.06000, 0.06100, 0.06150],   # 请替换为实际数据
    }
}

# 自定义刻度标签（tau 值）
x = [1, 2, 3, 4,5,6,7,8,9,10,11]
tau_labels = ['0.1','0.3','0.5','0.7','0.9','1.1','1.3','1.5','1.7','1.9','2.1']

def plot_single_metric(dataset_name, metric):
    """为单个数据集绘制指定指标随 tau 变化的图表，并保存为 PDF 文件"""
    
    if dataset_name not in datasets:
        print(f"数据集 {dataset_name} 不存在！")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 按指标划分颜色和marker
    if metric == "recall20":
        color = "#FF6B9D"  # 活力粉色 - 轻快活泼
        mark = "*"
        markersize = 44 
        ylabel = "Recall@20"
    else:
        color = "#87CEEB"  # 天蓝色 - 清新淡雅
        mark = "s"
        markersize = 34
        ylabel = "NDCG@20"
    
    # 绘制数据
    ax.plot(x, datasets[dataset_name][metric], label=ylabel, 
            marker=mark, color=color, linewidth=16, markersize=markersize)
    
    # 设置 x 轴和 y 轴
    ax.set_xticks(x)
    ax.set_xticklabels(tau_labels, fontsize=28)
    ax.set_xlabel(r"$\tau$", fontsize=44)
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
    plt.savefig(f"./sensitivity/tau/{metric}_vs_tau_{dataset_name}.pdf", bbox_inches="tight")
    plt.close()

# 调用函数分别绘制所有组合
for dataset_name in ["ali", "amazon"]:
    for metric in ["recall20", "ndcg20"]:
        plot_single_metric(dataset_name, metric)

print("成功生成4个tau敏感度分析PDF图表文件！")