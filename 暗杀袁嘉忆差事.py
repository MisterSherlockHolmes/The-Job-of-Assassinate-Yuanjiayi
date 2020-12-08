import easygui
import time
money=305000
death_reason=""
succeed=False
print("十字兄弟游戏行&刘宸煊制作工作室 出品")
time.sleep(1)
print("怀旧文字游戏系列")
time.sleep(1)
print("欢迎来到暗杀袁嘉忆差事")
time.sleep(1)
print("任务详情：将刚下飞机的袁嘉忆杀死，并将她的笔记、尸体和头颅运到港口，那里的船只将会将它们走私到中国北京。不要问我们为什么要走私，问就是躲避特朗普政府那高的离谱以至于会让我们的收入为负数的关税。")
time.sleep(2)
print("预计分红：￥305000")
time.sleep(0.5)
print("这是单人差事")
time.sleep(0.5)
mode=input("请选择模式\n A.气势汹汹 B.隐迹潜踪 C.兵不厌诈 现隐迹潜踪与兵不厌诈未开放\n")
#检验输入是否正确
if mode=="A":
	#mode="A" or "B" or "C"
	pass
else:
	print("请选择正确的模式！")
	mode=input("请选择模式\n A.气势汹汹 B.隐迹潜踪 C.兵不厌诈 现隐迹潜踪与兵不厌诈未开放\n")

if mode =="A":
	print("暗杀袁嘉忆差事：气势汹汹")
	weapon=easygui.choicebox("请选择武器","选择武器",["卡宾步枪","无托式步枪","火神机枪","火箭炮"])
	vehicle=easygui.choicebox("请选择载具","选择载具",["卡林 骷髅马（装甲版）","复仇者","佩洛西 暴君mk2","从詹姆士·邦德（007）特工那里借的车","丁卡 小型旅行家羽黑"])
	print("莱斯特：我们准备要出发了，嘟嘟")
	time.sleep(5)
	print("莱斯特：这可是个难以对付的暴力女孩，我看看你准备了什么，{}对吧？希望你不会后悔".format(weapon))
	time.sleep(5)
	print('刘宸煊：这个叫袁嘉忆的女孩子，是来摧毁我们的共和国的，也许她还会摧毁整个世界')
	time.sleep(5)
	print("刘宸煊：我们都很希望她死掉，她的笔记卖给某些对她有邪恶念头的人，可以捞很大一笔钱。她的尸体展览可以收很多门票费。")
	time.sleep(5)
	print("莱斯特：你要对付她和她的闺蜜军团。有一个好消息是她的闺蜜军团只有一些手枪，坏消息是袁嘉忆本人从苏联拿了火箭炮")
	time.sleep(5)
	print("袁嘉忆：你们都给爷爬，想杀我，没门。我的飞机已经降落了")
	time.sleep(5)
	print("袁嘉忆：老娘会把你们全杀光")
	time.sleep(5)
	print('刘宸煊：那你就来试试吧。')
	time.sleep(30)
	print("你已抵达机场")
	time.sleep(5)
	print("莱斯特：快去干掉她！！！哦，我紧张的感觉湿疹快要好了！")
	time.sleep(5)
	print("袁嘉忆一行人出现在你面前，向你冲了过来！！！你使用{}给她来了几发".format(weapon))
	time.sleep(3)
	if weapon=="火箭炮":
		print("袁嘉忆与她的闺蜜军团被炸成了灰，但是尸体损坏了一部分，分红-￥20000")
		money=money-20000
		print("路人报了警！！！快走！！！！")
		if vehicle == "丁卡 小型旅行家羽黑":
			print('你在车内被警察的子弹杀死了')
			death_reason="你 失败了"
			succeed=False
		else:
			print("你凭借精湛的驾驶技术将{}开到了港口，船只的烟囱冒着烟，向太平洋另一岸的文明古国，中国，航去。".format(vehicle))
			succeed=True
	elif weapon=="卡宾步枪" or "无托式步枪" or "火神机枪":
		print("袁嘉忆将你炸的血肉纷飞")
		#print("你凭借精湛的驾驶技术甩掉了警察将{}开到了港口，船只的烟囱冒着烟，向太平洋另一岸的文明古国，中国，航去。".format(vehicle))
		death_reason="你 因为在袁嘉忆面前装13被袁嘉忆使用暴力杀死了"
		succeed=False
	else:
		print("出现错误")
else:
	print("出现错误")
#if mode =="B":


#if mode =="C":
	
	
if succeed==True:
	print("暗杀袁嘉忆差事 成功")
	print(death_reason)
	print("预计分红：￥305000")
	print("实际分红：￥{}".format(money))
	print("不久后，你在报纸上看到袁嘉忆死于非命的消息")
	input("按下回车键 离开本游戏")
else:
	print("暗杀袁嘉忆差事 失败")
	print(death_reason)
	print("预计分红：￥305000")
	print("实际分红：￥0")
	input("按下回车键 离开本游戏")
