################################################################
'''
关于此程序
作者:B站@XiaoMing5442:https://space.bilibili.com/455779705
其中均为自己编写，使用本代码请先获得授权
qq:1810311796


使用本代码请保留以上信息
'''
################################################################

# 导包
#-*- coding:UTF-8 -*-
import json
import logging
import os
import random
import sys
import time
from logging import info

import XiaoMing
from PySide6 import QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox

# 确定共同路径,由于vscode中使用绝对路径,为保证程序不会因路径更改而导致报错
path_Num = sys.argv[0].rfind("\\")
PaTh = sys.argv[0]
Same_Path = PaTh[0:path_Num]

# 全局变量
ModeNumber = None
ModeData = None
HistoryDict = None
TodayDict = None
# 以下的全局变量不会再在帮助文档中提到,仅作切换窗口用
main_win1 = None
main_win2 = None
main_win3 = None
main_win4 = None
main_win5 = None
main_win6 = None
main_win7 = None
main_win8 = None
main_win9 = None
main_win10 = None
main_win11 = None

# logging日志模块配置
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

class Start():# 主菜单类
    def __init__(self):# 主菜单
        super().__init__()
        window=QFile(f'{Same_Path}/ui/main.ui')
        window.open(QFile.ReadOnly)
        window.close()
        self.ui=QUiLoader().load(window)
        # 显示数据
        self.FindDaTa()
        # 按键
        self.ui.about.clicked.connect(self.AbOut)
        self.ui.mode.clicked.connect(self.MoDe)
        self.ui.Start_only.clicked.connect(self.LottERy)
        self.ui.Start_batch.clicked.connect(self.SomeLottERy)
        self.ui.Exit.clicked.connect(self.Exit)
    def FindDaTa(self):# 用于加载并显示抽卡数据
        # 寻找在Today文件夹下面有没有今天的文件，来判断是不是今天第一次登陆
        toDaY_File = f'{XiaoMing.str_today()}.json'
        Today_listpath =  os.listdir(f'{Same_Path}/Data/Today')
        # 判断有没有今天的文件
        if XiaoMing.ListElement_exist(Today_listpath,toDaY_File):
            pass
        else:
            # 创建一个新文件,并写入基本数据防止报错,另外,检测还有没有别的文件,并把别的文件移入History文件夹
            with open(f'{Same_Path}/Data/Today/{toDaY_File}',mode="w+") as TodayFile:
                TodayFile.write('{"ThreeStar":[],"FourStar":[],"FiveStar":[]}')
            # 检测别的文件
            if Today_listpath:
                # 获取文件名
                YesterdayFileName = Today_listpath[0]
                # 读取文件
                with open(f'{Same_Path}/Data/Today/{YesterdayFileName}',mode="r") as YesterdayFile:
                    YesterdayFileContent = json.load(YesterdayFile)
                # 将之前的内容添加至History.json文件中(读写不能同时进行,先读后写)
                # 读 
                with open(f'{Same_Path}/Data/History/History.json',encoding='utf-8',mode="r") as HistoryFile:
                    # 读取昨天文件中的三个属性
                    HistoryFileContent = json.load(HistoryFile)
                # 写
                with open(f'{Same_Path}/Data/History/History.json',encoding='utf-8',mode="w+") as HistoryFile:
                    # 将它们写入到历史文件
                    ##########历史##########
                    # 历史三星
                    HistoryThreeStars = HistoryFileContent["ThreeStar"]
                    # 历史四星
                    HistoryFourStars = HistoryFileContent["FourStar"]
                    # 历史五星
                    HistoryFiveStars = HistoryFileContent["FiveStar"]
                    # 输出日志
                    info(f"HistoryThreeStars:{HistoryThreeStars}")
                    info(f"HistoryFourStars:{HistoryFourStars}")
                    info(f"HistoryFiveStars:{HistoryFiveStars}")
                    ##########昨天##########
                    # 昨天三星
                    YesterdayThreeStars = YesterdayFileContent["ThreeStar"]
                    # 昨天四星
                    YesterdayFourStars = YesterdayFileContent["FourStar"]
                    # 昨天五星
                    YesterdayFiveStars = YesterdayFileContent["FiveStar"]
                    # 输出日志
                    info(f"YesterdayThreeStars:{YesterdayThreeStars}")
                    info(f"YesterdayFourStars:{YesterdayFourStars}")
                    info(f"YesterdayFiveStars:{YesterdayFiveStars}")
                    ##########总体##########
                    # 分别三四五星
                    ThreeStars = HistoryThreeStars + YesterdayThreeStars
                    FourStars = HistoryFourStars + YesterdayFourStars
                    FiveStars = HistoryFiveStars + YesterdayFiveStars
                    # 输出日志
                    info(f"ThreeStars:{ThreeStars}")
                    info(f"FourStars:{FourStars}")
                    info(f"FiveStars:{FiveStars}")
                    info("{" + f'"ThreeStar":{ThreeStars},"FourStar":{FourStars},"FiveStar":{FiveStars}' + "}")
                    # 写入
                    # 打包
                    global HistoryDict
                    HistoryDict = {"ThreeStar":ThreeStars,"FourStar":FourStars,"FiveStar":FiveStars}
                    # 写入
                    json.dump(HistoryDict,HistoryFile)
                # 把旧文件删除
                XiaoMing.delete(f'{Same_Path}/Data/Today/{YesterdayFileName}')

        # 读取今天的数据
        with open(f'{Same_Path}/Data/Today/{toDaY_File}',encoding='utf-8',mode="r") as TodayFile:
            # 将读取到的文件数据转化成字典,并储存在TodayDict这个全局变量中
            global TodayDict
            TodayDict = json.load(TodayFile)
            info(f'今天数据{TodayDict}')
        # 读取历史的数据
        with open(f'{Same_Path}/Data/History/History.json',encoding='utf-8',mode="r") as HistoryFile:
            # 将读取到的文件数据转化成字典,并储存在HistortDict这个全局变量中
            HistoryDict = json.load(HistoryFile)
            info(f'历史数据{HistoryDict}')
        # 运行显示函数
        self.ShOwDaTa()
    # 显示抽卡信息
    def ShOwDaTa(self):
        # 今天三项指标
        TodayThreeStars = TodayDict["ThreeStar"]
        TodayFourStars = TodayDict["FourStar"]
        TodayFiveStars = TodayDict["FiveStar"]
        TodaySumStars = len(TodayThreeStars) + len(TodayFourStars) + len(TodayFiveStars)
        # 判断除数是否为0,如果是,则+1
        if TodaySumStars:
            TodayDivisorStars = TodaySumStars
        else:
            TodayDivisorStars = TodaySumStars + 1
        # 打印
        self.ui.ShowToday.append(f"""三星角色数量:{len(TodayThreeStars)}\n四星角色数量:{len(TodayFourStars)}\n五星角色数量:{len(TodayFiveStars)}\n\n抽卡总数:{TodaySumStars}\n三星出率:{round(((len(TodayThreeStars)/TodayDivisorStars)*100),2)}%\n四星出率:{round(((len(TodayFourStars)/TodayDivisorStars)*100),2)}%\n五星出率:{round(((len(TodayFiveStars)/TodayDivisorStars)*100),2)}%""")
        
        # 历史三项指标
        HistoryThreeStars = HistoryDict["ThreeStar"]
        HistoryFourStars = HistoryDict["FourStar"]
        HistoryFiveStars = HistoryDict["FiveStar"]
        HistorySumStars = len(HistoryThreeStars) + len(HistoryFourStars) + len(HistoryFiveStars)
        # 判断除数是否为0,如果是,则+1
        if HistorySumStars:
            HistoryDivisorStars = HistorySumStars
        else:
            HistoryDivisorStars = HistorySumStars + 1
        # 打印
        self.ui.ShowHistory.append(f"""三星角色数量:{len(HistoryThreeStars)}\n四星角色数量:{len(HistoryFourStars)}\n五星角色数量:{len(HistoryFiveStars)}\n\n抽卡总数:{HistorySumStars}\n三星出率:{round(((len(HistoryThreeStars)/HistoryDivisorStars)*100),2)}%\n四星出率:{round(((len(HistoryFourStars)/HistoryDivisorStars)*100),2)}%\n五星出率:{round(((len(HistoryFiveStars)/HistoryDivisorStars)*100),2)}%""")
    def AbOut(self):# 用于打开关于窗口
        global main_win1
        main_win1 = About()
        # 显示新窗口
        main_win1.ui.show()
        # 关闭自己
        self.ui.close()
    def MoDe(self):# 用于打开定义模式的窗口
        global main_win3
        main_win3 = Mode()
        # 显示新窗口
        main_win3.ui.show()
        # 关闭自己
        self.ui.close()
    def LottERy(self):# 打开单抽界面
        global main_win8
        main_win8 = Lottery()
        # 显示新窗口
        main_win8.ui.show()
        # 关闭自己
        self.ui.close()
    def SomeLottERy(self):# 打开多抽界面
        global main_win10
        main_win10 = SomeLottery()
        # 显示新窗口
        main_win10.ui.show()
        # 关闭自己
        self.ui.close()
    def Exit(self):# 退出
        exit()
class About():# 关于类
    def __init__(self):# 关于窗口
        super().__init__()
        window=QFile(f'{Same_Path}/ui/about.ui')
        window.open(QFile.ReadOnly)
        window.close
        self.ui=QUiLoader().load(window)
        # 按下返回键
        self.ui.return_2.clicked.connect(self.ReTuRn)
    def ReTuRn(self):# 返回到主菜单
        global main_win2
        main_win2 = Start()
        # 显示新窗口
        main_win2.ui.show()
        # 关闭自己
        self.ui.close()
class Mode():# 定义模式
    def __init__(self) -> None:# 模式窗口
        super().__init__()
        window=QFile(f'{Same_Path}/ui/mode.ui')
        window.open(QFile.ReadOnly)
        window.close
        self.ui=QUiLoader().load(window)
        # 修改选择框
        self.ui.mode.currentIndexChanged.connect(self.LoadData)
        # 按下退出
        self.ui.return_2.clicked.connect(self.ReTurN)
        # 选择修改
        self.ui.change.clicked.connect(self.ChanGe)
        pass
    def LoadData(self):# 加载数据
        info("选择框更改!")
        # 删除原先内容
        self.ui.three.setPlainText("")
        self.ui.four.setPlainText("")
        self.ui.five.setPlainText("")
        # 读取选择框数据
        mode_text = self.ui.mode.currentText()
        if mode_text == "none":# 检测选中对象是不是无用项
            info("选中无用项")
        else:
            # 打开文件读取数据
            with open(f'{Same_Path}/Data/Mode/{mode_text}.json',mode="r") as Mode_File:
                global ModeData
                ModeData = json.load(Mode_File)
            # 读取数据
            ModeThree = ModeData["ThreeStar"]
            ModeFour = ModeData["FourStar"]
            ModeFive = ModeData["FiveStar"]
            # 打印日志
            info(f"ModeThree:{ModeThree}")
            info(f"ModeFour:{ModeFour}")
            info(f"ModeFive:{ModeFive}")
            # 输出
            # 三星
            for three in ModeThree:
                self.ui.three.append(str(three))
            # 四星
            for four in ModeFour:
                self.ui.four.append(str(four))
            # 五星
            for five in ModeFive:
                self.ui.five.append(str(five))
    def ReTurN(self):#返回
        # 读取当前选项，将其设为默认
        mode_text = self.ui.mode.currentText()
        if mode_text == "none":# 检测选中对象是不是无用项
            info("无用项,无法设置")
        else:
            with open(f'{Same_Path}/Data/Mode/NowMode',mode="w") as NowModeFile:
                NowModeFile.write(mode_text)
            info(f"成功将{mode_text}设为默认")
        global main_win4
        main_win4 = Start()
        # 显示新窗口
        main_win4.ui.show()
        # 关闭自己
        self.ui.close()
    def ChanGe(self):# 切换到更改窗口
        mode_text = self.ui.mode.currentText()
        # 全局
        global ModeNumber
        ModeNumber = mode_text
        if mode_text == "none":# 检测选中对象是不是无用项
            # 弹出错误提示
            QMessageBox.critical(self.ui,'Error','我叼你mb,就你tm喜欢卡bug是不是?')
        else:
            global main_win5
            main_win5 = ModeWrite()
            # 显示新窗口
            main_win5.ui.show()
            # 关闭自己
            self.ui.close()
class ModeWrite():# 用来修改模式文件
    def __init__(self) -> None:# 修改模式窗口
        super().__init__()
        window=QFile(f'{Same_Path}/ui/mode_write.ui')
        window.open(QFile.ReadOnly)
        window.close
        self.ui=QUiLoader().load(window)
        # 加载数据
        self.LoadData()
        # 按下退出
        self.ui.Exit.clicked.connect(self.Exit)
    def LoadData(self):
        # 获取之前显示的内容再次显示
        # 读取数据
        ModeThree = ModeData["ThreeStar"]
        ModeFour = ModeData["FourStar"]
        ModeFive = ModeData["FiveStar"]
        # 打印日志
        info(f"ModeThree:{ModeThree}")
        info(f"ModeFour:{ModeFour}")
        info(f"ModeFive:{ModeFive}")
        # 输出
        # 三星
        for three in ModeThree:
            self.ui.three.append(str(three))
        # 四星
        for four in ModeFour:
            self.ui.four.append(str(four))
        # 五星
        for five in ModeFive:
            self.ui.five.append(str(five))
    def Exit(self):# 退出
        # 保存
        save = {"ThreeStar":self.ui.three.toPlainText().splitlines(),"FourStar":self.ui.four.toPlainText().splitlines(),"FiveStar":self.ui.five.toPlainText().splitlines()}
        # 打开文件写数据
        with open(f'{Same_Path}/Data/Mode/{ModeNumber}.json',mode="w") as Mode_File:
            json.dump(save,Mode_File)
        info(f"保存内容:{save}")
        # 切换窗口
        global main_win7
        main_win7 = Start()
        # 显示新窗口
        main_win7.ui.show()
        # 关闭自己
        self.ui.close()
class Lottery():# 抽个奖奖
    def __init__(self) -> None:# 抽奖
        super().__init__()
        window=QFile(f'{Same_Path}/ui/lottery.ui')
        window.open(QFile.ReadOnly)
        window.close
        self.ui=QUiLoader().load(window)
        # 定义两个记录变量
        self.Fourno = 0
        self.Fiveno = 0
        # 定义空列表
        self.NowThreeStars = []
        self.NowFourStars = []
        self.NowFiveStars = []
        # 检测按键按下
        self.ui.start.clicked.connect(self.StArt)# 开始
        self.ui.Exit.clicked.connect(self.SaVe_Exit)# 退出
    def StArt(self):# 开始抽奖
        # 检测模式中是否存在空的项目
        # 获得模式
        with open(f'{Same_Path}/Data/Mode/NowMode',mode="r") as Mode_File:
            mode = Mode_File.read()
        # 读取文件
        with open(f'{Same_Path}/Data/Mode/{mode}.json',mode="r") as Mode_File:
            RoleDict = json.load(Mode_File)
        # 写进变量
        ThreeStar = RoleDict['ThreeStar']
        FourStar = RoleDict["FourStar"]
        FiveStar = RoleDict["FiveStar"]
        # 判断是否为空
        if ThreeStar and FourStar and FiveStar:
            info("准备执行抽奖")
            Package = self.LotteryFunction((ThreeStar,FourStar,FiveStar),self.Fourno,self.Fiveno)
            info(f"Package = {Package}")
            self.Fiveno = Package[2]
            self.Fourno = Package[1]
            # 清除屏幕数据
            self.ui.Text.clear()
            # 判断四五星未出次数是否为0,如果是,那么就是这抽的角色是四五星
            if not self.Fiveno:
                self.NowFiveStars.append(Package[0])
                # 显示当前是五星
                self.ui.Text.append(f"当前抽出五星:{Package[0]}")
            elif not self.Fourno:
                self.NowFourStars.append(Package[0])
                # 显示当前是四星
                self.ui.Text.append(f"当前抽出四星:{Package[0]}")
            else:
                self.NowThreeStars.append(Package[0])
                # 显示当前是三星
                self.ui.Text.append(f"当前抽出三星:{Package[0]}")
            info(f"三星:{self.NowThreeStars}")
            info(f"四星:{self.NowFourStars}")
            info(f"五星:{self.NowFiveStars}")
            # 打印数据
            当前总抽卡数 = len(self.NowThreeStars)+len(self.NowFourStars)+len(self.NowFiveStars)
            self.ui.Text.append(f"总次数:{当前总抽卡数}")
            self.ui.Text.append(f"三星数量:{len(self.NowThreeStars)}")
            self.ui.Text.append(f"四星数量:{len(self.NowFourStars)}")
            self.ui.Text.append(f"五星数量:{len(self.NowFiveStars)}")
            self.ui.Text.append(f"三星出率:{round(((len(self.NowThreeStars)/当前总抽卡数)*100),2)}%")
            self.ui.Text.append(f"四星出率:{round(((len(self.NowFourStars)/当前总抽卡数)*100),2)}%")
            self.ui.Text.append(f"五星出率:{round(((len(self.NowFiveStars)/当前总抽卡数)*100),2)}%")
        else:
            info("正在尝试使用空项目!")
            # 弹出错误提示
            QMessageBox.critical(self.ui,'Error','nm戈壁,你知道修bug要多久吗,nnd')
    def LotteryFunction(self,Role:tuple,FourNO:int,FiveNO:int):# 抽奖算法
        """
        Role是指角色库,排列顺序为三星,四星,五星元组
        概率存储为千分数
        FourNO,FiveNO表示的是距离上一次出四五星有多久了,比如上抽才出,那么在这一抽时这个值就是1
        输出格式:(角色名,四星未出次数,五星未出次数)
        """
        # 拆包,读取数据
        ThreeStar = Role[0]
        FourStar = Role[1]
        FiveStar = Role[2]
        # 从第74抽之后的概率
        # 五星
        FIVEODDS = (66,126,186,246,306,366,426,486,546,606,666,726,786,846,906,966,1000)
        # 四星,从9抽开始
        FOURODDS= (561,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000)
        # 总概率是1000,先对1000进行分配,五星标准概率6,四星标准概率51
        # 五星挤四星,剩下的就是三星,如果没有剩下的,那么就只有四星五星或只有五星
        if FiveNO < 74:
            Fiveodd = 6
        else:
            Fiveodd = FIVEODDS[FiveNO-73]
        if FourNO < 9:
            Fourodd = 51
        else:
            Fourodd = FOURODDS[FourNO-8]
        # 计算总数
        all = Fourodd + Fiveodd
        # 判断是否大于1000
        if all > 1000:
            # 主程序
            num = random.randint(1,1000)
            info(f"生成的随机数{num}")
            if num > Fiveodd:
                # 这是四星
                # 读取四星库,输出最终结果
                fournum = random.randint(0,len(FourStar)-1)
                returnfour = FourStar[fournum]
                fourno = 0
                FiveNO += 1
                return (returnfour,fourno,FiveNO) 
            else:
                # 这是五星
                # 读取五星库,输出最终结果
                fivenum = random.randint(0,len(FiveStar)-1)
                returnfive = FiveStar[fivenum]
                FourNO += 1
                fiveno = 0
                return (returnfive,FourNO,fiveno) 
        else:
            # 主程序
            num = random.randint(1,1000)
            info(f"生成的随机数{num}")
            # 判断是不是五星
            if num > Fiveodd:
                # 这是四星或三星
                Fourodd = Fourodd + Fiveodd
                if num > Fourodd:
                    # 这是三星
                    # 读取三星库,输出最终结果
                    threenum = random.randint(0,len(ThreeStar)-1)
                    returnthree = ThreeStar[threenum]
                    FourNO += 1
                    FiveNO += 1
                    return (returnthree,FourNO,FiveNO) 
                else:
                    # 这是四星
                    # 读取四星库,输出最终结果
                    fournum = random.randint(0,len(FourStar)-1)
                    returnfour = FourStar[fournum]
                    fourno = 0
                    FiveNO += 1
                    return (returnfour,fourno,FiveNO) 
            else:
                # 这是五星
                # 读取五星库,输出最终结果
                fivenum = random.randint(0,len(FiveStar)-1)
                returnfive = FiveStar[fivenum]
                FourNO += 1
                fiveno = 0
                return (returnfive,FourNO,fiveno)
    def SaVe_Exit(self):# 退出和保存
        with open(f'{Same_Path}/Data/Today/{XiaoMing.str_today()}.json',mode="w") as Today_File:
            global TodayDict
            info(f"{TodayDict}")
            # read
            TodayThreeStars = TodayDict["ThreeStar"]
            TodayFourStars = TodayDict["FourStar"]
            TodayFiveStars = TodayDict["FiveStar"]
            # 添加刚刚的内容
            TodayThreeStars.extend(self.NowThreeStars)
            TodayFourStars.extend(self.NowFourStars)
            TodayFiveStars.extend(self.NowFiveStars)
            # 打包
            TodayDict = {"ThreeStar":TodayThreeStars,"FourStar":TodayFourStars,"FiveStar":TodayFiveStars}
            # 写入
            json.dump(TodayDict,Today_File)
        # 返回主菜单
        # 切换窗口
        global main_win9
        main_win9 = Start()
        # 显示新窗口
        main_win9.ui.show()
        # 关闭自己
        self.ui.close()
class SomeLottery():# 抽一些奖
    def __init__(self):# 抽一些奖窗口
        super().__init__()
        window=QFile(f'{Same_Path}/ui/somelottery.ui')
        window.open(QFile.ReadOnly)
        window.close
        self.ui=QUiLoader().load(window)
        # 定义两个记录变量
        self.Fourno = 0
        self.Fiveno = 0
        # 定义空列表
        self.NowThreeStars = []
        self.NowFourStars = []
        self.NowFiveStars = []
        # 设置进度条
        self.ui.progressBar.setRange(0,100)
        self.ui.progressBar.setValue(0)
        # 检测按键按下
        self.ui.Start.clicked.connect(self.StArt)# 开始
        self.ui.Exit.clicked.connect(self.SaVe_Exit)# 退出
    def StArt(self):
        # 检测输入数据是否大于1000
        number = int(self.ui.Edit.text())
        if number > 1000:
            info("尝试输入非法内容")
            # 弹出错误提示
            QMessageBox.critical(self.ui,'Error','就你不听劝?')
        else:
            # 设置进度条
            self.ui.progressBar.setRange(0,number)
            info(f"number = {number}")
            # 导入在Lottery中的函数
            lottery = Lottery()
            # 检测模式中是否存在空的项目
            # 获得模式
            with open(f'{Same_Path}/Data/Mode/NowMode',mode="r") as Mode_File:
                mode = Mode_File.read()
            # 读取文件
            with open(f'{Same_Path}/Data/Mode/{mode}.json',mode="r") as Mode_File:
                RoleDict = json.load(Mode_File)
            # 写进变量
            ThreeStar = RoleDict['ThreeStar']
            FourStar = RoleDict["FourStar"]
            FiveStar = RoleDict["FiveStar"]
            # 判断是否为空
            if ThreeStar and FourStar and FiveStar:
                for i in range(number):
                    info("准备执行抽奖")
                    Package = lottery.LotteryFunction((ThreeStar,FourStar,FiveStar),self.Fourno,self.Fiveno)
                    info(f"Package = {Package}")
                    self.Fiveno = Package[2]
                    self.Fourno = Package[1]
                    # 清除屏幕数据
                    self.ui.Text.clear()
                    # 判断四五星未出次数是否为0,如果是,那么就是这抽的角色是四五星
                    if not self.Fiveno:
                        self.NowFiveStars.append(Package[0])
                        # 显示当前是五星
                        self.ui.Text.append(f"当前抽出五星:{Package[0]}")
                    elif not self.Fourno:
                        self.NowFourStars.append(Package[0])
                        # 显示当前是四星
                        self.ui.Text.append(f"当前抽出四星:{Package[0]}")
                    else:
                        self.NowThreeStars.append(Package[0])
                        # 显示当前是三星
                        self.ui.Text.append(f"当前抽出三星:{Package[0]}")
                    info(f"三星:{self.NowThreeStars}")
                    info(f"四星:{self.NowFourStars}")
                    info(f"五星:{self.NowFiveStars}")
                    # 打印数据
                    当前总抽卡数 = len(self.NowThreeStars)+len(self.NowFourStars)+len(self.NowFiveStars)
                    self.ui.Text.append(f"总次数:{当前总抽卡数}")
                    self.ui.Text.append(f"三星数量:{len(self.NowThreeStars)}")
                    self.ui.Text.append(f"四星数量:{len(self.NowFourStars)}")
                    self.ui.Text.append(f"五星数量:{len(self.NowFiveStars)}")
                    self.ui.Text.append(f"三星出率:{round(((len(self.NowThreeStars)/当前总抽卡数)*100),2)}%")
                    self.ui.Text.append(f"四星出率:{round(((len(self.NowFourStars)/当前总抽卡数)*100),2)}%")
                    self.ui.Text.append(f"五星出率:{round(((len(self.NowFiveStars)/当前总抽卡数)*100),2)}%")
                    # 设置进度条
                    self.ui.progressBar.setValue(i+1)
            else:
                info("正在尝试使用空项目!")
                # 弹出错误提示
                QMessageBox.critical(self.ui,'Error','nm戈壁,你知道修bug要多久吗,nnd')
    def SaVe_Exit(self):# 退出和保存
        with open(f'{Same_Path}/Data/Today/{XiaoMing.str_today()}.json',mode="w") as Today_File:
            global TodayDict
            info(f"{TodayDict}")
            # read
            TodayThreeStars = TodayDict["ThreeStar"]
            TodayFourStars = TodayDict["FourStar"]
            TodayFiveStars = TodayDict["FiveStar"]
            # 添加刚刚的内容
            TodayThreeStars.extend(self.NowThreeStars)
            TodayFourStars.extend(self.NowFourStars)
            TodayFiveStars.extend(self.NowFiveStars)
            # 打包
            TodayDict = {"ThreeStar":TodayThreeStars,"FourStar":TodayFourStars,"FiveStar":TodayFiveStars}
            # 写入
            json.dump(TodayDict,Today_File)
        # 返回主菜单
        # 切换窗口
        global main_win9
        main_win9 = Start()
        # 显示新窗口
        main_win9.ui.show()
        # 关闭自己
        self.ui.close()
# 显示窗口        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Start()
    window.ui.show()
    sys.exit(app.exec())