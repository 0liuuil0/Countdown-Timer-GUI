#!/usr/bin/python
# -*- coding: UTF-8 -*-
from calendar import month_abbr
from cgitb import text
import datetime
from re import L
from sqlite3 import Row
import ssl  # 导入datetie库
from tkinter import *           # 导入 Tkinter 库
import tkinter as tk
import tkinter.messagebox  # 导入消息
from tkinter import ttk
from webbrowser import get
from numpy import ones

root = Tk()
root.title('倒计时 by 0liuuil0')  # 窗口标题
root.geometry("400x150")  # 长x宽+x*y
root.attributes('-alpha', 0.85)  # 窗口透明度
root.configure(bg='whitesmoke')  # 创建窗口对象的背景色


restdays = '剩余天数：'
middleexam = '高考：'
today = '今天：'

now = datetime.date.today()  # 实时日期
exam = datetime.date(2025, 6, 7)  # 考试时间
days = exam.__sub__(now).days  # 剩余天数

first = [today, now]
second = [middleexam, exam]
third = [restdays, days]
# 连接变量


def about():
    tkinter.messagebox.showinfo(
        title='关于', message='版本：3.0.0\n© 0liuuil0-202209')
# 版本号


def change():  # 编辑日期窗口
    top = Toplevel()
    top.geometry("400x150")  # 长x宽+x*y
    top.title('编辑')  # 标题
    year = '年'
    month = '月'
    day = '日'
    lab1 = Label(top, text=year)
    lab1.grid(row=0, column=1)
    lab2 = Label(top, text=month)
    lab2.grid(row=1, column=1)
    lab3 = Label(top, text=day)
    lab3.grid(row=2, column=1)

    # 下拉选框（备用）
    comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
    comboxlist = ttk.Combobox(
        top, textvariable=comvalue, width=6, state='normal')

    # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled)  # 初始化
    list1 = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
             '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039', '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050']
    comboxlist["values"] = (list1)
    # comboxlist.current(31)  # 选择第一个

    # def fun(event):
    # print(comboxlist.get())
    def getuser():
        print(comboxlist.get())

    comboxlist2 = ttk.Combobox(
        top, textvariable=comvalue, width=6, state='normal')
    list2 = ['1', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', '11', '12']
    comboxlist2["values"] = (list2)
    # comboxlist2.current(0)  # 选择第一个
    #comboxlist2.grid(row=1, column=1)
    # comboxlist2.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
    comboxlist3 = ttk.Combobox(
        top, textvariable=comvalue, width=6, state='normal')
    list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
             '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    comboxlist3["values"] = (list3)
    comboxlist.grid(row=0)
    comboxlist2.grid(row=1)
    comboxlist3.grid(row=2)

    lab1.pack
    lab2.pack
    lab3.pack
    comboxlist.pack
    comboxlist2.pack
    comboxlist3.pack
    top.mainloop()  # 新建窗口


root.title('日期倒计时 by 0liuuil0')  # 窗口标题
root.geometry("400x150")  # 长x宽+x*y
root.attributes('-alpha', 0.85)  # 窗口透明度
root.configure(bg='whitesmoke')  # 创建窗口对象的背景色


def close_window():
    root.destroy()
# 退出

# li = [third, second, first]
# listb = Listbox(root)  # 创建列表组件


rot = tk.Menu(root)
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(rot, tearoff=False)  # 菜单
#filemenu.add_command(label="编辑", command=change)
filemenu.add_command(label="关于", command=about)
# filemenu.add_command(label="保存")
filemenu.add_separator()  # 分割线
filemenu.add_command(label="退出", command=close_window)
rot.add_cascade(label="选项", menu=filemenu)
rot.add_cascade(label="编辑", command=change)
root.config(menu=rot)

lable = tk.Label(root, text=third, font=("微软雅黑", 23), bg='whitesmoke')
lable.pack()  # 剩余日期
lable1 = tk.Label(root, text=second, font=("微软雅黑", 23), bg='whitesmoke')
lable1.pack()  # 考试日期
lable2 = tk.Label(root, text=first,  font=("微软雅黑", 23), bg='whitesmoke')
lable2.pack()  # 今天

# for item in li:                 # 第一个小部件插入数据
# listb.insert(0, item)
# listb.pack()                    # 将小部件放置到主窗口中

root.mainloop()                 # 进入消息循环
