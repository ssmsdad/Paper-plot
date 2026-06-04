import matplotlib.pyplot as plt

# 数据集（根据需要调整 alpha 值和对应的 recall20 值）
# datasets = {
#     "ali": {
#         "recall20": [0.07235, 0.07047, 0.07404, 0.07424, 0.0739, 0.07236, 0.07358, 0.07333, 0.07253],
#     },
#     "amazon": {
#         "recall20": [0.04701, 0.04898, 0.04786, 0.04828, 0.04881, 0.04843, 0.04757, 0.04777, 0.04774],
#     }
# }
# datasets = {
#     "ali": {
#         "recall20": [0.07401, 0.07524, 0.07446, 0.07626, 0.0776, 0.07894, 0.04901, 0.00468],
#     },
#     "amazon": {
#         "recall20": [0.04821, 0.04811, 0.04878, 0.04966, 0.05002, 0.0504, 0.04407, 0.00268],
#     }
# }
datasets = {
    "ali": {
        "ndcg20": [0.03523, 0.03588, 0.03533, 0.03592, 0.03629, 0.03638, 0.02402, 0.0022],
    },
    "amazon": {
        "ndcg20": [0.02229, 0.02222, 0.02258, 0.02324, 0.02339, 0.02345, 0.02097, 0.0011],
    }
}

# 自定义刻度标签（alpha 值）
x = [1, 2, 3, 4, 5, 6, 7, 8]
# alpha_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alpha_labels = ['0.2', '0.4', '0.6', '0.8', '0.9', '0.95', '0.99', '0.995']

def plot_single_dataset(dataset_name):
    """为单个数据集绘制 Recall@20 随 alpha 变化的图表，并保存为 PDF 文件"""
    
    if dataset_name not in datasets:
        print(f"数据集 {dataset_name} 不存在！")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 设置颜色
    color = "#1f77b4" if dataset_name == "ali" else "#f4c542"
    mark = "*" if dataset_name == "ali" else "s"
    markersize = 44 if dataset_name == "ali" else 34

    # "#f4c542" #F5A623 #1f77b4 #4A90E2
    
    # 绘制数据
    # ax.plot(x, datasets[dataset_name]["recall20"], label="recall", 
    #         marker=mark, color=color, linewidth=16, markersize=markersize)
    ax.plot(x, datasets[dataset_name]["ndcg20"], label="ndcg", 
            marker=mark, color=color, linewidth=16, markersize=markersize)
    
    # 设置 x 轴和 y 轴
    ax.set_xticks(x)
    ax.set_xticklabels(alpha_labels, fontsize=30)
    # ax.set_xlabel(r"$\lambda$", fontsize=42)
    ax.set_xlabel(r"$\alpha$", fontsize=42)
    # ax.set_ylabel("Recall@20", fontsize=42)
    ax.set_ylabel("NDCG@20", fontsize=42)
    
    # 设置图例
    ax.legend(loc="lower right", fontsize=40)
    
    # 添加网格
    ax.grid(True, alpha=0.5)
    
    # 去掉刻度线
    ax.tick_params(axis="both", which="both", length=0)
    
    # 设置刻度标签大小
    ax.tick_params(axis="y", labelsize=30)
    
    # 保存图表
    # plt.savefig(f"./DCANS/recall_vs_Lambda_{dataset_name}.pdf", bbox_inches="tight")
    # plt.savefig(f"./POMNS/recall_vs_Alpha_{dataset_name}.pdf", bbox_inches="tight")
    plt.savefig(f"./POMNS/ndcg_vs_Alpha_{dataset_name}.pdf", bbox_inches="tight")
    plt.close()

# 调用函数分别绘制 ali 和 amazon 的图表
plot_single_dataset("ali")
plot_single_dataset("amazon")