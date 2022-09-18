import Execute
def start():
    if var1.get()=='' or var2.get()=='' :
        tkinter.messagebox.askokcancel('啊欧','用此功能，图片以及文件夹的路径请完整填写')
        tabControl.select(0)#跳回第一个标签
        pass
    else :#路径合法，可以执行
        label3.config(text="正在处理……")
        Init_dog()#初始化图像显示
        delButton(tree)#清空表列
        showPic1()#预览所找图
        time_start=time.time()#time.time()为1970.1.1到当前时间的毫秒数
        #搜图开【新进程没啥用】
        if numberChosen.current() == 0 :
            if var5.get()==1 :
                '''
                th1=threading.Thread(target=Execute.startSearch01(var1,var2,var3,tree,x,root))
                th1.start()
                button_img.configure(state='disabled')  #万一时间长，防止按钮连续点击
                th1.join()
                button_img.configure(state='normal')
                '''
                Execute.startSearch01(var1,var2,var3,tree,x,root)#单层文件夹
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
            tkinter.messagebox.askokcancel('啊欧','算法未找到，也许正在制作中')
            return
        time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数
        label3.config(text="耗时"+str(round(time_end-time_start,3))+'秒')#显示耗时
        #自动筛选
        if (var4_1.get()==1):
            sieve()