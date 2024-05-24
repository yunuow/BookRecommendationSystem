首先将前端的交互与data/ours/output.txt相关联,格式是userid itemid x n

如0 1 4 6 7

代表用户0 喜欢 1 4 6 7物品

然后code下main.py训练模型

训练完成后使用code下loadmodel.py生成推理结果

保存文件是code目录下recommendation.json格式是用户id 的top 20个推荐和推荐得分(没有归一化,不是线性得分,无实际意义)
