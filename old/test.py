import pickle
path = open('D:/MyRPG/data.dat','rb')
global dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang
dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang = pickle.load(path)
path.close()

print(xiguanall)
xiguanall = [['好习惯：每天对电脑的时候戴小眼镜。', '', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8, 2], ['好习惯：每月读非专业类书一到两本。', '坚持读书具有较好的属性加成，在完成目标的前提下：<br/>耐力加0.02，专注加0.05，智力加0.05，知识量加0.05。<br/>但是每天若花过多时间看闲书将导致扣分，因此你需要合理安排才能获得它。', 0.0, 0.0, 0.02, 0.05, 0.05, 0.05, 11, 3], ['好习惯：跑步一小时', '计算准备，跑步和回来的时间，你将获得<br/>体质0.04和耐力加成0.04。<br/>不能和运动一小时重复获得。', 0.04, 0.0, 0.04, 0.0, 0.0, 0.0, 11, 3], ['好习惯：坚持每日使用MyRPG', '玩游戏，送经验，不过当然只是意思一下。<br/>希望你能坚持使用这个软件。', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5, 1], ['好习惯：早睡早起（晚11点半前睡，早7点半前起。）', '由于你目前的作息习惯，这是一个困难级习惯。<br/>可获得耐力0.04的加成。', 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 11, 3], ['好习惯：坚持采用番茄工作法，并且在休息期间放松眼睛（证券交易时间可除外）。', '完成本习惯具有较高的专注加成（0.08），以及0.03的耐力加成。', 0.0, 0.0, 0.03, 0.08, 0.0, 0.0, 8, 2], ['好习惯：每天只吃健康的食品。', '一日三餐，不过饱，多吃蔬菜，多搭配，少量肉类蛋白质。<br/>暂时是这个标准，请关注更多关于食物的细节，来搭配适合自己的营养。', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8, 2], ['好习惯：写晨间日志。', '坚持写晨间日志，安排每天的计划回顾前一天<br/>的历程，进行反思。<br/>整个晨间日志不只是做一个日志，包含了MyRPG设定当天计划和完成任务，用Onenote来写一个具体的日志。', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8, 2], ['好习惯：运动一小时。', '运动一小时将增强体质和耐力，并获得较多经验。<br/>希望你每周能坚持四次。', 0.03, 0.0, 0.03, 0.0, 0.0, 0.0, 11, 3], ['好习惯：不抽烟。', '目前在戒烟当中，因此这是一个中等的好习惯。<br/>抽烟破坏身体健康和注意力，完成这个习惯，专注将加0.1。', 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 8, 2], ['好习惯：每天只坐中庭电梯，其他走楼梯。', '简单难度，获得经验和娱乐点，希望每日完成。', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5, 1], ['好习惯：每天上下的电梯全部不坐，走楼梯。', '中等难度，体质加0.02。', 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 8, 2], ['好习惯：做10个俯卧撑，做30个仰卧起坐。', '中等难度习惯，希望每天坚持。<br/>它可以让你的体质加0.01', 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 8, 2], ['坏习惯：上下班全部坐电梯。', '节约的时间毫无意义', -0.02, 0.0, 0.0, 0.0, 0.0, 0.0, -5, -2], ['坏习惯：吃夜宵', '吃了夜宵你觉得你能睡得好吗？', -0.01, 0.0, 0.0, 0.0, 0.0, 0.0, -6, -3], ['坏习惯：无故吃垃圾食品，包括喝碳酸饮料。', '体质-0.02，同时损失大量经验和娱乐点。<br/>不要功亏一篑。', -0.02, 0.0, 0.0, 0.0, 0.0, 0.0, -8, -3], ['坏习惯：花了许多时间在闲事情上，包括证券。', '每天花费过多时间用在看网页，新闻，股票，玩游戏等上。<br/>占用正常工作时间1小时以上就算。', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -8, -3], ['坏习惯：抽烟5根及5根以下。', '', -0.01, 0.0, 0.0, 0.0, 0.0, 0.0, -5, -2], ['坏习惯：抽烟5-10根，包括10根。', '体质-0.01，专注-0.01。', -0.01, 0.0, 0.0, -0.01, 0.0, 0.0, -8, -3], ['坏习惯：抽烟10根以上', '惩罚不小哦，经验-15，娱乐点-6，体质-0.02，专注-0.02，耐力-0.01。', -0.02, 0.0, -0.01, -0.02, 0.0, 0.0, -15, -6], ['坏习惯：临时扣分', '', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -20, -10]]
#print(rizhi[8][2])
#rizhi[58][2] = '浙江大学学报拒稿，希望渺茫，尽管如此我明天一定要争取申辩一下。然后选择期刊重新投稿，唉，always for the best。'

path = open('D:/MyRPG/data.dat','wb')
pickle.dump((dianshu,nengli,zhuangbei,xiguangeverday,xiguanall,renwu,renwufinish,rizhi,rizhifinish,jiangli,jiangliget,yuanwang),path)
path.close()
del path
