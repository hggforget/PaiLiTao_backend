import time
from tkinter import StringVar, IntVar

from Execute import startSearch01


def start(var1,var2,var3):
        # 搜图开【新进程没啥用】
        time_start=time.time()#time.time()为1970.1.1到当前时间的毫秒数
        #搜图开【新进程没啥用】
        imgs=startSearch01(var1, var2, var3)  # 单层文件夹
        '''
         if numberChosen.current() == 0 :
            if var5.get()==1 :
                Execute.startSearch01(var1, var2, var3, tree, x, root)#单层文件夹
            else:
                Execute.startSearch0(var1,var2,var3,tree,x,root)#多层文件夹
        elif numberChosen.current() == 1 :
            Execute.startSearch1(var1,var2,var3,tree,x,root)
        elif numberChosen.current() == 2 :
            Execute.startSearch2(var1,var2,var3,tree,x,root)
        elif numberChosen.current() == 3 :
            Execute.startSearch3(var1,var2,var3,tree,x,root)
        elif numberChosen.current() == 4 :
            Execute.startSearch4(var1,var2,var3,tree,x,root)
        elif numberChosen.current() == 5 :
            Execute.startSearch5(var1,var2,var3,tree,x,root)
        elif numberChosen.current() == 6 :
            Execute.startSearch6(var1,var2,var3,tree,x,root)
        else :
            return
        '''

        time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
        '''
            #自动筛选
        if (var4_1.get()==1):
            sieve()

        '''
        return imgs