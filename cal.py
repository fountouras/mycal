from tkinter import *
import math
scn=Tk()
scn.title("kompiouteraki")
n = "0"
show = Label(scn, text=n)
m="0"
def pn1p():#power number 1 press
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="1"
    show.config(text="p"+m)
def pn2p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="2"
    show.config(text="p"+m)
def pn3p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="3"
    show.config(text="p"+m)
def pn4p():
    global m
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="4"
    show.config(text="p"+m)
def pn5p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="5"
    show.config(text="p"+m)
def pn6p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="6"
    show.config(text="p"+m)
def pn7p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="7"
    show.config(text="p"+m)
def pn8p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="8"
    show.config(text="p"+m)
def pn9p():
    global m
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="9"
    show.config(text="p"+m)
def pn0p():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m +="0"
    show.config(text="p"+m)
def pmip():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += "-"
    show.config(text="p"+m)
def ppp():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += "+"
    show.config(text="p"+m)
def pdp():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += "/"
    show.config(text="p"+m)
def pmup():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += "*"
    show.config(text="p"+m)
def pep():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m= str(eval(n))
    show.config(text="p"+m)
def pcp():
    global m
    m = "0"
    show.config(text="p"+m)
def pupp():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += "."
    show.config(text="p"+m)
def pdep():
    global m
    m= m[:-1]
    if m == "":
        m = "0"
    show.config(text="p"+m)
def ppip():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    p=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    m += str(p)
    show.config(text="p"+m)
def psrp():
    global m
    m = str(math.sqrt(int(m)))
    show.config(text=m)
def pparop():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += "("
    show.config(text="p"+m)
def pparcp():
    global m
    if m == "0":
        m = m.replace("0", "", 1)
    m += ")"
    show.config(text="p"+m)
def n1p():#number 1 press
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "1"
    show.config(text=n)
def n2p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "2"
    show.config(text=n)
def n3p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "3"
    show.config(text=n)
def n4p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "4"
    show.config(text=n)
def n5p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "5"
    show.config(text=n)
def n6p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "6"
    show.config(text=n)
def n7p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "7"
    show.config(text=n)
def n8p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "8"
    show.config(text=n)
def n9p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "9"
    show.config(text=n)
def n0p():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "0"
    show.config(text=n)
def mip():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "-"
    show.config(text=n)
def pp():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "+"
    show.config(text=n)
def dp():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "/"
    show.config(text=n)
def mup():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "*"
    show.config(text=n)
def ep():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n = str(eval(n))
    show.config(text=n)
def cp():
    global n
    n = "0"
    show.config(text=n)
def upp():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "."
    show.config(text=n)
def dep():
    global n
    n = n[:-1]
    if n == "":
        n = "0"
    show.config(text=n)
def pip():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    p=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    n += str(p)
    show.config(text=n)
def srp():
    global n
    n = str(math.sqrt(int(n)))
    show.config(text=n)
def parop():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += "("
    show.config(text=n)
def parcp():
    global n
    if n == "0":
        n = n.replace("0", "", 1)
    n += ")"
    show.config(text=n)
def ppowerp():
    global m, n
    r = eval(m)
    n = int(n) ** r
    show.config(text=n)
    n1.config(command=n1p)
    n2.config(command=n2p)
    n3.config(command=n3p)
    n4.config(command=n4p)
    n5.config(command=n5p)
    n6.config(command=n6p)
    n7.config(command=n7p)
    n8.config(command=n8p)
    n9.config(command=n9p)
    n0.config(command=n0p)
    c.config(command=cp)
    mi.config(command=mip)
    mu.config(command=mup)
    e.config(command=ep)
    up.config(command=upp)
    de.config(command=dep)
    pi.config(command=pip)
    power.config(command=powerp)
    p.config(command=pp)
    paro.config(command=parop)
    parc.config(command=parcp)
    sr.config(command=srp)
def powerp():
    m = ""
    n1.config(command=pn1p)
    n2.config(command=pn2p)
    n3.config(command=pn3p)
    n4.config(command=pn4p)
    n5.config(command=pn5p)
    n6.config(command=pn6p)
    n7.config(command=pn7p)
    n8.config(command=pn8p)
    n9.config(command=pn9p)
    n0.config(command=pn0p)
    c.config(command=pcp)
    mi.config(command=pmip)
    mu.config(command=pmup)
    e.config(command=pep)
    up.config(command=pupp)
    de.config(command=pdep)
    pi.config(command=ppip)
    power.config(command=ppowerp)
    p.config(command=ppp)
    show.config(text="p"+m)
    paro.config(command=pparop)
    parc.config(command=pparcp)
    sr.config(command=psrp)
n1 = Button(scn, text="1", command=n1p, height=2, width=7, bg="white")
n2 = Button(scn, text="2", command=n2p, height=2, width=7, bg="white")
n3 = Button(scn, text="3", command=n3p, height=2, width=7, bg="white")
n4 = Button(scn, text="4", command=n4p, height=2, width=7, bg="white")
n5 = Button(scn, text="5", command=n5p, height=2, width=7, bg="white")
n6 = Button(scn, text="6", command=n6p, height=2, width=7, bg="white")
n7 = Button(scn, text="7", command=n7p, height=2, width=7, bg="white")
n8 = Button(scn, text="8", command=n8p, height=2, width=7, bg="white")
n9 = Button(scn, text="9", command=n9p, height=2, width=7, bg="white")
n0 = Button(scn, text="0", command=n0p, height=2, width=7, bg="white")
mi = Button(scn, text="-", command=mip, height=2, width=7)
p = Button(scn, text="+", command=pp, height=2, width=7)
d = Button(scn, text="/", command=dp, height=2, width=7)
mu = Button(scn, text="*", command=mup, height=2, width=7)
e = Button(scn, text="=", command=ep, height=2, width=7)
c = Button(scn, text="c", command=cp, height=2, width=7)
up = Button(scn, text=",", command=upp, height=2, width=7)
de = Button(scn, text="del", command=dep, height=2, width=7)
pi = Button(scn, text="π", command=pip, height=2, width=7)
power = Button(scn, text="power", command=powerp, height=2, width=7)
paro = Button(scn, text="(", command=parop, height=2, width=7)
parc = Button(scn, text=")", command=parcp, height=2, width=7)
sr = Button(scn, text="√", command=srp, height=2, width=7)
show.grid(row=0,column=0,columnspan=2)
n1.grid(row=1,column=0)
n2.grid(row=1,column=1)
n3.grid(row=1,column=2)
n4.grid(row=2,column=0)
n5.grid(row=2,column=1)
n6.grid(row=2,column=2)
n7.grid(row=3,column=0)
n8.grid(row=3,column=1)
n9.grid(row=3,column=2)
n0.grid(row=4,column=1)
mi.grid(row=4,column=3)
p.grid(row=3,column=3)
d.grid(row=2,column=3)
mu.grid(row=1,column=3)
e.grid(row=4,column=2)
c.grid(row=0,column=2)
up.grid(row=4,column=0)
de.grid(row=0,column=3)
pi.grid(row=5,column=0)
power.grid(row=5,column=1)
paro.grid(row=5, column=2)
parc.grid(row=5, column=3)
sr.grid(row=6,column=2, columnspan=4)
scn.mainloop()
