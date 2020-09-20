# class listadd():
#     def __init__(self,list1):
#         self.list1 = list1

#     def __repr__(self):
#         return f'listadd(list3)'

#     def __add__(self,other):
#         len = len(self.list1)
#         for i in range(len):
#             list3[i] = self.list1[i] + other.list1[i]
# day 10
# import tkinter as tk

# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x100')#中间是x字母 长和宽

# var = tk.StringVar() #tk里面字符串的变量
# '''
# 这块是Label和Button
# '''
# l = tk.Label(window,textvariable = var,bg = 'green',font = ('Arial,12'),width = 15,height = 2)#对象都是大写的，类似Tk,Label
# #上面这个Label，现在用的是textvariable,也可以直接text = ""让他输出
# l.pack() #放置他，上或下或左或右

# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set("you hit me")
#     else:
#         on_hit = False
#         var.set("")

# b = tk.Button(window,text = 'hit me',width = 15,height = 1,
#     command = hit_me)

# b.pack()
# window.mainloop()#不断的刷新，很大的while循环，窗口文件必须要有类似的东西,这个东西放在最下面

'''
输入和文本框
'''
# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# e = tk.Entry(window,show = '*')
# #要变成输入密码的形式的话，改成show = '*'
# #show = None的话，就会显示
# e.pack()
# def insert_point():#放在指针位置处
#     var = e.get()
#     t.insert('insert',var)
# def insert_end():
#     var = e.get()
#     t.insert('end',var)#t.insert(1.1,var) 1.1是输出到Text第一行第一位(从零开始)

# b1 = tk.Button(window,text = 'insert point',width = 15,height = 2,
#     command = insert_point)
# b1.pack()

# b2 = tk.Button(window,text = 'insert end',
#     command = insert_end)
# b2.pack()

# t = tk.Text(window,height = 2)
# t.pack()

# window.mainloop()


'''
列表部件ListBox
'''
# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# var1 = tk.StringVar()
# l = tk.Label(window,bg = 'yellow',width = 4,textvariable = var1)
# l.pack()

# def print_selection():
#     # value = lb.get(lb.curselection())#拿出光标选中的东西
#     value = lb.get(lb.curselection())
#     # lb.get(lb.curselection())
#     var1.set(value)



# b1 = tk.Button(window,text = 'print selection',width = 15,height = 2,command = print_selection)
# b1.pack()

# var2 = tk.StringVar()
# var2.set((11,22,33,44))
# lb = tk.Listbox(window,listvariable = var2)
# list_items = [1,2,3,4]
# for item in list_items:
#     lb.insert('end',item)
# lb.insert(1,'first')
# lb.insert(2,'second')
# lb.delete(2)
# lb.pack()

# window.mainloop()

'''
Radiobutton选择按钮
'''
# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# # global var1
# var1 = tk.StringVar()
# # l = tk.Label(window,bg = 'yellow',width = 20,text = 'empty')
# l = tk.Label(window,bg = 'yellow',width = 20,textvariable = var1)

# l.pack()

# def print_selection():
#     # l.config(text = 'you have selected ' + var1.get())
#     #这个l.config是第一次用
#     # l.set(text = 'you have selected' + var1.get())
#     # global var1
#     var1 = 'you have selected' + var1.get()
#     # l.pack()
#     global var1
#     #还是应该l.config(text = 'you have selected ' + var1.get()) ，上面那块不用textvariable,用text
# r1 = tk.Radiobutton(window,text = 'Option A',
#     variable = var1,value = 'A',#当这个var1选这个r1的时候，他就会被赋值成A
#     command = print_selection)#print_selection后面没有括号
# r1.pack()

# r2 = tk.Radiobutton(window,text = 'Option B',
#     variable = var1,value = 'B',
#     command = print_selection)
# #当这个var1选这个r1的时候，他就会被赋值成A
# r2.pack()

# r3 = tk.Radiobutton(window,text = 'Option C',
#     variable = var1,value = 'C',
#     command = print_selection)
# #当这个var1选这个r1的时候，他就会被赋值成A
# r3.pack()

# window.mainloop()


'''
Scale尺度,就是被拉动的一个条，返回一个数字
'''
# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# l = tk.Label(window,bg = 'yellow',width = 20,text = 'emtpy')
# l.pack()

# def print_selection(v):
#     l.config(text = 'you have selected' + v)
# s = tk.Scale(window,label = 'try me',from_ = 5,to = 11,orient = tk.HORIZONTAL,length = 200,showvalue = 0,tickinterval = 3,resolution = 0.01,
#     command = print_selection)
# #这边这个宽度是像素的宽度   方向：横向  showvalue = 0就是不显示
# #tickinterval是标签的单位长度(也就是隔多少个单位显示一个数值)resolution = 0.01就是保留两位小说
# #Scale这个print_selection是有一个默认的传入值的，就是Scale标签标注的那个值
# s.pack()
# window.mainloop()

'''
Checkbutton 勾选框，所有的都可以被勾选
'''
# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# l = tk.Label(window,bg = 'yellow',width = 20,text = 'emtpy')
# l.pack()

# def print_selection():
#     if(var1.get() == 1)&(var2.get() == 0):
#         l.config(text ='I only love Python')
#     elif(var1.get() == 0)&(var2.get() == 1):
#         l.config(text = 'I only love C++')
#     elif(var1.get() == 0)&(var2.get() == 0):
#         l.config(text = 'I do not love either')
#     else:
#         l.config(text = 'I love both')

# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window,text = 'Python',variable = var1,
#     onvalue = 1,offvalue = 0,command = print_selection)
# #选中c1那么var1被赋值成1，否则被赋值成0
# c2 = tk.Checkbutton(window,text = 'C++',variable = var2,
#     onvalue = 1,offvalue = 0,command = print_selection)

# c1.pack()
# c2.pack()

# window.mainloop()


'''
Canvas 画布 规定一片区域，在上面画东西，然后可以调换位置
'''
# import os, getpass, time  #python3使用
# import tkinter as tk
# # from pygame.examples import moveit

# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# canvas = tk.Canvas(window,bg = 'blue',height = 100,width = 200)
# image_file = tk.PhotoImage(file = '22.gif')
# #jpg,png文件还识别不了
# image  = canvas.create_image(0,0,anchor = 'nw',image = image_file)
# #将图片放在(0,0)点，anchor是锚定点的意思，东西南北中等
# x0,y0,x1,y1 = 50,50,80,80
# line = canvas.create_line(x0,y0,x1,y1)#在画布上画这么一条线
# oval = canvas.create_oval(x0,y0,x1,y1,fill = 'red')#圆形
# arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180) #扇形，从零度开始展开，到180度
# # rect = canvas.create_rectangle(100,30,100+20,30+20)
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
# canvas.pack()
# # b =  tk.Button(window,text = 'move',command = moveit).pack()
# def moveit():
#     canvas.move(rect,0,2)
# b = tk.Button(window, text='move', command=moveit).pack()

# window.mainloop()
# from pygame.examples import moveit

# import tkinter as tk

# window = tk.Tk()
# window.title('my window')
# window.geometry('200x200')

# canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# image_file = tk.PhotoImage(file='22.gif')
# image = canvas.create_image(10, 10, anchor='nw', image=image_file)
# x0, y0, x1, y1= 50, 50, 80, 80
# line = canvas.create_line(x0, y0, x1, y1)
# oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
# rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
# canvas.pack()

# def moveit():
#     canvas.move(rect, 0, 2)

# b = tk.Button(window, text='move', command=moveit).pack()


# window.mainloop()

'''
Menubar 菜单，显示在窗口上方的菜单。类似于那种File。Edit那种
'''
# import tkinter as tk

# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# l = tk.Label(window,bg = 'yellow',width = 20,text = '')
# l.pack()

# counter = 0
# def do_job():
#     global counter
#     l.config(text = 'do'+str(counter))
#     counter += 1
# menubar = tk.Menu(window)
# #然后开始定义菜单上的选项
# filemenu = tk.Menu(menubar,tearoff = 1)#tearoff是能不能被分开 改成1呢，改成1之后你会发现菜单栏开始多了一个虚线行
# menubar.add_cascade(label = 'file',menu = filemenu)#增加级联,没有这个的话不会显示file这个菜单选项
# filemenu.add_command(label = 'New',command = do_job)
# #以file命名filemenu
# filemenu.add_command(label = 'Open',command = do_job)
# filemenu.add_command(label = 'Save',command = do_job)
# filemenu.add_separator()#增加分离线
# filemenu.add_command(label = 'Exit',command = window.quit)
# #这个quit是Tkinter自带的

# editmenu = tk.Menu(menubar,tearoff = 1)
# menubar.add_cascade(label = 'Edit',menu = editmenu)
# #以file命名filemenu
# editmenu.add_command(label = 'Cut',command = do_job)
# editmenu.add_command(label = 'Copy',command = do_job)
# editmenu.add_separator()#增加分离线
# editmenu.add_command(label = 'Paste',command = do_job)

# window.config(menu = menubar)#将menubar放窗口上

# #想要在添加一级菜单栏，做法如下
# submenu = tk.Menu(filemenu)#一级菜单这里填的是menubar
# filemenu.add_cascade(label = 'Import',menu = submenu,underline = 1)#underline = 1之后就是在二级菜单多了一条线
# submenu.add_command(label = 'Submenu1',command = do_job)
# window.mainloop()

'''
frame 底层的框架，在上面放各种小部件，就像窗口上的窗口
'''
# import tkinter as tk

# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# tk.Label(window,text = 'on the window').pack()

# frm = tk.Frame(window)#主frame
# frm.pack()
# frm_l = tk.Frame(frm)
# frm_r = tk.Frame(frm)
# frm_l.pack(side = 'left')#放在基于主frame的左边
# frm_r.pack(side = 'right')#放在基于主frame的右边

# tk.Label(frm_l,text = 'on the frm_l1').pack()
# tk.Label(frm_l,text = 'on the frm_l2').pack()
# tk.Label(frm_r,text = 'on the frm_r1').pack()




# window.mainloop()




'''
messagebox 弹窗
'''
# import tkinter as tk
# import tkinter.messagebox
# # from tkinter import
# window = tk.Tk()#建立窗口 对象
# window.title("my window")
# window.geometry('200x200')#中间是x字母 长和宽

# def hit_me():
#     # tk.messagebox.showinfo(title = 'Hi',message = 'haha')
#     # tk.messagebox.showwarning(title = 'Hi',message = 'nononono')
#     # tk.messagebox.showerror(title = 'Hi',message = '11')
#     #warnging没有致命的影响，而error出现就是有致命的影响
#     # print(tk.messagebox.askquestion(title = 'Hi',message = 'haha'))
#     #return 'yes' or 'no'
#     print(tk.messagebox.askyesno(title = 'Hi',message = 'haaaha'))
#     #return 'True' or 'False'
# tk.Button(window,text = 'hit me',command = hit_me).pack()


# window.mainloop()

'''
pack , grid ,place 放置的不同
'''
import tkinter as tk
# import tkinter.messagebox
# from tkinter import
window = tk.Tk()#建立窗口 对象
window.title("my window")
window.geometry('200x200')#中间是x字母 长和宽

# tk.Label(window,text = 1).pack(side = 'top')#四个方位 top,bottom,left,right

#grid用方格的形式来放置
# for i in range(4):
#     for j in range(3):
#         tk.Label(window,text = 1).grid(row = i,column = j,padx = 10,pady = 10)#padx,pady是内部x,y方向上的间隔距离

tk.Label(window,text = 1).place(x = 10,y = 100,anchor = 'nw')
#一个点，放在（10,100) ,设置锚点在西北角上
window.mainloop()