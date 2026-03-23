# 今日工作总结

## 项目名称：SSplayer

### 今日完成
- 在GPT辅助下明确了大致模型设计
- 完成了玩家状态类，敌人状态类，敌人总状态类（用于模型输入），攻击卡牌的统计与加载
- 完成了github仓库的创建与代码分支提交
- Git 操作步骤：
  - cd /项目路径
  - git init
  - git add .
  - git commit -m "提交说明内容"
  - ssh-keygen -t ed25519 -C "email@example.com"
  - 在仓库设置公钥
  - git remote set-url origin git@github.com:MaokoRei/SSplayer.git
  - git push -u origin master
  - 测试连接指令：ssh -T git@github.com

### 遇到的问题
- github的ssh连接

### 明日计划
1. 修改 attackcard 设计，将群攻改成 bool 判断，将攻击拆分为基本攻击和攻击段数，添加攻击目标是否随机 bool
2. 完成牌堆状态、状态修改方法并进行测试