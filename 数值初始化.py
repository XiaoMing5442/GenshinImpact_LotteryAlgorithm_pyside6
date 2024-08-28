#导包
import XiaoMing
import os

def History():# 重新加载历史文件
    #初始化History.json
    with open("D:/VScode/python_document/原神抽卡模拟内核/Data/History/History.json",mode="w+") as History_File:
        History_File.write('{"ThreeStar":[],"FourStar":[],"FiveStar":[]}')
def Today():# 删除今天的文件
    #列出今天的文件
    TodayPathFile = os.listdir("D:/VScode/python_document/原神抽卡模拟内核/Data/Today/")
    print(TodayPathFile)
    #删除今天的文件
    # 挨个删for循环
    for TodayFile in TodayPathFile:
        XiaoMing.delete(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Today/{TodayFile}")
def Mode(number:int,mode:bool):# number表示的是当前要删除的模式序号，如果mode为True，那么就初始化所有文件
    if mode:#检测模式
        #列出模式文件
        ModePathFile = os.listdir("D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/")
        print(ModePathFile)
        #删除模式文件
        # 挨个删for循环
        for ModeFile in ModePathFile:
            XiaoMing.delete(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/{ModeFile}")
        # 挨着初始化
        for i in range(19):
            #初始化mode*.json
            with open(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/mode{i+2}.json",mode="w+") as mode_file:
                mode_file.write('{"ThreeStar":[],"FourStar":[],"FiveStar":[]}')
        # 单独生成mode1.json加载原神原版数据
        with open(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/mode1.json",mode="w+",encoding="utf-8") as mode_file:
            mode_file.write('{"ThreeStar": ["\u5f39\u5f13", "\u9e26\u7fbd\u5f13", "\u8ba8\u9f99\u82f1\u6770\u8c2d", "\u9ed1\u7f28\u67aa", "\u6c90\u6d74\u9f99\u8840\u7684\u5251", "\u98de\u5929\u5fa1\u5251", "\u51b7\u5203", "\u795e\u5c04\u624b\u4e4b\u8a93", "\u7fe1\u7389\u6cd5\u7403", "\u9b54\u5bfc\u7eea\u8bba", "\u4ee5\u7406\u670d\u4eba", "\u94c1\u5f71\u9614\u5251", "\u9ece\u660e\u795e\u5251"], "FourStar": ["\u83b1\u4f9d\u62c9", "\u574e\u8482\u4e1d", "\u591a\u8389", "\u67ef\u83b1", "\u4e45\u5c90\u5fcd", "\u4e91\u5807", "\u9e7f\u91ce\u9662\u5e73\u85cf", "\u4e5d\u6761\u88df\u7f57", "\u4e94\u90ce", "\u65e9\u67da", "\u6258\u9a6c", "\u70df\u7eef", "\u7f57\u838e\u8389\u4e9a", "\u8f9b\u7131", "\u7802\u7cd6", "\u8fea\u5965\u5a1c", "\u91cd\u4e91", "\u8bfa\u827e\u5c14", "\u73ed\u5c3c\u7279", "\u83f2\u8c22\u5c14", "\u51dd\u5149", "\u884c\u79cb", "\u5317\u6597", "\u9999\u83f1", "\u5b89\u67cf", "\u96f7\u6cfd", "\u51ef\u4e9a", "\u82ad\u82ad\u62c9", "\u4e3d\u838e", "\u5f13\u85cf", "\u796d\u793c\u5f13", "\u7edd\u5f26", "\u897f\u98ce\u730e\u5f13", "\u662d\u5fc3", "\u796d\u793c\u6b8b\u7ae0", "\u6d41\u6d6a\u4e50\u7ae0", "\u897f\u98ce\u79d8\u5178", "\u897f\u98ce\u957f\u67aa", "\u5323\u91cc\u706d\u8fb0", "\u96e8\u88c1", "\u796d\u793c\u5927\u5251", "\u949f\u5251", "\u897f\u98ce\u5927\u5251", "\u5323\u91cc\u9f99\u541f", "\u796d\u793c\u5251", "\u7b1b\u5251", "\u897f\u98ce\u5251"], "FiveStar": ["\u63d0\u7eb3\u91cc", "\u523b\u6674", "\u83ab\u5a1c", "\u4e03\u4e03", "\u8fea\u5362\u514b", "\u7434", "\u963f\u83ab\u65af\u4e4b\u5f13", "\u5929\u7a7a\u4e4b\u7ffc", "\u56db\u98ce\u539f\u5178", "\u5929\u7a7a\u4e4b\u5377", "\u548c\u749e\u9e22", "\u5929\u7a7a\u4e4b\u810a", "\u72fc\u7684\u672b\u8def", "\u5929\u7a7a\u4e4b\u50b2", "\u5929\u7a7a\u4e4b\u5203", "\u98ce\u9e70\u5251"]}')
        # 单独生成mode2.json加载星穹铁道原版数据
        with open(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/mode2.json",mode="w+",encoding="utf-8") as mode_file:
            mode_file.write('{"ThreeStar": ["\u950b\u955d", "\u7269\u7a70", "\u5929\u503e", "\u7425\u73c0", "\u5e7d\u9083", "\u9f50\u9882", "\u667a\u5e93", "\u79bb\u5f26", "\u5609\u679c", "\u4e50\u572e", "\u620d\u5fa1", "\u6e0a\u73af", "\u8f6e\u5951", "\u7075\u94a5", "\u76f8\u6297", "\u8543\u606f", "\u4ff1\u6b81", "\u5f00\u7586", "\u533f\u5f71", "\u8c03\u548c", "\u777f\u89c1"], "FourStar": ["\u4e09\u6708\u4e03", "\u4e39\u6052", "\u963f\u5170", "\u827e\u4e1d\u59b2", "\u9ed1\u5854", "\u5a1c\u5854\u838e", "\u5e0c\u9732\u74e6", "\u4f69\u62c9", "\u6851\u535a", "\u864e\u514b", "\u7d20\u88f3", "\u9752\u96c0", "\u505c\u4e91", "\u4e00\u573a\u672f\u540e\u5bf9\u8bdd", "\u665a\u5b89\u4e0e\u7761\u989c", "\u4f59\u751f\u7684\u7b2c\u4e00\u5929", "\u552f\u6709\u6c89\u9ed8", "\u8bb0\u5fc6\u4e2d\u7684\u6a21\u6837", "\u9f39\u9f20\u515a\u6b22\u8fce\u4f60", "\u2308\u6211\u230b\u7684\u8bde\u751f", "\u540c\u4e00\u79cd\u5fc3\u60c5", "\u730e\u7269\u7684\u89c6\u7ebf", "\u6717\u9053\u7684\u9009\u62e9", "\u8bba\u5251", "\u4e0e\u884c\u661f\u76f8\u4f1a", "\u79d8\u5bc6\u8a93\u5fc3", "\u522b\u8ba9\u4e16\u754c\u9759\u4e0b\u6765", "\u6b64\u65f6\u6070\u597d", "\u821e\uff01\u821e\uff01\u821e\uff01", "\u5728\u84dd\u5929\u4e0b", "\u5929\u624d\u4eec\u7684\u4f11\u61a9"], "FiveStar": ["\u59ec\u5b50", "\u74e6\u5c14\u7279", "\u5e03\u6d1b\u59ae\u5a05", "\u6770\u5e15\u5fb7", "\u514b\u62c9\u62c9", "\u5f66\u537f", "\u767d\u9732", "\u94f6\u6cb3\u94c1\u9053\u4e4b\u591c", "\u65e0\u53ef\u53d6\u4ee3\u7684\u4e1c\u897f", "\u4f46\u6218\u6597\u8fd8\u672a\u7ed3\u675f", "\u4ee5\u4e16\u754c\u4e4b\u540d", "\u5236\u80dc\u7684\u77ac\u95f4", "\u5982\u6ce5\u9163\u7720", "\u65f6\u8282\u4e0d\u5c45"]}')
        # 别忘了NowMode.json
        with open(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/NowMode",mode="w+") as NowMode_file:
            NowMode_file.write("mode1")
    else:
        #初始化mode*.json
        with open(f"D:/VScode/python_document/原神抽卡模拟内核/Data/Mode/mode{number}.json",mode="w+") as mode_file:
            mode_file.write('{"ThreeStar":[],"FourStar":[],"FiveStar":[]}')
def main():# 全体初始化
    Mode(0,1)
    History()
    Today()
# 运行
if __name__ == "__main__":
    main()    