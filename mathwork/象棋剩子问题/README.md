# 象棋剩子问题的python实现 

## 必要的库
> * python3
> * pygame
> * numpy

## 问题定义
1. 首先假设有一盘象棋棋子，6个棋子可以摆成一个2x3的矩形或1x6的矩形。

⚪⚪⚪                                   ⚪⚪⚪⚪⚪⚪  
⚪⚪⚪

2. 我们都知道象棋中的炮可以打隔子，现假设有7个棋子在棋盘上呈的长方形，如图中所示，如果假定1号棋子为“炮”，根据炮可以打隔子原理，1号棋子可以消去并替代（后文中简称“消替”）3号棋子，紧接着又可以继续消替5号棋子，然后继续消替7号棋子与4号两个棋子，最后剩下2号与1号，6号三个棋子，如果假定2号棋子为“炮”，2号可以消替4号，接着消替6号，3号，7号，1号，结果只剩下2号与5号两个棋子。那么假定其他棋子为“炮”时，结果会剩下几个棋子呢？而且这些之中，哪一种会使得最后剩下的棋子最少？最少又为多少？通过验证可知，1X6的长方形经过如此步骤最后最少会剩下2个棋子，我们不妨将其称之为1X6的长方形“炮消除”为2。
  
⚪ ⚪ ⚪ ⚪ ⚪ ⚪

3. 从1和2的观点来看，那么对于由N个棋子构成的矩形“炮消除”为多少呢？

## 文件解释
> * problem_solver.py  
  对于给定的矩形获得最高的分数也即最少的剩子  
> * run_game.py  
  运行游戏，自行选择棋局大小和其实位置后，按上 下 左 右键即可开始游戏
