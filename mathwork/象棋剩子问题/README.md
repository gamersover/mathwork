# 象棋剩子问题的python实现 

## 必要的库
> * python3
> * pygame
> * numpy

## 问题定义
1. 首先假设有一盘象棋棋子，现在随意取出N个棋子摆成矩形，如图所示，取出6个棋子可以摆成一个1x6的矩形或2x3的矩形。  

<center>
<img src="https://note.youdao.com/yws/api/personal/file/7D378491699D46DBABEC4E8E2C543B0A?method=download&shareKey=50f0891492fb747b257391d75559db8a"  width=30% height=30% />
<img src="https://note.youdao.com/yws/api/personal/file/8A1A5FA031954F258A31F70921D2E158?method=download&shareKey=221764e3db49285ae0c17a6aca167828"  width=30%  height=30% />
</center>

2. 我们都知道象棋中的炮可以打隔子，现假设有7个棋子在棋盘上呈的长方形，如图中所示，如果假定1号棋子为“炮”，根据炮可以打隔子原理，1号棋子可以消去并替代（后文中简称“消替”）3号棋子，紧接着又可以继续消替5号棋子，然后继续消替7号棋子与4号两个棋子，最后剩下2号与1号，6号三个棋子，如果假定2号棋子为“炮”，2号可以消替4号，接着消替6号，3号，7号，1号，结果只剩下2号与5号两个棋子。那么假定其他棋子为“炮”时，结果会剩下几个棋子呢？而且这些之中，哪一种会使得最后剩下的棋子最少？最少又为多少？通过验证可知，的长方形经过如此步骤最后最少会剩下2个棋子，我们不妨将其称之为的长方形“炮消除”为2，由此而知，的长方形“炮消除”为2，的正方形“炮消除”为6，的正方形“炮消除”为5。

<center>
<img src="https://note.youdao.com/yws/api/personal/file/8E6D35A15EE84917A2A36296C445A68C?method=download&shareKey=574246ff9649f469abfe9e136af52335"  width=30%  height=30% />
<img src="https://note.youdao.com/yws/api/personal/file/D3FE28DDC8E84328BA11F1F0A2BE21B5?method=download&shareKey=ed808ed2c8c0a189f9de3b23d3af0d85"  width=30%  height=30% />
<img src="https://note.youdao.com/yws/api/personal/file/43A138C3A80148CD8BA2CECA7A6FA8F7?method=download&shareKey=96c35465286f1bf250503d4d7e255c83"  width=30%  height=30% />
</center>
3. 从1和2的观点来看，那么对于由N个棋子构成的矩形“炮消除”为多少呢？

## 文件解释
> * problem_solver.py  
  对于给定的矩形获得最高的分数也即最少的剩子  
> * run_game.py  
  运行游戏，自行选择棋局大小和其实位置后，按上 下 左 右键即可开始游戏