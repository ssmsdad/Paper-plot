# import matplotlib.pyplot as plt
# import numpy as np

# # 中文字体
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False

# # 方法
# methods = ['HRNS-PA', 'HRNS-HI', 'HRNS']

# # 数据
# data = {
#     "Alibaba": {
#         "Recall@20": [0.0695, 0.0674, 0.0725],
#         "NDCG@20": [0.0326, 0.0304, 0.0350],
#         "Hit_ratio@20": [0.0793, 0.0776, 0.0829]
#     },
#     "Amazon": {
#         "Recall@20": [0.0475, 0.0463, 0.0486],
#         "NDCG@20": [0.0219, 0.0214, 0.0226],
#         "Hit_ratio@20": [0.0524, 0.0510, 0.0538]
#     },
#     "Yelp2018": {
#         "Recall@20": [0.0709, 0.0684, 0.0727],
#         "NDCG@20": [0.0578, 0.0564, 0.0600],
#         "Hit_ratio@20": [0.0413, 0.0403, 0.0428]
#     }
# }

# metrics = ["Recall@20", "NDCG@20", "Hit_ratio@20"]

# # 清亮配色
# colors = ['#4C72B0', '#55A868', '#DD8452']

# bar_width = 0.22
# x = np.arange(len(methods))

# for dataset in data:
#     # 关键：让柱子更扁
#     # plt.figure(figsize=(7,3.5))
#     plt.figure(figsize=(6,4))

#     for i, metric in enumerate(metrics):

#         values = data[dataset][metric]

#         plt.bar(
#             x + (i-1)*bar_width,
#             values,
#             width=bar_width,
#             label=metric,
#             color=colors[i],
#             edgecolor='black',
#             linewidth=0.6
#         )

#     plt.xticks(x, methods)
#     plt.xlabel("方法")
#     plt.ylabel("指标值")

#     # plt.title(dataset + " 数据集消融实验")

#         # 关键：扩大y轴范围，让柱子看起来更低
#     max_value = max([max(data[dataset][m]) for m in metrics])
#     plt.ylim(0, max_value * 1.4)

#     plt.legend(loc='upper left')

#     plt.grid(axis='y', linestyle='--', alpha=0.5)

#     plt.tight_layout()

#     plt.savefig(dataset + "_消融实验.png", dpi=300)
import matplotlib.pyplot as plt
import numpy as np

# 字体设置
plt.rcParams['font.family'] = ['Times New Roman', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 字号设置
plt.rcParams['font.size'] = 14           # 全局字体大小
plt.rcParams['axes.titlesize'] = 16      # 标题大小
plt.rcParams['axes.labelsize'] = 15      # 坐标轴标签大小
plt.rcParams['xtick.labelsize'] = 13     # x轴刻度标签大小
plt.rcParams['ytick.labelsize'] = 24     # y轴刻度标签大小
plt.rcParams['legend.fontsize'] = 13     # 图例字体大小

# methods = ['HRNS-HP', 'HRNS-HI', 'HRNS']
methods = ['ADRNS-OS', 'ADRNS-RA', 'ADRNS']

fp_data = {
    "Alibaba": {
        "Recall@20": [0.0703, 0.0696, 0.0725],
        "NDCG@20": [0.0334, 0.0332, 0.0350],
        "Hit_ratio@20": [0.0804, 0.0792, 0.0838]
    },
    "Amazon": {
        "Recall@20": [0.0476, 0.0479, 0.0486],
        "NDCG@20": [0.0223, 0.0220, 0.0226],
        "Hit_ratio@20": [0.0528, 0.0526, 0.0538]
    },
    "Yelp2018": {
        "Recall@20": [0.0718, 0.0697, 0.0727],
        "NDCG@20": [0.0590, 0.0574, 0.0600],
        "Hit_ratio@20": [0.4245, 0.4175, 0.4291]
    }
}

rew_data = {
    "Alibaba": {
        "Recall@20": [0.0543,0.0728, 0.0746],
        "NDCG@20": [0.0242, 0.0349, 0.0358],
        "Hit_ratio@20": [0.0639, 0.0834, 0.0858]
    },
    "Amazon": {
        "Recall@20": [0.0403, 0.0486, 0.0492],
        "NDCG@20": [0.0175, 0.0225, 0.0230],
        "Hit_ratio@20": [0.0454, 0.0537, 0.0548]
    },
    "Yelp2018": {
        "Recall@20": [0.0555, 0.0728, 0.0733],
        "NDCG@20": [0.0452, 0.0599, 0.0605],
        "Hit_ratio@20": [0.3546, 0.4282, 0.4296]
    }
}

metrics = ["Recall@20", "NDCG@20", "Hit_ratio@20"]
colors = ['#4C72B0', '#55A868', '#DD8452']

bar_width = 0.22
x = np.arange(len(methods))

datasets = list(fp_data.keys())
# datasets = list(rew_data.keys())

fig, axes = plt.subplots(1, 3, figsize=(18,7))

for idx, dataset in enumerate(datasets):

    ax = axes[idx]

    for i, metric in enumerate(metrics):

        values = fp_data[dataset][metric]
        # values = rew_data[dataset][metric]

        ax.bar(
            x + (i-1)*bar_width,
            values,
            width=bar_width,
            label=metric,
            color=colors[i],
            edgecolor='black',
            linewidth=0.6
        )

    ax.set_xticks(x)
    ax.set_xticklabels(methods, fontsize=18)

    ax.set_xlabel("方法", fontsize=24)
    ax.set_ylabel("指标值", fontsize=24)

    ax.set_title(dataset, fontsize=24, fontname='Times New Roman')

    # 保持柱子扁一点
    max_value = max([max(fp_data[dataset][m]) for m in metrics])
    # max_value = max([max(rew_data[dataset][m]) for m in metrics])
    ax.set_ylim(0, max_value * 1.4)

    # 图例仍然在图内，字体更大
    ax.legend(loc='upper right', fontsize=20)

    ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig("./ablation/消融实验_三数据集_fp.png", dpi=300)
# plt.savefig("./ablation/消融实验_三数据集_rew.png", dpi=300)


# plt.show()
print("弄完了!")
    # plt.show()