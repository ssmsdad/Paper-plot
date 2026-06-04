import matplotlib.pyplot as plt

# 数据集（根据需要调整 window length 值和对应的 recall20 值）
datasets = {
    "ali": {
        "recall20": [0.0726, 0.07391, 0.07402, 0.07476, 0.07537, 0.07377, 0.07377, 0.07354, 0.07366, 0.07253],
    },
    "amazon": {
        "recall20": [0.0486, 0.04879, 0.04741, 0.04721, 0.04898, 0.04868, 0.04848, 0.04867, 0.04682, 0.04792],
    }
}

# 自定义刻度标签（window length 值）
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # window length 的值
window_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # 对应的标签

def plot_single_dataset(dataset_name):
    """为单个数据集绘制 Recall@20 随 window length 变化的图表，并保存为 PDF 文件"""
    
    if dataset_name not in datasets:
        print(f"数据集 {dataset_name} 不存在！")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 设置颜色
    color = "#1f77b4" if dataset_name == "ali" else "#f4c542"
    mark = "*" if dataset_name == "ali" else "s"
    markersize = 44 if dataset_name == "ali" else 38
    loc = "upper right" if dataset_name == "ali" else "lower right"
    
    # 绘制数据，将标签设置为 "recall"，标记改为星号
    ax.plot(x, datasets[dataset_name]["recall20"], label="recall", 
            marker=mark, color=color, linewidth=16, markersize=markersize)
    
    # 设置 x 轴和 y 轴
    ax.set_xticks(x)
    ax.set_xticklabels(window_labels, fontsize=32)
    ax.set_xlabel("Window Length", fontsize=42)
    ax.set_ylabel("Recall@20", fontsize=42)
    
    # 设置图例
    ax.legend(loc=loc, fontsize=40)
    
    # 添加网格
    ax.grid(True, alpha=0.5)
    
    # 去掉刻度线
    ax.tick_params(axis="both", which="both", length=0)
    
    # 设置刻度标签大小
    ax.tick_params(axis="y", labelsize=24)
    
    # 保存图表
    plt.savefig(f"./DCANS/recall_vs_window_{dataset_name}.pdf", bbox_inches="tight")
    plt.close()

# 调用函数分别绘制 ali 和 amazon 的图表
plot_single_dataset("ali")
plot_single_dataset("amazon")