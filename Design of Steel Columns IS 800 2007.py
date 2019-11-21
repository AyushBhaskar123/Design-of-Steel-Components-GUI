from tkinter import*
import math

window=Tk()
window.title("Design of Steel Column")
window.state('zoomed')
window.configure(bg="lightblue1")

u=IntVar()
v=IntVar()
w1=IntVar()
ly=float(0)
lz=float(0)
p=float(0)
Ky=float(1.0)
Kz=float(1.0)

i=int(0)

w1.set(1)

strp=""

heading_label=Label(window,text="STEEL COLUMN DESIGN",fg="blue",bg="lightblue1",font=("Sitka Small Bold",24))
heading_label.place(x=400,y=0)

#photo = PhotoImage(file = r"C:\Users\ayush\Desktop\Documents\Columnphoto.png")
#photoimage = photo.subsample(2,2)

#label=Label(window,image=photoimage)
#label.place(x=1100,y=390)

canvas1=Canvas(window,width=350,height=500,bg="white",borderwidth=2,relief="solid")
canvas1.place(x=315,y=50)

canvas2=Canvas(window,width=350,height=500,bg="white",borderwidth=2,relief="solid")
canvas2.place(x=695,y=50)

canvas3=Canvas(window,width=280,height=330,bg="lemonchiffon",borderwidth=2,relief="solid")
canvas3.place(x=1070,y=50)

canvas4=Canvas(window,width=280,height=330,bg="lavender",borderwidth=2,relief="solid")
canvas4.place(x=10,y=50)

canvas5=Canvas(window,width=280,height=280,bg="lightcyan",borderwidth=2,relief="solid")
canvas5.place(x=10,y=400)

text01=canvas1.create_text(170,490,fill="black",font="Times 12",text="Along Y-Axis")
text02=canvas2.create_text(170,490,fill="black",font="Times 12",text="Along Z-Axis")

stry="length = "+str(ly)+" m"
strz="length = "+str(lz)+" m"

text05=canvas1.create_text(270,300,fill="black",font="Times 10",text=stry)
text06=canvas2.create_text(270,300,fill="black",font="Times 10",text=strz)


def f1():
    canvas1.delete("all")
    
    text1=canvas1.create_text(120,490,fill="black",font="Arial 10",text="Along Y-Axis")
    text2=canvas1.create_text(270,300,fill="black",font="Arial 10",text=stry)
    
    line1=canvas1.create_line(170,170,170,470,width=25)
    
    points1=[170,170,200,140,200,200]
    triangle1=canvas1.create_polygon(points1,outline="blue",fill="white",width=2)

    points2=[170,470,200,440,200,500]
    triangle2=canvas1.create_polygon(points2,outline="blue",fill="white",width=2)
    


def f2():
    canvas1.delete("all")
    
    text1=canvas1.create_text(170,490,fill="black",font="Arial 10",text="Along Y-Axis")
    text2=canvas1.create_text(270,300,fill="black",font="Arial 10",text=stry)
    
    line1=canvas1.create_line(170,170,170,470,width=25)

    points1=[120,170,220,160]
    rectangle1=canvas1.create_rectangle(points1,outline="blue",fill="deepskyblue",width=2)

    points2=[120,470,220,480]
    rectangle2=canvas1.create_rectangle(points2,outline="blue",fill="deepskyblue",width=2)

def f3():
    canvas1.delete("all")
    
    text1=canvas1.create_text(170,490,fill="black",font="Arial 10",text="Along Y-Axis")
    text2=canvas1.create_text(270,300,fill="black",font="Arial 10",text=stry)
    
    line1=canvas1.create_line(170,170,170,470,width=25)

    points2=[120,470,220,480]
    rectangle2=canvas1.create_rectangle(points2,outline="blue",fill="deepskyblue",width=2)

def f4():
    canvas1.delete("all")
    
    text1=canvas1.create_text(170,490,fill="black",font="Arial 10",text="Along Y-Axis")
    text2=canvas1.create_text(270,300,fill="black",font="Arial 10",text=stry)
    
    line1=canvas1.create_line(170,170,170,470,width=25)

    points1=[170,170,200,140,200,200]
    triangle1=canvas1.create_polygon(points1,outline="blue",fill="white",width=2)

    points2=[120,470,220,480]
    rectangle2=canvas1.create_rectangle(points2,outline="blue",fill="deepskyblue",width=2)

def f5():
    canvas2.delete("all")
    
    text2=canvas2.create_text(120,490,fill="black",font="Arial 10",text="Along Z-Axis")
    text3=canvas2.create_text(270,300,fill="black",font="Arial 10",text=strz)
    
    line2=canvas2.create_line(170,170,170,470,width=25)
    
    points1=[170,170,200,140,200,200]
    triangle1=canvas2.create_polygon(points1,outline="blue",fill="white",width=2)

    points2=[170,470,200,440,200,500]
    triangle2=canvas2.create_polygon(points2,outline="blue",fill="white",width=2)

def f6():
    canvas2.delete("all")
    
    text2=canvas2.create_text(170,490,fill="black",font="Arial 10",text="Along Z-Axis")
    text3=canvas2.create_text(270,300,fill="black",font="Arial 10",text=strz)
    
    line2=canvas2.create_line(170,170,170,470,width=25)

    points1=[120,170,220,160]
    rectangle1=canvas2.create_rectangle(points1,outline="blue",fill="deepskyblue",width=2)

    points2=[120,470,220,480]
    rectangle2=canvas2.create_rectangle(points2,outline="blue",fill="deepskyblue",width=2)

def f7():
    canvas2.delete("all")
    
    text2=canvas2.create_text(170,490,fill="black",font="Arial 10",text="Along Z-Axis")
    text3=canvas2.create_text(270,300,fill="black",font="Arial 10",text=strz)
    
    line2=canvas2.create_line(170,170,170,470,width=25)

    points2=[120,470,220,480]
    rectangle2=canvas2.create_rectangle(points2,outline="blue",fill="deepskyblue",width=2)

def f8():
    canvas2.delete("all")
    
    text2=canvas2.create_text(170,490,fill="black",font="Arial 10",text="Along Z-Axis")
    text3=canvas2.create_text(270,300,fill="black",font="Arial 10",text=strz)
    
    line2=canvas2.create_line(170,170,170,470,width=25)

    points1=[170,170,200,140,200,200]
    triangle1=canvas2.create_polygon(points1,outline="blue",fill="white",width=2)

    points2=[120,470,220,480]
    rectangle2=canvas2.create_rectangle(points2,outline="blue",fill="deepskyblue",width=2)

def f9():
    window1=Toplevel()
    window1.title("Add Column")
    window1.geometry("582x300")
    window1.configure(bg="white")

    global ly,stry

    canvas5=Canvas(window1,width=575,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas5.place(x=0,y=40)

    label1=Label(window1,text="Length of Column(m)",fg="black",font=("Arial Bold",20),bg="wheat1")
    label1.place(x=12,y=120)

    entry1=Entry(window1,width=10,borderwidth=2,relief="solid",font=("Arial Bold",20))
    entry1.place(x=365,y=120)

    
    def f22():
        global ly,stry
        
        canvas1.delete("all")
        ly=float(entry1.get())
        stry="length = "+str(ly)+" m"

        text1=canvas1.create_text(170,490,fill="black",font="Arial 10",text="Along Y-Axis")
        line1=canvas1.create_line(170,170,170,470,width=25)
        text100=canvas1.create_text(270,300,fill="black",font="Arial 10",text=stry)
        f110()
        
    def f110():
        window1.destroy()

    btn2=Button(window1,text="ADD COLUMN",fg="black",bg="red",width=19,command=f22,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn2.place(x=0,y=247)

    btn3=Button(window1,text="CANCEL",fg="black",bg="red",width=19,command=f110,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn3.place(x=285,y=247)

    btn4=Button(window1,text="EXIT",fg="black",bg="red",width=9,command=f110,borderwidth=2,relief="raised",font=("Arial Bold",12))
    btn4.place(x=462,y=0)

    window1.mainloop()

def f10():
    window1=Toplevel()
    window1.title("Add Column")
    window1.geometry("582x300")
    window1.configure(bg="white")

    global lz,strz

    canvas5=Canvas(window1,width=575,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas5.place(x=0,y=40)

    label1=Label(window1,text="Length of Column(m)",fg="black",font=("Arial Bold",20),bg="wheat1")
    label1.place(x=12,y=120)

    entry1=Entry(window1,width=10,borderwidth=2,relief="solid",font=("Arial Bold",20))
    entry1.place(x=365,y=120)

    
    def f22():
        global lz,strz
        
        canvas2.delete("all")
        lz=float(entry1.get())
        strz="length = "+str(lz)+" m"
        
        text2=canvas2.create_text(170,490,fill="black",font="Arial 10",text="Along Z-Axis")
        line1=canvas2.create_line(170,170,170,470,width=25)
        text100=canvas2.create_text(270,300,fill="black",font="Arial 10",text=strz)
        f110()
        
    def f110():
        window1.destroy()

    btn2=Button(window1,text="ADD COLUMN",fg="black",bg="red",width=19,command=f22,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn2.place(x=0,y=247)

    btn3=Button(window1,text="CANCEL",fg="black",bg="red",width=19,command=f110,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn3.place(x=285,y=247)

    btn4=Button(window1,text="EXIT",fg="black",bg="red",width=9,command=f110,borderwidth=2,relief="raised",font=("Arial Bold",12))
    btn4.place(x=465,y=0)

    window1.mainloop()

def f11():
    window1=Toplevel()
    window1.title("Add Load")
    window1.geometry("582x300")
    window1.configure(bg="white")

    global p,strp

    canvas6=Canvas(window1,width=575,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas6.place(x=0,y=40)

    label2=Label(window1,text="Load Magnitude(KN)",fg="black",font=("Arial Bold",20),bg="wheat1")
    label2.place(x=13,y=120)

    entry2=Entry(window1,width=10,borderwidth=2,relief="solid",font=("Arial Bold",20))
    entry2.place(x=370,y=120)

    def f22():
        global strp,p
        
        p=float(entry2.get())
        
        pointsp=[170,70,170,170]
        linep1=canvas1.create_line(pointsp,width=4,fill="red",arrow=LAST)
        linep2=canvas2.create_line(pointsp,width=4,fill="red",arrow=LAST)

        strp="P ="+str(p)+" KN"
        textp1=canvas1.create_text(170,50,fill="black",font="Times 15",text=strp)
        textp2=canvas2.create_text(170,50,fill="black",font="Times 15",text=strp)
        
        f110()
        
    def f110():
        window1.destroy()

    btn2=Button(window1,text="ADD LOAD",fg="black",bg="red",width=19,command=f22,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn2.place(x=0,y=247)

    btn3=Button(window1,text="CANCEL",fg="black",bg="red",width=19,command=f110,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn3.place(x=285,y=247)

    btn4=Button(window1,text="EXIT",fg="black",bg="red",width=9,command=f110,borderwidth=2,relief="raised",font=("Arial Bold",12))
    btn4.place(x=463,y=0)

    window1.mainloop()


def f12():

    x=u.get()
    y=v.get()
    z=w1.get()


    global i,Ky,Kz

    window4=Toplevel()
    window4.title("Analysis Result")
    window4.state('zoomed')
    window4.configure(bg="lavender")
    
    if(x==1):
        Ky=float(1.0)
    elif(x==2):
        Ky=float(0.65)
    elif(x==3):
        Ky=float(0.8)
    elif(x==4):
        Ky=float(2.0)

    if (y==1):
        Kz=float(1.0)
    elif(y==2):
        Kz=float(0.65)
    elif(y==3):
        Kz=float(0.8)
    elif(y==4):
        Kz=float(2.0)

    if(z==1):
        ISMB=["ISLB75","ISLB100","ISLB125","ISLB150","ISLB175","ISLB200","ISLB225","ISLB250","ISLB275","ISLB300","ISLB325","ISLB350","ISLB400","ISLB450","ISLB500","ISLB550","ISLB600"]
        w=[6.1,8.0,11.9,14.2,16.7,19.8,23.5,27.9,33.0,37.7,43.1,49.5,56.9,65.3,75.0,86.3,99.5]
        H=[75,100,125,150,175,200,225,250,275,300,325,350,400,450,500,550,600]
        Ze=[19.4,33.6,65.1,91.8,125.3,169.7,222.4,297.4,392.4,488.9,607.7,751.9,965.3,1223.8,1543.2,1933.2,2428.9]
        Zp=[22.35,38.89,73.93,104.50,143.30,184.34,254.72,338.69,443.09,554.32,687.76,851.11,1099.45,1401.35,1773.67,2228.16,2798.56]
        Ae=[7.71,10.21,15.12,18.08,21.30,25.27,29.92,35.53,42.02,48.08,54.90,63.01,72.43,83.14,95.50,109.97,126.69]
        Tf=[5.0,6.4,6.5,6.8,6.9,7.3,8.6,8.2,8.8,9.4,9.8,11.4,12.5,13.4,14.1,15.0,15.5]
        Bf=[50,50,75,80,90,100,100,125,140,150,165,165,165,170,180,190,210]
        Tw=[3.7,4.0,4.4,4.8,5.1,5.4,5.8,6.1,6.4,6.7,7.0,7.4,8.0,8.6,9.2,9.9,10.5]
        Rf=[6.5,7.0,8.0,9.5,9.5,9.5,12.0,13.0,14.0,15.0,16.0,16.0,16.0,16.0,17.0,18.0,20.0]
        Ry=[1.14,1.12,1.69,1.75,1.93,2.13,1.94,2.33,2.61,2.80,3.05,3.17,3.15,3.20,3.34,3.48,3.79]
        Rz=[3.07,4.06,5.19,6.17,7.17,8.19,9.15,10.23,11.31,12.35,13.41,14.45,16.33,18.20,20.10,21.99,23.98]
        Iy=[1.0,12.7,43.4,55.2,79.6,115.4,112.7,193.4,287.0,376.2,510.8,631.9,716.4,853.0,1063.9,1335.1,1821.9]
        Ix=[72.7,168.0,406.8,688.2,1096.2,1696.6,2501.9,3717.8,5375.3,7332.9,9874.6,13158.3,19306.3,27536.1,38579.0,53161.6,72867.6]
        ntimes=len(ISMB)
    elif (z==2):
        ISMB=["ISMB100","ISMB125","ISMB150","ISMB175","ISMB200","ISMB225","ISMB250","ISMB300","ISMB350","ISMB400","ISMB450","ISMB500","ISMB550","ISMB600"]
        w=[11.5,13.0,14.9,19.3,35.4,31.2,37.3,44.2,52.4,61.6,72.4,86.9,103.7,122.6]
        H=[100,125,150,175,200,225,250,300,350,400,450,500,550,600]
        Ze=[51.5,71.8,96.9,145.4,223.5,305.9,410.5,573.6,778.9,1022.9,1350.7,1808.7,2359.8,3060.4]
        Zp=[41.68,81.85,110.48,166.08,253.86,348.27,465.71,651.74,889.57,1176.18,1533.36,2074.67,2711.98,3510.63]
        Ae=[14.60,16.60,19.0,24.62,32.33,39.72,47.55,56.26,66.71,78.46,92.27,110.74,132.11,156.21]
        Tf=[7.2,7.6,7.6,8.6,10.8,11.8,12.5,12.4,14.2,16.0,17.4,17.2,19.3,20.8]
        Bf=[75,75,80,90,100,110,125,140,140,140,150,180,190,210]
        Tw=[4.0,4.4,4.8,5.5,5.7,6.5,6.9,7.5,8.1,8.9,9.4,10.2,11.2,12.0]
        Rf=[9,9,9,10,11,12,13,14,14,14,15,17,18,20]
        Ry=[1.67,1.62,1.66,1.86,2.15,2.34,2.65,2.84,2.84,2.82,3.01,3.52,3.73,4.12]
        Rz=[4.20,5.20,6.18,7.19,8.32,9.31,10.39,12.37,14.29,16.15,18.15,20.21,22.16,24.24]
        Iy=[40.8,43.7,52.6,85.0,150.0,218.3,334.5,453.9,537.7,622.1,834.0,1369.8,1833.8,2651.0]
        Ix=[257.5,449.0,726.4,1272.0,2235.4,3441.8,5131.6,8603.6,13630.3,20458.4,30390.8,45218.3,64893.6,91813.0]
        ntimes=len(ISMB)
    elif (z==3):
        ISMB=["ISHB150","ISHB150","ISHB150","ISHB200","ISHB200","ISHB225","ISHB225","ISHB250","ISHB250","ISHB300","ISHB300","ISHB350","ISHB350","ISHB400","ISHB400","ISHB450","ISHB450"]
        w=[27.1,30.6,34.6,37.3,40.0,43.1,46.8,51.0,54.7,58.8,63.0,67.4,72.4,77.4,82.2,87.2,92.5]
        H=[150,150,150,200,200,225,225,250,250,300,300,350,350,400,400,450,450]
        Ze=[194.1,205.1,218.1,360.8,372.2,469.3,487.0,618.9,638.7,836.3,863.3,1094.8,1131.6,1404.2,1444.2,1742.7,1793.3]
        Zp=[215.64,232.52,251.64,397.23,414.23,515.82,542.22,678.73,708.43,921.68,962.18,1213.53,1268.69,1556.33,1626.36,1955.03,2030.95]
        Ae=[34.48,38.98,44.08,47.54,50.94,54.94,59.66,64.96,69.71,74.85,80.25,85.91,92.21,98.66,104.66,111.14,117.89]
        Tf=[9,9,9,9,9,9.1,9.1,9.7,9.7,10.6,10.6,11.6,11.6,12.7,12.7,13.7,13.7]
        Bf=[150,150,150,200,200,225,225,250,250,250,250,250,250,250,250,250,250]
        Tw=[5.4,8.4,11.8,6.1,7.8,6.5,8.6,6.9,8.8,7.6,9.4,8.3,10.1,9.1,10.6,9.8,11.3]
        Rf=[8,8,8,9,9,10,10,10,10,11,11,12,12,14,14,15,15]
        Ry=[3.54,3.44,3.35,4.51,4.42,4.96,4.84,5.49,5.37,5.41,5.29,5.34,5.22,5.26,5.16,5.18,5.08]
        Rz=[6.5,6.29,6.09,8.71,8.55,9.80,9.58,10.91,10.70,12.95,12.70,14.93,14.65,16.87,16.61,18.78,18.50]
        Iy=[431.7,460.3,494.9,967.1,994.6,1353.8,1396.6,1961.3,2011.7,2193.6,2246.7,2451.4,2510.5,2728.3,2783.0,2985.2,3045.0]
        Ix=[1455.6,1540.0,1635.6,3608.4,3721.8,5279.5,5478.8,7736.5,7983.9,12545.2,12950.2,19159.7,19802.8,28083.5,28823.5,39210.8,40349.9]
        ntimes=len(ISMB)
    elif (z==4):
        ISMB=["ISWB150","ISWB175","ISWB200","ISWB225","ISWB250","ISWB300","ISWB350","ISWB400","ISWB450","ISWB500","ISWB550","ISWB600","ISWB600"]
        w=[17.0,22.1,28.8,33.9,40.9,48.1,56.9,66.7,79.4,95.2,112.5,133.7,145.1]
        H=[150,175,200,225,250,300,350,400,450,500,550,600,600]
        Ze=[111.9,172.5,262.5,348.5,475.4,654.8,887.0,1171.3,1558.1,2091.6,2723.9,3540.0,3854.2]
        Zp=[126.86,194.20,293.99,389.93,527.57,731.21,995.49,1290.19,1760.59,2351.35,3066.29,3986.66,4341.63]
        Ae=[21.67,28.11,36.71,43.24,52.05,61.33,72.50,85.01,101.15,121.22,143.34,170.38,184.86]
        Tf=[7.0,7.4,9.0,9.9,9.0,10.0,11.4,13.0,15.4,14.7,17.6,21.3,23.6]
        Bf=[100,125,140,150,200,200,200,200,200,250,250,250,250]
        Tw=[5.4,5.8,6.1,6.4,6.7,7.4,8.0,8.6,9.2,9.9,10.5,11.2,11.8]
        Rf=[8.0,8.0,9.0,9.0,10.0,11.0,12,13,14,15,16,17,18]
        Ry=[2.09,2.59,2.99,3.22,4.06,4.02,4.03,4.04,4.11,4.96,5.11,5.25,5.35]
        Rz=[6.22,7.33,8.46,9.52,10.69,12.66,14.63,16.60,18.63,20.77,22.86,24.97,25.01]
        Iy=[94.8,188.6,328.8,448.6,857.5,990.1,1175.9,1388.0,1706.7,2987.8,3740.6,4702.5,5298.3]
        Ix=[839.1,1509.4,2624.5,3920.5,5943.1,9821.6,15521.7,23426.7,35057.6,52290.9,74906.1,106198.5,115626.6]
        ntimes=len(ISMB)
    elif (z==5):
        ISMB=["ISLC75","ISLC100","ISLC125","ISLC150","ISLC175","ISLC200","ISLC225","ISLC250","ISLC300","ISLC350","ISLC400"]
        w=[5.7,7.9,10.7,14.4,17.6,20.6,24.0,28.0,33.1,38.8,45.7]
        H=[75,100,125,150,175,200,225,250,300,350,400]
        Ze=[17.6,32.9,57.1,93.0,131.3,172.6,226.5,295.0,403.2,532.1,699.5]
        Zp=[20.61,38.09,65.45,106.17,150.36,198.77,260.13,338.11,466.73,622.95,825.02]
        Ae=[7.26,10.02,13.67,18.36,22.40,26.22,30.53,35.65,42.11,49.47,58.25]
        Tf=[6,6.4,6.6,7.8,9.5,10.8,10.2,10.7,11.6,12.5,14.0]
        Bf=[40,50,65,75,75,75,90,100,100,100,100]
        Tw=[3.7,4.0,4.4,4.8,5.1,5.5,5.8,6.1,6.7,7.4,8.0]
        Rf=[6,6,7,8,8,8.5,11,11,12,13,14]
        Ry=[1.26,1.57,2.05,2.37,2.38,2.37,2.62,2.89,2.87,2.82,2.81]
        Rz=[3.02,4.06,5.11,6.16,7.16,8.11,9.14,10.17,11.98,13.72,15.50]
        Iy=[11.5,24.8,57.2,103.2,126.5,146.9,209.5,298.4,346.0,394.6,460.4]
        Ix=[66.1,164.7,356.8,697.2,1148.4,1725.5,2547.9,3687.9,6047.9,9312.6,13989.5]
        ntimes=len(ISMB)
    elif (z==6):
        ISMB=["ISMC75","ISMC100","ISMC125","ISMC150","ISMC175","ISMC200","ISMC225","ISMC250","ISMC300","ISMC350","ISMC400"]
        w=[6.8,9.2,12.7,16.4,19.1,22.1,25.9,30.4,35.8,42.1,49.4]
        H=[75,100,125,150,175,200,225,250,300,350,400]
        Ze=[20.3,37.3,66.6,103.9,139.8,181.9,239.5,305.3,424.2,571.9,754.1]
        Zp=[24.17,43.83,77.15,119.82,161.65,211.25,277.93,356.72,496.77,672.19,891.03]
        Ae=[8.67,11.70,16.19,20.88,24.38,28.21,33.01,38.67,45.64,53.65,62.93]
        Tf=[7.3,7.5,8.1,9.0,10.2,11.4,12.4,14.1,13.6,13.5,15.3]
        Bf=[40,50,65,75,75,75,80,80,90,100,100]
        Tw=[4.4,4.7,5.0,5.4,5.7,6.1,6.4,7.1,7.6,8.1,8.6]
        Rf=[8.5,9,9.5,10,10.5,11,12,12,13,14,15]
        Ry=[1.21,1.49,1.92,2.21,2.23,2.23,2.38,2.38,2.61,2.83,2.83]
        Rz=[2.96,4.0,5.07,6.11,7.08,8.03,9.03,9.94,11.81,13.66,15.48]
        Iy=[12.6,25.9,59.9,102.3,121.0,140.4,187.2,219.1,310.8,430.6,504.8]
        Ix=[76.0,186.7,416.4,779.4,1223.3,1819.3,2694.6,3816.8,6362.6,10008.0,15082.8]
        ntimes=len(ISMB)
    

    j=int(0)
    while (j<=(ntimes-1)):
        H[j]=H[j]/1000
        Ze[j]=Ze[j]/1000000
        Zp[j]=Zp[j]/1000000
        Ae[j]=Ae[j]/10000
        Tf[j]=Tf[j]/1000
        Bf[j]=Bf[j]/1000
        Tw[j]=Tw[j]/1000
        Rf[j]=Rf[j]/1000
        Ry[j]=Ry[j]/100
        Rz[j]=Rz[j]/100
        Iy[j]=Iy[j]/(10**(8))
        Ix[j]=Ix[j]/(10**(8))
        j=j+1
    Fy=250000
    E=2*(10**8)
    Mew=0.3
    G=E/(2*(1+Mew))
    Gamma=1.1
    result=int(0)
        
    while (i<=(ntimes-1)):
        
        if(z==1 or z==2 or z==3 or z==4):
            
            if((H[i]/Bf[i])>1.2):
                
                if((Tf[i]*(10**3))<=40):
                    
                    Alphaz=0.21
                    Classz="A"
                    
                    Alphay=0.34
                    Classy="B"
                elif (((Tf[i]*(10**3))>=40) and ((Tf[i]*(10**3))<=100)):
                    
                    Alphaz=0.34
                    Classz="B"
                    
                    Alphay=0.49
                    Classy="C"
            elif((H[i]/Bf[i])<=1.2):
                
                if((Tf[i]*(10**3))<=100):
                    
                    Alphaz=0.34
                    Classz="B"
                    
                    Alphay=0.49
                    Classy="C"
                elif ((Tf[i]*(10**3))>100):
                    
                    Alphaz=0.76
                    Classz="D"
                    
                    Alphay=0.76
                    Classy="D"

        if(z==5 or z==6):
            Classy="C"
            Classz="C"

            Alphay=0.49
            Alphaz=0.49

        if(z==1 or z==2 or z==3 or z==4 or z==5 or z==6):
            
            Fccy=(((math.pi)**2)*E)/((Ky*ly/Ry[i])**2)
            Lambday=math.sqrt(Fy/Fccy)
            Phiy=0.5*(1+(Alphay*((Lambday)-0.2))+((Lambday)**2))
            Fcdy=(Fy/Gamma)/(Phiy+(((Phiy**2)-(Lambday**2))**0.5))
            F1=Fcdy*Ae[i]
    
            Fccz=(((math.pi)**2)*E)/((Kz*lz/Rz[i])**2)
            Lambdaz=math.sqrt(Fy/Fccz)
            Phiz=0.5*(1+(Alphaz*(Lambdaz-0.2))+(Lambdaz**2))
            Fcdz=(Fy/Gamma)/(Phiz+(((Phiz**2)-(Lambdaz**2))**0.5))
            F2=Fcdz*Ae[i]

            Pd=min(F1,F2)

            if (p<=Pd):
                if((Ky*ly/Ry[i])<=180):
                    if((Kz*lz/Rz[i])<=180):
                        result=1;
                        break

        i=i+1            

    if (result==1):
        H[i]=H[i]*1000
        Ze[i]=Ze[i]*1000000
        Zp[i]=Zp[i]*1000000
        Ae[i]=Ae[i]*10000
        Tf[i]=Tf[i]*1000
        Bf[i]=Bf[i]*1000
        Tw[i]=Tw[i]*1000
        Rf[i]=Rf[i]*1000
        Ry[i]=Ry[i]*100
        Rz[i]=Rz[i]*100
        Iy[i]=Iy[i]*(10**(8))
        Ix[i]=Ix[i]*(10**(8))



        canvas6=Canvas(window4,width=565,height=650,bg="lavender",borderwidth=2,relief="solid")
        canvas6.place(x=5,y=5)
        label8=Label(window4,text="Selected Section",fg="blue",font=("Verdana Bold",23),bg="lavender")
        label8.place(x=10,y=9)
        label9=Label(window4,text="Name of Section=",fg="black",font=("Sitka Small Bold",15),bg="lavender")
        label9.place(x=10,y=62)
        label10=Label(window4,text=ISMB[i],fg="black",bg="cyan",width=10,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label10.place(x=330,y=65)
        label11=Label(window4,text="Depth of Section(h)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label11.place(x=10,y=160)
        label12=Label(window4,text=round(H[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label12.place(x=370,y=165)
        label13=Label(window4,text="Section Modulus(Ze)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label13.place(x=10,y=210)
        label14=Label(window4,text=round(Ze[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label14.place(x=370,y=215)
        label15=Label(window4,text="Plastic Modulus(Zp)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label15.place(x=10,y=260)
        label16=Label(window4,text=round(Zp[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label16.place(x=370,y=265)
        label17=Label(window4,text="Thickness of Flange(Tf)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label17.place(x=10,y=310)
        label18=Label(window4,text=round(Tf[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label18.place(x=370,y=315)
        label19=Label(window4,text="Width of Flange(Bf)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label19.place(x=10,y=360)
        label20=Label(window4,text=round(Bf[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label20.place(x=370,y=365)
        label21=Label(window4,text="Thickness of Web(Tw)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label21.place(x=10,y=410)
        label21=Label(window4,text=round(Tw[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label21.place(x=370,y=415)
        label22=Label(window4,text="Root Radius(r1)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label22.place(x=10,y=460)
        label23=Label(window4,text=round(Rf[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label23.place(x=370,y=465)
        
        label022=Label(window4,text="Weight per metre(w)=",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label022.place(x=10,y=110)
        label023=Label(window4,text=round(w[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label023.place(x=370,y=115)

        label_22=Label(window4,text="KN/m",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_22.place(x=484,y=120)
        
        label_23=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_23.place(x=489,y=170)

        label_231=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_231.place(x=489,y=220)

        label_2311=Label(window4,text="3",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_2311.place(x=527,y=216)

        label_232=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_232.place(x=489,y=270)

        label_2322=Label(window4,text="3",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_2322.place(x=527,y=266)

        label_233=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_233.place(x=489,y=320)

        label_234=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_234.place(x=489,y=370)

        label_235=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_235.place(x=489,y=420)

        label_236=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_236.place(x=489,y=470)

        label_237=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_237.place(x=489,y=520)

        label_2377=Label(window4,text="4",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_2377.place(x=527,y=516)

        label_238=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_238.place(x=489,y=570)

        label_2388=Label(window4,text="4",fg="black",bg="lavender",font=("Verdana Bold",13))
        label_2388.place(x=527,y=566)
        
        label122=Label(window4,text="Moment of Inertia(Ixx) = ",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label122.place(x=10,y=510)
        label123=Label(window4,text=round(Ix[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label123.place(x=370,y=515)
        label222=Label(window4,text="Moment of Inertia(Iyy) = ",fg="black",bg="lavender",font=("Sitka Small Bold",15))
        label222.place(x=10,y=560)
        label223=Label(window4,text=round(Iy[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label223.place(x=370,y=565)
        

        canvas7=Canvas(window4,width=750,height=210,bg="skyblue",borderwidth=2,relief="solid")
        canvas7.place(x=590,y=450)
        label24=Label(window4,text="FINAL RESULT",fg="blue",bg="skyblue",font=("Verdana Bold",25))
        label24.place(x=600,y=455)
        label25=Label(window4,text="Design Load(P) = ",fg="black",bg="skyblue",font=("Sitka Small Bold",20))
        label25.place(x=600,y=510)
        label26=Label(window4,text=round(p,2),fg="black",bg="yellow",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label26.place(x=1090,y=520)
        label30=Label(window4,text="KN",fg="black",bg="skyblue",font=("Verdana Bold",20))
        label30.place(x=1250,y=520)
        label27=Label(window4,text="Capacity of Section(Pd) = ",fg="black",bg="skyblue",font=("Sitka Small Bold",20))
        label27.place(x=600,y=555)
        label28=Label(window4,text=round(Pd,2),fg="black",bg="yellow",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label28.place(x=1090,y=570)
        label29=Label(window4,text="KN",fg="black",bg="skyblue",font=("Verdana Bold",20))
        label29.place(x=1250,y=565)
        label35=Label(window4,text="P < Pd i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",20),borderwidth=2,relief="solid")
        label35.place(x=620,y=605)

        canvas8=Canvas(window4,width=750,height=215,bg="greenyellow",borderwidth=2,relief="solid")
        canvas8.place(x=590,y=5)
        label24_8=Label(window4,text="CRITERION CHECK ALONG Y-AXIS",fg="blue",bg="greenyellow",font=("Verdana Bold",20))
        label24_8.place(x=600,y=15)
        label25_8=Label(window4,text="Slenderness Ratio(KL/r)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label25_8.place(x=600,y=60)
        label26_8=Label(window4,text=round((Ky*ly*100/Ry[i]),2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label26_8.place(x=970,y=65)
        label36_8=Label(window4,text=" < 180 i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
        label36_8.place(x=1090,y=60)
        label27_8=Label(window4,text="Compressive Stress(Fcd)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label27_8.place(x=600,y=100)
        label28_8=Label(window4,text=round(Fcdy/1000,2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label28_8.place(x=970,y=105)
        label37_8=Label(window4,text="N/mm",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label37_8.place(x=1090,y=104)
        label38_8=Label(window4,text="2",fg="black",bg="greenyellow",font=("Verdana Bold",13))
        label38_8.place(x=1182,y=104)
        label39_8=Label(window4,text="Sectional Area(Ae)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label39_8.place(x=600,y=140)
        label40_8=Label(window4,text=round(Ae[i],2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label40_8.place(x=970,y=145)
        label41_8=Label(window4,text="mm",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label41_8.place(x=1110,y=140)
        label42_8=Label(window4,text="2",fg="black",bg="greenyellow",font=("Verdana Bold",13))
        label42_8.place(x=1167,y=136)
        label43_8=Label(window4,text="Strength of Column(P1)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label43_8.place(x=600,y=180)
        label44_8=Label(window4,text=round(F1,2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label44_8.place(x=970,y=185)
        label45_8=Label(window4,text="KN",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label45_8.place(x=1110,y=180)

        canvas9=Canvas(window4,width=750,height=215,bg="greenyellow",borderwidth=2,relief="solid")
        canvas9.place(x=590,y=230)
        label24_9=Label(window4,text="CRITERION CHECK ALONG Z-AXIS",fg="blue",bg="greenyellow",font=("Verdana Bold",20))
        label24_9.place(x=600,y=235)
        label25_9=Label(window4,text="Slenderness Ratio(KL/r)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label25_9.place(x=600,y=280)
        label26_9=Label(window4,text=round((Kz*lz*100/Rz[i]),2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label26_9.place(x=970,y=285)
        label36_9=Label(window4,text=" < 180 i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
        label36_9.place(x=1090,y=280)
        label27_9=Label(window4,text="Compressive Stress(Fcd)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label27_9.place(x=600,y=320)
        label28_9=Label(window4,text=round(Fcdz/1000,2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label28_9.place(x=970,y=325)
        label37_9=Label(window4,text="N/mm",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label37_9.place(x=1090,y=324)
        label38_9=Label(window4,text="2",fg="black",bg="greenyellow",font=("Verdana Bold",13))
        label38_9.place(x=1182,y=324)
        label39_9=Label(window4,text="Sectional Area(Ae)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label39_9.place(x=600,y=360)
        label40_9=Label(window4,text=round(Ae[i],2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label40_9.place(x=970,y=365)
        label41_9=Label(window4,text="mm",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label41_9.place(x=1110,y=360)
        label42_9=Label(window4,text="2",fg="black",bg="greenyellow",font=("Verdana Bold",13))
        label42_9.place(x=1167,y=356)
        label43_9=Label(window4,text="Strength of Column(P1)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",15))
        label43_9.place(x=600,y=400)
        label44_9=Label(window4,text=round(F2,2),fg="black",bg="yellow",width=6,font=("Verdana Bold",15),borderwidth=2,relief="solid")
        label44_9.place(x=970,y=405)
        label45_9=Label(window4,text="KN",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label45_9.place(x=1110,y=400)

        label90=Label(window4,text="Do you want to get the next best design.....Click on NEXT Button",fg="black",font=("Sitka Small Bold",12),bg="green")
        label90.place(x=300,y=655)


    def next_page():
        global i
        i=i+1
        window4.destroy()
        f12()
    def previous_page():
        global i
        i=i-1
        window4.destroy()
        f12()
    def exit_window4():
        window4.destroy()
        global i
        i=0

    nextbtn=Button(window4,text="NEXT",fg="black",bg="red",width=7,command=next_page,borderwidth=2,relief="raised",font=("Verdana Bold",14))
    nextbtn.place(x=1250,y=650)

    previousbtn=Button(window4,text="PREVIOUS",fg="black",bg="red",width=8,command=previous_page,borderwidth=2,relief="raised",font=("Verdana Bold",15))
    previousbtn.place(x=0,y=645)

    exitbtn4=Button(window4,text="EXIT",fg="black",bg="red",width=7,command=exit_window4,borderwidth=2,relief="raised",font=("Verdana Bold",15))
    exitbtn4.place(x=1250,y=0)    

    window4.mainloop()

def exit_window():
    window.destroy()

def reset_all():
    global u,v
    u.set(0)
    v.set(0)
    canvas1.delete("all")
    canvas2.delete("all")
    

radio1=Radiobutton(window,text="Pinned Supports",variable=u,value=1,command=f1,fg="black",bg="lavender",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio1.place(x=20,y=170)

radio2=Radiobutton(window,text="Fixed Support",variable=u,value=2,command=f2,fg="black",bg="lavender",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio2.place(x=20,y=225)

radio3=Radiobutton(window,text="Cantilever Support",variable=u,value=3,command=f3,fg="black",bg="lavender",font=("Sitka Small Bold",14),borderwidth=2,relief="solid")
radio3.place(x=20,y=280)

radio4=Radiobutton(window,text="Propped Cantilever",variable=u,value=4,command=f4,fg="black",bg="lavender",font=("Sitka Small Bold",14),borderwidth=2,relief="solid")
radio4.place(x=20,y=332)

radio5=Radiobutton(window,text="Pinned Supports",variable=v,value=1,command=f5,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio5.place(x=1080,y=170)

radio6=Radiobutton(window,text="Fixed Support",variable=v,value=2,command=f6,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio6.place(x=1080,y=225)

radio7=Radiobutton(window,text="Cantilever Support",variable=v,value=3,command=f7,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",14),borderwidth=2,relief="solid")
radio7.place(x=1080,y=280)

radio8=Radiobutton(window,text="Propped Cantilever",variable=v,value=4,command=f8,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",14),borderwidth=2,relief="solid")
radio8.place(x=1080,y=332)

sectionpreference_label=Label(window,text="Preferred Section",fg="blue",bg="lightcyan",font=("Sitka Small Bold",17))
sectionpreference_label.place(x=14,y=404)

alongyaxis_label=Label(window,text="Along Y-Axis",fg="blue",bg="lavender",font=("Sitka Small Bold",20))
alongyaxis_label.place(x=35,y=54)

alongzaxis_label=Label(window,text="Along Z-Axis",fg="blue",bg="lemonchiffon",font=("Sitka Small Bold",20))
alongzaxis_label.place(x=1105,y=54)

radio9=Radiobutton(window,text="ISLB",variable=w1,value=1,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio9.place(x=20,y=450)

radio10=Radiobutton(window,text="ISMB",variable=w1,value=2,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio10.place(x=20,y=505)

radio11=Radiobutton(window,text="ISHB",variable=w1,value=3,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio11.place(x=20,y=560)

radio12=Radiobutton(window,text="ISWB",variable=w1,value=4,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio12.place(x=20,y=615)

radio13=Radiobutton(window,text="ISLC",variable=w1,value=5,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio13.place(x=170,y=450)

radio14=Radiobutton(window,text="ISMC",variable=w1,value=6,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio14.place(x=170,y=505)

btn1=Button(window,text="ADD COLUMN",fg="black",bg="red",width=17,command=f9,borderwidth=2,relief="raised",font=("Verdana Bold",13))
btn1.place(x=21,y=110)

btn2=Button(window,text="ADD COLUMN",fg="black",bg="red",width=17,command=f10,borderwidth=2,relief="raised",font=("Verdana Bold",13))
btn2.place(x=1081,y=110)

btn3=Button(window,text="ADD LOAD",fg="black",bg="red",width=8,command=f11,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn3.place(x=1058,y=640)

btn4=Button(window,text="RESULT",fg="black",bg="red",width=8,command=f12,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn4.place(x=1212,y=640)

exitbtn1=Button(window,text="EXIT",fg="black",bg="red",width=8,command=exit_window,borderwidth=2,relief="raised",font=("Times New Roman Bold",14))
exitbtn1.place(x=1245,y=0)

helpbtn1=Button(window,text="HELP",fg="black",bg="red",width=8,command=exit_window,borderwidth=2,relief="raised",font=("Times New Roman Bold",14))
helpbtn1.place(x=1123,y=0)

resetbtn1=Button(window,text="RESET",fg="black",bg="red",width=8,command=reset_all,borderwidth=2,relief="raised",font=("Times New Roman Bold",14))
resetbtn1.place(x=1001,y=0)

window.mainloop()
