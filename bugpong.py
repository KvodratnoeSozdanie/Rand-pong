import random
import time
import threading
from tkinter import *
import winsound

q = Tk()
q.title('Rand-Pong')
q.geometry('1400x700+300+150')
q.resizable(width=False, height=False)

speeds = [i for i in range(-6, -2)] + [n for n in range(3, 7)]
speedpl = [-75, 75, -75, 75]  # [0] - скорость синей платформы вверх | [1] - ск синей платформы вниз | [2] и [3] -
# тоже самое но для красной
speedbl = [random.choice(speeds) for i in range(4)]
upr = [False, 0, 0, 0, 10, 10, False, False, 10, False, True, False, False, False,
       False, False]  # [0] - кулдаун отскока х | [1] - счёт красного | [2] - счёт синего | [3] - рандомная инверсия,
# 16 эл

if ((speedbl[2] < 0) and (speedbl[0] < 0)) or ((speedbl[2] > 0) and (speedbl[0] > 0)):
    speedbl[2] = -speedbl[2]
if ((speedbl[3] < 0) and (speedbl[1] < 0)) or ((speedbl[3] > 0) and (speedbl[1] > 0)):
    speedbl[3] = -speedbl[3]

d = Canvas(width=1500, height=800, background='#3cb371')
d.place(x=-10, y=0)

d.create_line((700 + 10, 0), (700 + 10, 1000), fill='#308f5a', width=5)
d.create_oval((-300, 50), (300, 650), outline='#308f5a', width=5)
d.create_oval((1400 + 20 - 300, 50), (1400 + 20 + 300, 650), outline='#308f5a', width=5)
d.create_oval((700 - 100 + 10, 350 - 100), (700 + 100 + 10, 350 + 100), outline='#308f5a', width=5)
lb = Label(text=f"{upr[2]}/10", font='Arial 50', background='#3cb371')
lr = Label(text=f"{upr[1]}/10", font='Arial 50', background='#3cb371')
ir = Label(text='управление инвертировано на {} сек'.format(upr[4]), font='Arial 14', background='#3cb371')
br = Label(text='управление инвертировано на {} сек'.format(upr[8]), font='Arial 14', background='#3cb371')
gol = Label(text='гол!', font='Arial 50', background='#3cb371')
lb.place(x=700 / 2, y=3)
lr.place(x=1400 - 700 / 2, y=3)
pb = d.create_rectangle((-20, 350 - 125), (30, 350 + 125), fill='blue', outline='black', width=5)
pr = d.create_rectangle((1400 - 30 + 20, 350 - 125), (1400 + 20 + 20, 350 + 125), fill='red', outline='black', width=5)
ball1 = d.create_rectangle((700 - 25 + 10, 350 - 25), (700 + 25 + 10, 350 + 25), fill='white', outline='black', width=5)
ball2 = d.create_rectangle((-100, -100), (-50, -50), fill='black', outline='white', width=5)


# win.place(x=475, y=300)


def move(event):
    global speedpl
    if event.keycode == 87:
        d.move(pb, 0, speedpl[0])
    elif event.keycode == 83:
        d.move(pb, 0, speedpl[1])
    elif event.keysym == 'Up':
        d.move(pr, 0, speedpl[2])
    elif event.keysym == 'Down':
        d.move(pr, 0, speedpl[3])


d.bind_all('<KeyPress>', move)


def dance():
    global speedpl, speedbl
    corb1 = d.coords(ball1)
    corpb = d.coords(pb)
    corpr = d.coords(pr)
    if corb1[1] <= 0 or corb1[3] >= 700:
        speedbl[1] = -speedbl[1]
    if (corb1[0] <= 30 and (corb1[3] >= corpb[1] and corb1[1] <= corpb[3])) and not upr[0]:
        if random.randint(0, 25) == 1:
            invent_r()
        threading.Thread(target=timer_x, daemon=True).start()
    if ((corb1[0] >= 1400 - 60) and (corb1[1] <= corpr[3] and corb1[3] >= corpr[1])) and not upr[0]:
        if random.randint(0, 25) == 1:
            invent_b()
        threading.Thread(target=timer_x, daemon=True).start()
    if corb1[0] <= 0 and not (corb1[3] >= corpb[1] and corb1[1] <= corpb[3]):
        gol_red()
    elif corb1[2] >= 1410 and not (corpr[1] <= corb1[1] <= corpr[3]):
        gol_blue()
    if not upr[6]:
        threading.Thread(target=timer_speed, daemon=True).start()
    if not upr[7]:
        d.move(ball1, speedbl[0], speedbl[1])
    if random.randint(0, 1000) == 1 and not upr[11]:
        upr[11] = True
    if upr[11]:
        if not upr[12]:
            d.coords(ball2, 700 - 25 + 10, 350 - 25, 700 + 25 + 10, 350 + 25)
        hell(corpb, corb1, corpr)
    d.after(20, dance)


def hell(corpb, corb1, corpr):
    global upr
    if not upr[14]:
        threading.Thread(target=timer_ball2, daemon=True).start()
        threading.Thread(target=ball_start(), daemon=True).start()
    corb2 = d.coords(ball2)
    if corb2[1] <= 0 or corb2[3] >= 700:
        speedbl[3] = -speedbl[3]
    if (corb2[0] <= 30 and (corb2[3] >= corpb[1] and corb2[1] <= corpb[3])) and not upr[13]:
        if random.randint(0, 25) == 1:
            invent_r()
        threading.Thread(target=timer_x2, daemon=True).start()
    if ((corb2[0] >= 1400 - 60) and (corb2[1] <= corpr[3] and corb2[3] >= corpr[1])) and not upr[13]:
        if random.randint(0, 25) == 1:
            invent_b()
        threading.Thread(target=timer_x2, daemon=True).start()
    if corb2[0] <= 0 and not (corb2[3] >= corpb[1] and corb2[1] <= corpb[3]):
        gol_red()
    elif corb2[2] >= 1410 and not (corpr[1] <= corb2[1] <= corpr[3]):
        gol_blue()
    if not upr[6]:
        threading.Thread(target=timer_speed, daemon=True).start()
    if not upr[7]:
        d.move(ball2, speedbl[2], speedbl[3])
    if (corb2[1] >= corb1[1] >= corb2[3]) and (corb2[0] <= corb1[2] <= corb2[2]):
        speedbl[1], speedbl[3] = speedbl[3], speedbl[1]
    if (corb2[3] <= corb1[3] <= corb2[1]) and (corb2[0] <= corb1[2] <= corb2[2]):
        speedbl[1], speedbl[3] = speedbl[3], speedbl[1]
    if (corb2[2] <= corb1[2] <= corb2[0]) and (corb1[1] <= corb2[1] <= corb1[3]):
        speedbl[0], speedbl[2] = speedbl[2], speedbl[0]
    if (corb2[0] <= corb1[0] <= corb2[2]) and (corb1[1] <= corb2[1] <= corb1[3]):
        speedbl[0], speedbl[2] = speedbl[2], speedbl[0]


def invent_r():
    global speedpl
    if not upr[9]:
        threading.Thread(target=timer, daemon=True).start()


def invent_b():
    global speedpl
    if not upr[10]:
        threading.Thread(target=timer_b, daemon=True).start()


def timer():
    global speedpl, upr
    upr[9] = True
    speedpl[2] = 50
    speedpl[3] = -50
    upr[4] = 10
    ir.configure(text='управление инвертировано на {} сек'.format(upr[4]), font='Arial 14', background='#3cb371')
    ir.place(x=700 / 2 + 700 - 100, y=650)
    for _ in range(11):
        time.sleep(1)
        upr[4] -= 1
        ir.configure(text='управление инвертировано на {} сек'.format(upr[4]), font='Arial 14', background='#3cb371')
    speedpl[2] = -50
    speedpl[3] = 50
    ir.place(x=-100, y=-100)
    upr[9] = False


def timer_b():
    upr[10] = True
    global speedpl
    speedpl[0] = 50
    speedpl[1] = -50
    upr[8] = 10
    br.configure(text='управление инвертировано на {} сек'.format(upr[8]), font='Arial 14', background='#3cb371')
    br.place(x=700 / 2 - 200, y=650)
    for _ in range(11):
        time.sleep(1)
        upr[8] -= 1
        br.configure(text='управление инвертировано на {} сек'.format(upr[8]), font='Arial 14', background='#3cb371')
    speedpl[0] = -50
    speedpl[1] = 50
    br.place(x=-100, y=-100)
    upr[10] = False


def timer_speed():
    upr[6] = True
    time.sleep(7)
    if speedbl[0] > 0:
        speedbl[0] += 2
    else:
        speedbl[0] -= 2
    if speedbl[1] > 0:
        speedbl[1] += 2
    else:
        speedbl[1] -= 2
    if upr[11]:
        if speedbl[2] > 0:
            speedbl[2] += 2
        else:
            speedbl[2] -= 2
        if speedbl[3] > 0:
            speedbl[3] += 2
        else:
            speedbl[3] -= 2
    upr[6] = False


def timer_x():
    global upr
    upr[0] = True
    speedbl[0] = -speedbl[0]
    time.sleep(1)
    upr[0] = False


def timer_x2():
    global upr
    upr[13] = True
    speedbl[2] = -speedbl[2]
    time.sleep(1)
    upr[13] = False


def timer_ball2():
    upr[12] = True
    upr[14] = True
    time.sleep(50)
    upr[12] = False
    upr[11] = False
    upr[14] = False
    d.coords(ball2, -100, -100, -100, -100)


def timer_balls():
    upr[15] = True
    time.sleep(3)
    upr[15] = False


def gol_blue():
    global upr, speedbl
    upr[2] += 1
    if upr[2] == 10:
        end_game()
        time.sleep(5)
    lb.configure(text=f"{upr[2]}/10")
    # threading.Thread(target=gol_zv(), daemon=True).start()
    d.coords(ball1, (685, 325, 700 + 25 + 10, 350 + 25))
    if upr[11]:
        d.coords(ball2, (685, 325 - 200, 700 + 25 + 10, 350 + 25 - 200))
    upr[6] = True
    upr[7] = True
    gol.place(x=650, y=300)
    while threading.Thread(target=timer_speed).is_alive():
        threading.Thread(target=time.sleep(1), daemon=True).start()
    speedbl = [random.choice(speeds) for _ in range(4)]
    if ((speedbl[2] < 0) and (speedbl[0] < 0)) or ((speedbl[2] > 0) and (speedbl[0] > 0)):
        speedbl[2] = -speedbl[2]
    if ((speedbl[3] < 0) and (speedbl[1] < 0)) or ((speedbl[3] > 0) and (speedbl[1] > 0)):
        speedbl[3] = -speedbl[3]
    threading.Thread(target=timer_after_gol, daemon=True).start()


def timer_after_gol():
    time.sleep(3)
    gol.place(x=-100, y=-100)
    upr[7] = False
    upr[6] = False


def gol_red():
    global upr, speedbl
    upr[1] += 1
    if upr[1] == 10:
        end_game()
    lr.configure(text=f"{upr[1]}/10")
    # threading.Thread(target=gol_zv(), daemon=True).start()
    d.coords(ball1, (685, 325, 700 + 25 + 10, 350 + 25))
    if upr[11]:
        d.coords(ball2, (685, 325 - 200, 700 + 25 + 10, 350 + 25 - 200))
    upr[6] = True
    upr[7] = True
    gol.place(x=650, y=300)
    while threading.Thread(target=timer_speed).is_alive():
        threading.Thread(target=time.sleep(1), daemon=True).start()
    speedbl = [random.choice(speeds) for _ in range(4)]
    if ((speedbl[2] < 0) and (speedbl[0] < 0)) or ((speedbl[2] > 0) and (speedbl[0] > 0)):
        speedbl[2] = -speedbl[2]
    if ((speedbl[3] < 0) and (speedbl[1] < 0)) or ((speedbl[3] > 0) and (speedbl[1] > 0)):
        speedbl[3] = -speedbl[3]
    threading.Thread(target=timer_after_gol, daemon=True).start()


def ball_start():
    upr[15] = True
    time.sleep(2)
    upr[15] = False


def timer_knock_ball2():
    upr[15] = True
    time.sleep(3)
    upr[15] = False


# def gol_zv():
    # winsound.PlaySound('win31.wav', winsound.SND_ASYNC | winsound.SND_NOSTOP)


def end_game():
    win = Label(text=f'{"Красный" if upr[1] == 10 else "Синий"} выиграл', font='Arial 50',
                fg="red" if upr[1] == 10 else "blue")
    d.destroy()
    lb.place(x=-100, y=-100)
    lr.place(x=-100, y=-100)
    win.place(x=475, y=300)


threading.Thread(target=winsound.PlaySound("ost.wav", winsound.SND_LOOP | winsound.SND_ASYNC | winsound.SND_NOSTOP),
                 daemon=False).start()
dance()

d.mainloop()
