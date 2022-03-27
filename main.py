from ctypes import alignment
from msilib.schema import ComboBox
from tkinter import *
import sys
import os
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

ws = Tk()

wd = PhotoImage(file = resource_path("./img/wood.png"))

ws.title('권작가님 타이머')
ws.geometry('480x630')
ws.configure(bg=_from_rgb((90, 174, 138)))
ws.resizable(0,0)

c = Canvas(ws,width=480,height=670,bg=_from_rgb((90, 174, 138)))
c.pack()
#fill="#FFFAF0"
# c.create_image(0, 200, image=wd)
time_y=100
time_text=c.create_text(240,time_y, text="Happy Writing Time!",font=('닉스곤체 M 2.0',22),fill="white")
sec_text=c.create_text(335, time_y+10, text="",font=('닉스곤체 M 2.0',16),fill="white")
msg_text=c.create_text(240, 480, text="",font=('닉스곤체 M 2.0',13),fill="white")
# hap_text=c.create_text(240, 80, text="Happy Writing Time!",font=('닉스곤체 M 2.0',20,'bold'),fill=_from_rgb((110, 68, 10)))

cir_y=280
cicy = Image.open(resource_path("./img/circle_y.png"))
cicy=cicy.resize((250,250))
ciry = ImageTk.PhotoImage(cicy)
img_y=c.create_image(240, cir_y, image=ciry)

cic = Image.open(resource_path("./img/circle_b.png"))
cic=cic.resize((250,250))
cir = ImageTk.PhotoImage(cic)
img_c=c.create_image(240, cir_y, image=cir)

ico_y=560
pl = Image.open(resource_path("./img/play.png"))
pl=pl.resize((40,40))
play = ImageTk.PhotoImage(pl)
img_pl=c.create_image(120, ico_y, image=play)

pa = Image.open(resource_path("./img/pause.png"))
pa=pa.resize((40,40))
pau = ImageTk.PhotoImage(pa)
img_pa=c.create_image(240, ico_y, image=pau)

sa = Image.open(resource_path("./img/asmr.png"))
sa=sa.resize((40,40))
asmr = ImageTk.PhotoImage(sa)
img_asmr=c.create_image(360, ico_y, image=asmr)


cicx = Image.open(resource_path("./img/circle.png"))
cicx=cicx.resize((300,300))
cirx = ImageTk.PhotoImage(cicx)
img_c=c.create_image(240, cir_y, image=cirx)


mal = Image.open(resource_path("./img/mal.png"))
mal=mal.resize((200,200))
aml = ImageTk.PhotoImage(mal)
img=c.create_image(240, cir_y, image=aml)

imgfl=list()
for i in range(12):    
    bg = Image.open(resource_path(f'./img/frame{i+2}.png'))
    bg=bg.resize((200,200))
    gb = ImageTk.PhotoImage(bg)
    imgfl.append(gb)

counter = 0
running = False

def counter_label():
    def count():
        if running:
            global counter
            h=format(counter//(10*60*60), '02')
            m=format((counter%36000)//(10*60), '02')
            s=format((counter//10)%60, '02')
            display=h+":"+m
            c.itemconfigure(time_text, text=display,font=('닉스곤체 M 2.0',44),fill="white")
            c.itemconfigure(sec_text, text=s)
            if 12000>=counter:
                url.destroy()
                c.itemconfigure(msg_text, text="“윌리엄 셰익스피어의 문장에도 여섯 줄에 한 가지 잘못은 있다.”\n\t\t- 스펜서 존슨")
            elif 18000>=counter:
                c.itemconfigure(msg_text, text="“위대한 글쓰기는 존재하지 않는다.\n오직 위대한 고쳐 쓰기만 존재할 뿐이다.”\n\t\t- E. B. 화이트")
            elif 24000>=counter:
                c.itemconfigure(msg_text, text="“읽고 싶은 책이 있는데 그 이야기가 책으로 나오지 않았다면 \n\t당신이 그 이야기를 쓰면 된다.”\n\t\t-토니 모리슨")
            elif 36000>=counter:
                c.itemconfigure(msg_text, text="“글쓰기는 세상에서 가장 외로운 노동이다.”\n- 존 스타인 벡")
            else :
                c.itemconfigure(msg_text, text="“사람이 가장 아름다운 순간은,\n 깊이 느끼고, 자유롭게 사랑하고, 거침없이 표현할 때다.”\n- K. 진호")
                        
            c.itemconfigure(img,image=imgfl[counter%12])
            
            c.after(100, count)    
            counter += 1
            

    count() 
    

def StartTimer(event):
    global running
    running=True
    counter_label()
    start_btn['state']='disabled'
    stop_btn['state']='normal'
    # reset_btn['state']='normal'

def StopTimer(event):
    global running
    start_btn['state']='normal'
    stop_btn['state']='disabled'
    # reset_btn['state']='normal'
    running = False

# def ResetTimer(lbl):
#     global counter
#     counter=-1
#     if running==False:      
#         reset_btn['state']='disabled'
#         lbl['text']='00'
#     else:                          
#         lbl['text']=''
def musicbrowse(event):
    a = url.get()
    if(a=='모닥불'):
        webbrowser.open("https://www.youtube.com/watch?v=UgHKb_7884o&ab_channel=CatTrumpet")
    elif (a=='도서관'):
        webbrowser.open("https://www.youtube.com/watch?v=4vIQON2fDWM&ab_channel=TheGuildofAmbience")
    elif(a=='빗소리'):
        webbrowser.open("https://www.youtube.com/watch?v=-N9rb2QDqrw&ab_channel=dreamysound")
    elif(a=='클래식'):
        webbrowser.open("https://www.youtube.com/watch?v=38LMlhYiQzc&ab_channel=HALIDONMUSIC")
    elif(a=='카페'):
        webbrowser.open("https://www.youtube.com/watch?v=R2sYaJyFETM&ab_channel=%EB%AA%BD%ED%82%A4%EB%B9%84%EC%A7%80%EC%97%A0MONKEYBGM")
    url.destroy()
    c.itemconfigure(msg_text, text="“첫 줄을 쓰는 것은 어마어마한 공포이자 마술이며, \n기도인 동시에 수줍음이다.” \n- 존 스타인벡",font=('NanumSquare',12))

start_btn=Button(
    ws, 
    text='시작', 
    width=15, 
    font=('NanumSquare', 10),
    command=lambda:StartTimer()
    )

stop_btn = Button(
    ws, 
    text='Stop', 
    width=15, 
    state='disabled', 
    # font=(font, 10),
    command=StopTimer
    )
brow_btn = Button(
    ws, 
    text='ASMR', 
    width=15, 
    # font=(font, 10),
    command=musicbrowse
)
combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground':_from_rgb((72, 113, 95)),
                                       'fieldbackground': _from_rgb((72, 113, 95)),
                                       'fieldforeground': _from_rgb((90, 174, 138)),
                                       'foreground': _from_rgb((255, 255, 255)),
                                       'background': _from_rgb((90, 174, 138)),
                                       }}}
                         )
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle') 

url = ttk.Combobox(ws,values=["모닥불","도서관","빗소리","클래식","카페"],state='readonly',font=('닉스곤체 M 2.0',15),width=6)
url.set("ASMR")
# url.current(0)

url.place(x=200,y=460)

# reset_btn = Button(
#     ws, 
#     text='Reset', 
#     width=15, 
#     state='disabled', 
#     command=lambda:ResetTimer(lbl)
#     )

c.tag_bind(img_pl,"<Button-1>",StartTimer)
c.tag_bind(img_pa,"<Button-1>",StopTimer)
c.tag_bind(img_asmr,"<Button-1>",musicbrowse)

# start_btn.place(x=50, y=630)
# stop_btn.place(x=320, y=630)
# brow_btn.place(x=185, y=630)
# reset_btn.place(x=270, y=390)

ws.mainloop()