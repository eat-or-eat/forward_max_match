# 前向最大匹配算法实现

> 本项目完成两种前向最大匹配的的实现方法，并进行了比较

# 一，运行项目

## 环境

```
python3
random
time
```



## 1.克隆下载

`git clone git@github.com:eat-or-eat/forward_max_match.git`

## 2.运行脚本

在项目文件夹下(.../forward_max_match/:)用命令窗口运行：`python method_comparison.py`

## 3.运行结果

```bash
D:\project\forward_max_match>python method_comparison.py
朴素分词耗时: 0.028026103973388672
前缀分词耗时: 0.012010812759399414

# 结论：前缀字典切分速度优于朴素切分，实验结果受电脑配置影响，但整体结果不变
```

# 二，项目说明

## 1.数据来源

1. 词表来自于jieba的[dict.txt.small](https://github.com/fxsjy/jieba/tree/master/extra_dict)
2. 待切分预料由词表数据生成

## 2.项目结构以及文件介绍

```
|——README.md //项目介绍
|——method_comparison.py //算法运行脚本
|——config.py //配置文件
|——data      //数据文件夹
	|——corpus.txt  //由词典数据生成的预料
	|——generate_corpus.py //利用词典生成预料的脚本
	|——small_dict.txt //jieba词典
|——output    //输出（简单日志）文件夹
	|——prefix_cut_result.txt //前缀字典分词结果
	|——simple_cut_result.txt //朴素字典分词结果

```





