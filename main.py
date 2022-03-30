from ctypes import alignment
from msilib.schema import ComboBox
from tkinter import *
import sys
import os
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk
import random

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

ws = Tk()
ws.iconphoto(False, PhotoImage(file=resource_path("./img/ico.png")))

ws.title('권작가님 타이머')
ws.geometry('480x630')
ws.configure(bg=_from_rgb((90, 174, 138)),borderwidth = 0)
ws.resizable(0,0)

c = Canvas(ws,width=480,height=670,bg=_from_rgb((90, 174, 138)),bd=0, highlightthickness=0, relief='ridge')
c.pack()

time_y=100
time_text=c.create_text(240,time_y, text="Happy Writing Time!",font=('닉스곤체 M 2.0',22),fill="white")
sec_text=c.create_text(335, time_y+10, text="",font=('닉스곤체 M 2.0',16),fill="white")
msg_shadow=c.create_text(242, 482, text="",font=('닉스곤체 M 2.0',13),fill=_from_rgb((78, 158, 124)))
msg_text=c.create_text(240, 480, text="",font=('닉스곤체 M 2.0',13),fill="white")
rect = c.create_rectangle(10,10, 470, 620, outline='white',width=2)
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
npl = Image.open(resource_path("./img/nplay.png"))
npl=npl.resize((40,40))
nplay = ImageTk.PhotoImage(npl)
img_pl=c.create_image(120, ico_y, image=play)

pa = Image.open(resource_path("./img/pause.png"))
pa=pa.resize((40,40))
pau = ImageTk.PhotoImage(pa)
npa = Image.open(resource_path("./img/npause.png"))
npa=npa.resize((40,40))
npau = ImageTk.PhotoImage(npa)
img_pa=c.create_image(240, ico_y)

sa = Image.open(resource_path("./img/asmr.png"))
sa=sa.resize((40,40))
asmr = ImageTk.PhotoImage(sa)
img_asmr=c.create_image(360, ico_y, image=asmr)


cicx = Image.open(resource_path("./img/circle.png"))
cicx=cicx.resize((300,300))
cirx = ImageTk.PhotoImage(cicx)
img_c=c.create_image(240, cir_y, image=cirx)


mal = Image.open(resource_path("./img/mal.png"))
mal=mal.resize((150,194))
aml = ImageTk.PhotoImage(mal)
img=c.create_image(240, cir_y, image=aml)

imgfl=list()
for i in range(12):    
    bg = Image.open(resource_path(f'./img/frame{i+2}.png'))
    bg=bg.resize((200,200))
    gb = ImageTk.PhotoImage(bg)
    imgfl.append(gb)

m_list=[]
m_list.append("“윌리엄 셰익스피어의 문장에도 여섯 줄에 한 가지 잘못은 있다.”\n\t\t- 스펜서 존슨")
m_list.append("“위대한 글쓰기는 존재하지 않는다.\n오직 위대한 고쳐 쓰기만 존재할 뿐이다.”\n\t\t- E. B. 화이트")
m_list.append("“읽고 싶은 책이 있는데 그 이야기가 책으로 나오지 않았다면 \n\t\t당신이 그 이야기를 쓰면 된다.”\n\t\t-토니 모리슨")
m_list.append("“글쓰기는 세상에서 가장 외로운 노동이다.”\n- 존 스타인 벡")
m_list.append("“사람이 가장 아름다운 순간은,\n 깊이 느끼고, 자유롭게 사랑하고, 거침없이 표현할 때다.”\n\t\t- K. 진호")
m_list.append("“작가란 오늘 아침에 글을 쓴 사람이다.\n\t\t -R. 진 프라이언트")
m_list.append("“글을 쓰고 싶다면 종이와 펜 혹은 컴퓨터\n그리고 약간의 배짱만 있으면 된다.”\n\t\t -R. 진 프라이언트")
m_list.append("“작가는 다른 사람들보다 글쓰기를 어려워 하는 사람이다.” \n\t\t- 토마스 만")
m_list.append("“바빠서 글을 쓸 수 없다는 사람은 평생 글을 쓰지 못한다.”\n\t\t- 찰스 램")
m_list.append("“영감이 찾아오길 기다려선 안된다.\n몽둥이를 들고 그걸 쫓아가야 한다.”\n\t\t - 잭 런던")
m_list.append("“언어만 있고, 사물이 없는 글을 짓지 말 것\n아프지도 않은데 신음하는 글을 짓지 말 것” \n\t\t- 후스")
m_list.append("“지금 쓰고 있는 글을 당신이 즐기지 못하면\n아무도 즐기지 못한다.”\n\t\t - 마르티나 콜")
m_list.append("“만약 작가가 사람을 사랑하지 않는다면 \n어떻게 다른 사람이 그의 작품을 사랑하겠는가.”\n\t\t -앤드루 카네기")
m_list.append("“시간은 작가 중의 작가이다.” \n\t\t- 프란시스 베이컨")
m_list.append("“작가는 인간 영혼의 기사이다.” \n\t\t- J. 스탈린")
m_list.append("“작가의 서고는 그가 날마다 되풀이해서 읽을 원전이라고 할 \n다섯 권 내지 여섯 권의 책으로 이루어져야 할 것이다.” \n\t\t- 플로베르")
m_list.append("“열린 출구는 단 하나밖에 없다. 네 속으로 파고 들어가라.” \n\t\t- 에리히 케스트너")
m_list.append("“미래의 시작은 언제나 즐거운 상상에 있다” \n\t\t- 미야자키 하야오")
m_list.append("“반복은 예술의 죽음이다.” \n\t\t- 로빈 그린")
m_list.append("“모든 예술은 자연의 모방이다.”\n\t\t - 세네카")
m_list.append("“예술의 목적은 사물의 내적인 의미를 보여주는 것이다.” \n\t\t - 아리스토텔레스")
m_list.append("“예술과 사랑을 하기에도 인생은 짧다.” \n\t\t- 윌리엄 서머셋 ")
m_list.append("“사람들이 흥미를 가지는가는 중요하지 않다. \n중요한 건 허공에 대고 당신의 이야기를 소리 치는 것이다.”\n\t\t - 자델르 코르도바")
m_list.append("“글쓰기의 실천은 기본적으로 '망설임들'로 꾸며진다.”\n\t\t- 롤랑 바르트")
m_list.append("“옳다고 해서 반드시 대중적인 것은 아니고\n 대중적이라고 해서 반드시 옳은 것도 아니다.\n 결국 자신이 추구하는 가치를 길잡이로 삼을 수밖에 없다.”\n\t\t- 빌 캐포더글리")
m_list.append("“첫 줄을 쓰는 것은 어마어마한 공포이자 마술이며, \n기도인 동시에 수줍음이다.” \n\t\t- 존 스타인벡")
m_list.append("“서정적인 것이란 자신을 고백하는 주체의 고백이고 \n서사적인 것은 세계의 객관성을 파악하려는 정열로부터 온다.” \n\t\t- 밀란 쿤데라")
m_list.append("“소설가는 자신의 서정세계의 폐허 위에서 태어난다.” \n\t\t- 밀란 쿤데라")
m_list.append("“오직 하나 뿐인 삶에서 완벽함이란 있을 수 없다.” \n\t\t- 밀란 쿤데라")
m_list.append("“자신이 사는 곳을 떠나기를 갈망하는 사람은 불행한 사람이다.” \n\t\t- 밀란 쿤데라")
m_list.append("“인생은 폭풍이 지나가길 기다리는 것이 아니라 \n빗속에서 춤추는 것을 배우는 것이다.” \n\t\t- 밀란 쿤데라")
m_list.append("“부담이 클수록 우리의 삶이 지구에 가까워지고\n 더더욱 현실적이고 진실해 진다.” \n\t\t- 밀란 쿤데라")
m_list.append("“두려움의 근원은 미래에 있고\n미래에서 해방된 사람은 두려워할 것이 없다.” \n\t\t- 밀란 쿤데라")
m_list.append("“당신 스스로가 하지 않는다면 \n누구도 당신의 운명을 개선시키려 들지 않는다.” \n\t\t- B. 브레히트")
counter = 0
im_cnt=0

running = False
def counter_label():
    def count():
        if running:
            global im_cnt
            global counter

            h=format(int(counter)//(60*60), '02')
            m=format((int(counter)%3600)//(60), '02')
            s=format(int(counter)%60, '02')
            display=h+":"+m
            c.itemconfigure(time_text, text=display,font=('닉스곤체 M 2.0',44),fill="white")
            c.itemconfigure(sec_text, text=s)
            if (im_cnt%3000)==0:
                random.shuffle(m_list)
                tmp=m_list.pop()
                c.itemconfigure(msg_text, text=tmp)
                c.itemconfigure(msg_shadow, text=tmp)
                        
            c.itemconfigure(img,image=imgfl[im_cnt%12])
            if(counter%60==0 and counter!=0):
                counter+=1
            c.after(200, count)    
            im_cnt+=1
            if(im_cnt%5==0):
                counter += 1
            

    count() 
    

def StartTimer(event):
    global running
    running=True
    url.place_forget()
    url.set("ASMR")
    counter_label()
    c.itemconfigure(img_pl,image=nplay)
    c.itemconfigure(img_pa,image=pau)

def StopTimer(event):
    global running
    running = False
    c.itemconfigure(img_pl,image=play)
    c.itemconfigure(img_pa,image=npau)

def openASMR(link):
    url.place_forget()
    random.shuffle(m_list)
    tmp=m_list.pop()
    c.itemconfigure(msg_text, text=tmp)
    c.itemconfigure(msg_shadow, text=tmp)
    webbrowser.open(link)
    c.itemconfigure(img_pa,image=npau)
    url.set("ASMR")

def musicbrowse(event):
    StopTimer(event)
    c.itemconfigure(img_pa,image="")
    a = url.get()
    url.place(x=200,y=ico_y-15)

    if(a=='모닥불'):
        openASMR("https://www.youtube.com/watch?v=UgHKb_7884o&ab_channel=CatTrumpet")
    elif (a=='도서관'):
        openASMR("https://www.youtube.com/watch?v=4vIQON2fDWM&ab_channel=TheGuildofAmbience")
    elif(a=='빗소리'):
        openASMR("https://www.youtube.com/watch?v=-N9rb2QDqrw&ab_channel=dreamysound")
    elif(a=='클래식'):
        openASMR("https://www.youtube.com/watch?v=38LMlhYiQzc&ab_channel=HALIDONMUSIC")
    elif(a=='카페'):
        openASMR("https://www.youtube.com/watch?v=R2sYaJyFETM&ab_channel=%EB%AA%BD%ED%82%A4%EB%B9%84%EC%A7%80%EC%97%A0MONKEYBGM")
    
    

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground':_from_rgb((72, 113, 95)),
                                       'fieldbackground': _from_rgb((72, 113, 95)),
                                       'fieldforeground': _from_rgb((90, 174, 138)),
                                       'foreground': _from_rgb((255, 255, 255)),
                                       'background': _from_rgb((90, 174, 138)),
                                       'arrowcolor':"white",
                                       "bordercolor":_from_rgb((90, 174, 138)),
                                       "darkcolor":"lightgreen",
                                       "insertcolor":"lightgreen",
                                       "insertwidth":20
                                       }}}
                         )

ws.option_add("*TCombobox*Listbox*Background", _from_rgb((90, 174, 138)))
ws.option_add("*TCombobox*Listbox*font",('"닉스곤체 M 2.0"'))
ws.option_add("*TCombobox*Listbox*foreground", "white")
ws.option_add("*TCombobox*Listbox*selectBackground", _from_rgb((72, 113, 95)))

# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle') 

url = ttk.Combobox(ws,values=["모닥불","도서관","빗소리","클래식","카페"],state='readonly',font=('닉스곤체 M 2.0',15),width=6)
url.set("ASMR")

url.place(x=200,y=ico_y-15)

c.tag_bind(img_pl,"<Button-1>",StartTimer)
c.tag_bind(img_pa,"<Button-1>",StopTimer)
c.tag_bind(img_asmr,"<Button-1>",musicbrowse)

ws.mainloop()