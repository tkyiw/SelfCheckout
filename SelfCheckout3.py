#1 tkinterモジュールをtkという名前でインポート
import tkinter as tk
import tkinter.ttk as ttk
import time
from PIL import Image, ImageTk

import picamera
import pygame.mixer
import time


pygame.mixer.init()
#pygame.mixer.music.load('/usr/share/sounds/alsa/Rear_Center.wav')
#pygame.mixer.music.set_volume(1.0)
#pygame.mixer.music.play()
#time.sleep(5)

import models


import cv2
import numpy as np
import matplotlib.pyplot as plt

global dic_registered_current_count
global dic_unregistered_current_count
global dic_registered_past_count
global lst_item_past
global lst_item_current

dic_registered_name={'black_uron':'黒烏龍茶 350ml',
                     'tyouseimeitai':'超生命体飲料ライフガード 500ml',
                     'match':'ビタミン炭酸MATCH 500ml',
                     'orangina100':'ORANGINA100 300ml',
                     'cola':'コカ・コーラ ゼロ 500ml'}

dic_registered_price={'black_uron':200,
                     'tyouseimeitai':130,
                     'match':140,
                     'orangina100':120,
                     'cola':150}

dic_registered_current_count={'black_uron':0,
                     'tyouseimeitai':0,
                     'match':0,
                     'orangina100':0,
                     'cola':0}

dic_unregistered_current_count={'unknown':0}

dic_registered_past_count={'black_uron':0,
                     'tyouseimeitai':0,
                     'match':0,
                     'orangina100':0,
                     'cola':0}




lst_item_past=[]
lst_item_current=[]



def fixed_map(option):
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]







#2 ウインドウの生成と変数への格納
root_window = tk.Tk()
root_window.title(u"セルフレジ")
root_window.geometry("1500x900")

# ツリービューの作成
style = ttk.Style(root_window)
style.configure('Treeview',rowheight=37,font=(None,18))
style.configure('Treeview.Heading',font=(None,18))
tree = ttk.Treeview(root_window)

style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))




# 列インデックスの作成
tree["columns"] = (1,2,3,4)
# 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
tree["show"] = "headings"
# 各列の設定(インデックス,オプション(今回は幅を指定))
tree.column(1,width=600)
tree.column(2,width=70)
tree.column(3,width=70)
tree.column(4,width=70)

# 各列のヘッダー設定(インデックス,テキスト)
tree.heading(1,text="商品名")
tree.heading(2,text="単価")
tree.heading(3,text="個数")
tree.heading(4,text="小計")



tree.tag_configure('yellow',foreground='black',background='yellow')
tree.tag_configure('white',foreground='black',background='white')
tree["height"] = 13


img_1=Image.open('OK.jpg')
img_1=ImageTk.PhotoImage(img_1)

canvas_1=tk.Canvas(bg='white',width=1020,height=520)
canvas_1.create_image(10,10,image=img_1,anchor=tk.NW)

img_2=Image.open('img/result.jpg')
img_2=ImageTk.PhotoImage(img_2)

canvas_2=tk.Canvas(bg='white',width=512,height=512)
image_on_canvas=canvas_2.create_image(0,0,image=img_2,anchor=tk.NW)

img_3=Image.open('hello.jpg')
img_3=ImageTk.PhotoImage(img_3)

canvas_3=tk.Canvas(bg='white',width=400,height=300)
canvas_3.create_image(0,0,image=img_3,anchor=tk.NW)

img_4=Image.open('bye.jpg')
img_4=ImageTk.PhotoImage(img_4)

canvas_4=tk.Canvas(bg='white',width=400,height=300)
canvas_4.create_image(0,0,image=img_4,anchor=tk.NW)



#3 可変文字列の生成と変数への格納
lbl_1_text = tk.StringVar()
lbl_2_text = tk.StringVar()
lbl_3_text = tk.StringVar()
lbl_4_text = tk.StringVar()
lbl_5_text = tk.StringVar()
lbl_6_text = tk.StringVar()
lbl_7_text = tk.StringVar()
lbl_8_text = tk.StringVar()
lbl_9_text = tk.StringVar()

#4 可変文字列の初期化
lbl_1_text.set("ペットボトルを横向きに配置してから「商品スキャン」ボタンを押下してください。")
lbl_2_text.set("商品をスキャンしました。")
lbl_3_text.set("続けて他の商品を読み取る場合は、他の商品を置いてから再度「商品スキャン」ボタンを押下してください。")
lbl_4_text.set("会計へ進む場合は「お支払いへ」ボタンを押下してください。")
lbl_5_text.set("以下の合計金額をセルフレジにてお支払いください。")
lbl_6_text.set("お支払金額")
lbl_7_text.set("商品数：     　　12点")
lbl_8_text.set("合計金額：　2,800円")
lbl_9_text.set("商品内訳")


#5 ボタンが押された時用の関数を予め定義しておく。
def btn_start_clicked():
    
    global dic_registered_current_count
    global dic_unregistered_current_count
    global dic_registered_past_count
    global lst_item_past
    global lst_item_current
    
    lbl_1.place(x=55,y=30)
    
    btn_call.place(x=140,y=750)
    btn_scan.place(x=590,y=750)
    btn_cancel.place(x=1040,y=750)
    btn_start.place_forget()
    canvas_3.place_forget()
    
    canvas_1.place(x=250,y=160)
    
    pygame.mixer.music.load('いらっしゃいませ.wav')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(2)
    
    lst_item_current=[]
    lst_item_past=[]
    
    dic_registered_current_count={'black_uron':0,
                         'tyouseimeitai':0,
                         'match':0,
                         'orangina100':0,
                         'cola':0}

    dic_unregistered_current_count={'unknown':0}

    dic_registered_past_count={'black_uron':0,
                         'tyouseimeitai':0,
                         'match':0,
                         'orangina100':0,
                         'cola':0}    
    
    
    

def btn_cancel_clicked():
    btn_start.place(x=280,y=280)
    canvas_3.place(x=560,y=90)
    lbl_1.place_forget()
    canvas_1.place_forget()
    btn_scan.place_forget()
    btn_cancel.place_forget()
    btn_call.place_forget()

def btn_scan_clicked():
    
    with picamera.PiCamera() as camera:
        camera.resolution=(512,512)
        camera.start_preview()
        time.sleep(0.1)
        camera.capture('img/image.jpg')
    
    lst_item=models.predict('img/image.jpg')
    print(lst_item)

    
    lst_item_current=[]
    if len(lst_item)>0:
        for item in lst_item:
            if not item in lst_item_current:
                if item in dic_registered_name:
                    lst_item_current.append(item)
                    dic_registered_current_count[item]=1
                else:                
                    lst_item_current.append('unknown')
                    dic_unregistered_current_count['unknown']=1
            else:
                if item in dic_registered_name:
                    dic_registered_current_count[item]=dic_registered_current_count[item]+1
                else:                
                    dic_unregistered_current_count['unknown']=dic_unregistered_current_count['unknown']+1              


    #ツリービューのリストを初期化
    tree.delete(*tree.get_children())
         
    for past in lst_item_past:
        tree.insert("","end",values=(dic_registered_name[past],dic_registered_price[past],dic_registered_past_count[past],dic_registered_price[past]*dic_registered_past_count[past]),tags=['white'])


    for current in lst_item_current:
        if current=='unknown':
            tree.insert("","end",values=('未登録商品','-',dic_unregistered_current_count[current],'-'),tags=['yellow'])
        else:
            tree.insert("","end",values=(dic_registered_name[current],dic_registered_price[current],dic_registered_current_count[current],dic_registered_price[current]*dic_registered_current_count[current]),tags=['yellow'])
    
    
    if len(lst_item_current)>0:
        for current in lst_item_current:
            if not current in lst_item_past:
                if current in dic_registered_name:
                    lst_item_past.append(current)
                    #dic_registered_past_count[current]=1
                    dic_registered_past_count[current]=dic_registered_current_count[current]
            else:
                if current in dic_registered_name:
                    #dic_registered_past_count[current]=dic_registered_past_count[current]+1
                    dic_registered_past_count[current]=dic_registered_past_count[current]+dic_registered_current_count[current]
    lst_item_current=[]


    global img_2
    img_2=Image.open('img/result.jpg')
    img_2=ImageTk.PhotoImage(img_2)
    canvas_2.itemconfig(image_on_canvas,image=img_2)
    
    lbl_1.place_forget()
    canvas_1.place_forget()
    
    btn_cancel.place_forget()
    lbl_2.place(x=55,y=30)
    lbl_3.place(x=55,y=640)
    lbl_4.place(x=55,y=690)
    btn_check.place(x=1040,y=750)
    
    canvas_2.place(x=55,y=100)
    tree.place(x=620,y=100)
    
    pygame.mixer.music.load('Beep_1.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(0.25)
    
    
def btn_check_clicked():
    
    price=0
    count=0
    
    
    #ツリービューのリストを初期化
    tree.delete(*tree.get_children())    
    
    for past in lst_item_past:
        tree.insert("","end",values=(dic_registered_name[past],dic_registered_price[past],dic_registered_past_count[past],dic_registered_price[past]*dic_registered_past_count[past]),tags=['white'])
        price=price+dic_registered_price[past]*dic_registered_past_count[past]
        count=count+dic_registered_past_count[past]
    
    lbl_7_text.set("商品数：     　　"+str(count)+"点")
    lbl_8_text.set("合計金額：　"+str(price)+"円")
    
    
    
    
    lbl_2.place_forget()
    lbl_3.place_forget()
    lbl_4.place_forget()
    canvas_2.place_forget()
    #tree.place_forget()
    tree.place(x=620,y=160)
    btn_scan.place_forget()
    btn_check.place_forget()
    lbl_5.place(x=55,y=30)
    lbl_6.place(x=55,y=110)
    lbl_7.place(x=55,y=180)
    lbl_8.place(x=55,y=280)
    lbl_9.place(x=620,y=110)
    btn_ok.place(x=580,y=750)
    canvas_4.place(x=100,y=375)

def btn_ok_clicked():
    lbl_5.place_forget()
    lbl_6.place_forget()
    lbl_7.place_forget()
    lbl_8.place_forget()
    lbl_9.place_forget()
    btn_ok.place_forget()
    btn_call.place_forget()
    tree.place_forget()
    canvas_4.place_forget()
    canvas_3.place(x=560,y=90)
    btn_start.place(x=280,y=280)
    pygame.mixer.music.load('Register_1.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.load('ご利用ありがとうございました.wav')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(5)
    
    st_item_past=[]
    lst_item_current=[]
    
def btn_call_clicked():
    pygame.mixer.music.load('店員呼び出し.wav')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    time.sleep(4)
    
#6 GUIパーツの生成と変数への格納
lbl_1 = tk.Label(
    master=root_window,
    textvariable=lbl_1_text,
    font=("",28)
    )

lbl_2 = tk.Label(
    master=root_window,
    textvariable=lbl_2_text,
    font=("",28)
    )

lbl_3 = tk.Label(
    master=root_window,
    textvariable=lbl_3_text,
    font=("",20)
    )

lbl_4 = tk.Label(
    master=root_window,
    textvariable=lbl_4_text,
    font=("",20)
    )

lbl_5 = tk.Label(
    master=root_window,
    textvariable=lbl_5_text,
    font=("",28)
    )

lbl_6 = tk.Label(
    master=root_window,
    textvariable=lbl_6_text,
    font=("",24)
    )

lbl_7 = tk.Label(
    master=root_window,
    textvariable=lbl_7_text,
    font=("",38)
    )

lbl_8 = tk.Label(
    master=root_window,
    textvariable=lbl_8_text,
    font=("",38)
    )

lbl_9 = tk.Label(
    master=root_window,
    textvariable=lbl_9_text,
    font=("",24)
    )

btn_call = tk.Button(
    master=root_window,
    text="店員呼び出し",
    command=btn_call_clicked,
    width=12,
    height=2,
    font=("",30)
    )

btn_start = tk.Button(
    master=root_window,
    text="お会計を始める",
    command=btn_start_clicked,
    width=12,
    height=2,
    font=("",90)
    )

btn_scan = tk.Button(
    master=root_window,
    text="商品スキャン",
    command=btn_scan_clicked,
    width=12,
    height=2,
    font=("",30)
    )

btn_cancel = tk.Button(
    master=root_window,
    text="キャンセル",
    command=btn_cancel_clicked,
    width=12,
    height=2,
    font=("",30)
    )

btn_check = tk.Button(
    master=root_window,
    text="お支払いへ",
    command=btn_check_clicked,
    width=12,
    height=2,
    font=("",30)
    )

btn_ok = tk.Button(
    master=root_window,
    text="OK",
    command=btn_ok_clicked,
    width=12,
    height=2,
    font=("",30)
    )

#7 GUIパーツの配置
btn_start.place(x=280,y=280)
canvas_3.place(x=560,y=90)

models=models.Model_takami()
#8 ウインドウ表示
root_window.mainloop()
