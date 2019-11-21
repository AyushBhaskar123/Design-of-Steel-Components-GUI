from tkinter import*
import math
import matplotlib.pyplot as plt
from decimal import *

window=Tk()
window.title("Design of Steel Beam")
#window.geometry("1050x400")
#window.attributes('-fullscreen', True)
window.state('zoomed')
window.tk.call('tk', 'scaling', 1.3)
window.configure(bg="lightblue1")
height = window.winfo_screenmmheight()

u=IntVar()
v=IntVar()
u.set(1)

heading_label=Label(window,text="STEEL  BEAM  DESIGN",fg="blue",bg="lightblue1",font=("Sitka Small Bold",50))
heading_label.place(x=250,y=0)

canvas=Canvas(window,width=900,height=300,bg="white",borderwidth=2,relief="solid")
canvas.place(x=10,y=370)

photo = PhotoImage(file = r"C:\Users\ayush\Desktop\Documents\beam.png")
photoimage = photo.subsample(1,1)

label_image=Label(window,image=photoimage)
label_image.place(x=60,y=10)

photo2 = PhotoImage(file = r"C:\Users\ayush\Desktop\Documents\bridgebeam.png")
photoimage2 = photo2.subsample(5,5)

label_image2=Label(window,image=photoimage2)
label_image2.place(x=930,y=370)

text3=canvas.create_text(110,290,fill="black",font="Arial 15",text="")
text4=canvas.create_text(780,290,fill="black",font="Arial 15",text="")
text5=canvas.create_text(75,130,fill="black",font="Arial 15",text="")

def reset_life():
    text3=canvas.create_text(110,290,fill="black",font="Arial 15",text="")
    text4=canvas.create_text(780,290,fill="black",font="Arial 15",text="")
    text5=canvas.create_text(75,130,fill="black",font="Arial 15",text="")

text100=canvas.create_text(800,20,fill="black",font="Times 10",text="")

l=Decimal(0)
p=Decimal(0)
w=Decimal(0)
w1=Decimal(0)
w2=Decimal(0)
a=Decimal(0)
b=Decimal(0)
R1=Decimal(0)
R2=Decimal(0)
M1=Decimal(0)
V,M,Z=[],[],[]
x=[]

canvas1=Canvas(window,width=260,height=210,bg="white",borderwidth=2,relief="solid")
canvas1.place(x=10,y=150)

canvas2=Canvas(window,width=400,height=210,bg="lightcyan",borderwidth=2,relief="solid")
canvas2.place(x=280,y=150)

canvas3=Canvas(window,width=350,height=210,bg="lavender",borderwidth=2,relief="solid")
canvas3.place(x=690,y=150)

canvas4=Canvas(window,width=300,height=280,bg="lemonchiffon",borderwidth=2,relief="solid")
canvas4.place(x=1050,y=150)

label1=Label(window,text="Type of Beam",fg="royalblue1",font=("Sitka Small Bold",25),bg="white")
label1.place(x=20,y=154)

label2=Label(window,text="Type of Load",fg="saddlebrown",font=("Sitka Small Bold",25),bg="lightcyan")
label2.place(x=290,y=154)

radio1=Radiobutton(window,text="Simply Supported",variable=u,value=1,fg="black",bg="white",font=("Arial Bold",19),borderwidth=2,relief="solid")
radio1.place(x=20,y=220)

radio2=Radiobutton(window,text="Cantilever",variable=u,value=2,fg="black",bg="white",font=("Arial Bold",20),borderwidth=2,relief="solid")
radio2.place(x=20,y=270)

var1=IntVar()
var2=IntVar()
var1.set(1)
var2.set(1)

label3=Label(window,text="Support Conditions",fg="red",bg="lavender",font=("Sitka Small Bold",25))
label3.place(x=700,y=154)

label4=Label(window,text="Type of Sections",fg="navy",font=("Sitka Small Bold",25),bg="lemonchiffon")
label4.place(x=1055,y=154)

radio5=Radiobutton(window,text="Laterally Supported",variable=var1,value=1,fg="black",font=("Arial Bold",20),bg="lavender",borderwidth=2,relief="solid")
radio5.place(x=700,y=220)

radio6=Radiobutton(window,text="Laterally Unsupported",variable=var1,value=2,fg="black",font=("Arial Bold",20),bg="lavender",borderwidth=2,relief="solid")
radio6.place(x=700,y=270)

radio7=Radiobutton(window,text="ISLB",variable=var2,value=1,fg="black",font=("Arial Bold",20),bg="lemonchiffon",borderwidth=2,relief="solid")
radio7.place(x=1060,y=220)

radio8=Radiobutton(window,text="ISMB",variable=var2,value=2,fg="black",font=("Arial Bold",20),bg="lemonchiffon",borderwidth=2,relief="solid")
radio8.place(x=1060,y=270)

radio9=Radiobutton(window,text="ISWB",variable=var2,value=3,fg="black",font=("Arial Bold",20),bg="lemonchiffon",borderwidth=2,relief="solid")
radio9.place(x=1060,y=320)

radio10=Radiobutton(window,text="Economical Section",variable=var2,value=4,fg="black",font=("Arial Bold",20),bg="lemonchiffon",borderwidth=2,relief="solid")
radio10.place(x=1060,y=370)

i=int(0)

def f1():
    window1=Toplevel()
    window1.title("Add Beam")
    window1.geometry("585x300")
    window1.configure(bg="white")

    canvas5=Canvas(window1,width=575,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas5.place(x=0,y=40)

    global l,V,M,x,Z
    global text3,text4,text100
    
    label1=Label(window1,text="Length of Beam(m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label1.place(x=30,y=120)

    entry1=Entry(window1,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry1.place(x=350,y=120)

    def f22():
        global l,V,M,x,Z
        global text3,text4
        l=Decimal(entry1.get())
        q=Decimal(0)
        while(q<=(l+Decimal(0.1))):
            V.append(0.0)
            M.append(0.0)
            Z.append(0.0)
            q=q+Decimal(0.1)
        #canvas.itemconfigure(text100,text=len(V))
        
        line1=canvas.create_line(50,200,850,200,width=8)
        if((u.get())==1):
            points1=[50,200,75,225,25,225]
            triangle1=canvas.create_polygon(points1,outline="black",fill="white",width=2)

            points01=[825,200,860,225]
            circle1=canvas.create_oval(points01,outline="black",fill="white",width=3)

            points3=[50,300,50,225]
            line3=canvas.create_line(points3,width=2,fill="red",arrow=LAST)
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            points4=[850,300,850,225]
            line4=canvas.create_line(points4,width=2,fill="red",arrow=LAST)
            

            str4="R2 ="+str(round(R2,2))+" KN"
            canvas.itemconfigure(text4,text=str4)

            
        if((u.get())==2):
            points1=[30,150,50,250]
            rectangle1=canvas.create_rectangle(points1,outline="black",fill="deepskyblue",width=2)

            points3=[40,300,40,225]
            line3=canvas.create_line(points3,width=2,fill="red",arrow=LAST)

            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str04="M1 ="+str(round(M1,2))+" KN.m"
            canvas.itemconfigure(text5,text=str04)
        
        f10()

    def f10():
        window1.destroy()

    btn2=Button(window1,text="ADD BEAM",fg="black",bg="red",width=18,command=f22,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn2.place(x=0,y=247)

    btn3=Button(window1,text="CANCEL",fg="black",bg="red",width=18,command=f10,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn3.place(x=285,y=247)

    btn4=Button(window1,text="EXIT",fg="black",bg="red",width=10,command=f10,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn4.place(x=450,y=0)

    window1.mainloop()


def f3():
    window2=Toplevel()
    window2.title("Add Point Load")
    window2.geometry("585x300")
    window2.configure(bg="white")

    global p,a
    global R1,R2,V,M,x,M1,Z
    global text3,text4,text100

    canvas6=Canvas(window2,width=575,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas6.place(x=0,y=40)

    label2=Label(window2,text="Load Magnitude(KN)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label2.place(x=30,y=80)

    label2=Label(window2,text="Load Position(m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label2.place(x=30,y=160)

    entry2=Entry(window2,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry2.place(x=360,y=80)
    
    entry3=Entry(window2,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry3.place(x=360,y=160)

    def f4():
        global l
        global p,a
        global R1,R2,V,M,x,M1,Z
        global text3,text4,text100
        p=Decimal(entry2.get())
        a=Decimal(entry3.get())

        o=Decimal(a/l)
        points2=[(50)+(o)*800,70,(50)+(o)*800,200]
        line2=canvas.create_line(points2,width=2,fill="blue",arrow=LAST)

        str2="P ="+str(round(p,2))+" KN"
        text2=canvas.create_text((50)+(o)*800,60,fill="black",font="Arial 15",text=str2)
        if((u.get())==1):
            r1=(p*(l-a)/l)
            r2=(p*a/l)
            R1=R1+r1
            R2=R2+r2

            x1,x2=[],[]
            v1,v2=[],[]
            m1,m2=[],[]
            z1,z2=[],[]
            b=Decimal(a+Decimal(0.1))
            q,r=Decimal(0.0),Decimal(b)
            while (q<=b):
                x1.append(q)
                q=Decimal(q+Decimal(0.1))
            while (r>=(b) and r<=(l+Decimal(0.1))):
                x2.append(r)
                r=Decimal(r+Decimal(0.1))
            l1,l2=len(x1),len(x2)
            p1,p2=0,0
            while (p1<=(l1-1)):
                v1.append(float(r1))
                m1.append(float(r1*x1[p1]))
                z1.append(float((p*(l-a)*x1[p1]/(6*l))*((l**2)-((l-a)**2)-(x1[p1]**2))))
                p1=(p1)+1
            while (p2<=(l2-1)):
                v1.append(float(-r2))
                m1.append(float(r2*(l-x2[p2])))
                z1.append(float((p*a*(l-x2[p2])/(6*l))*((2*l*x2[p2])-(x2[p2]**2)-(a**2))))
                p2=(p2)+1
            v_point=v1
            m_point=m1
            x=x1+x2
            V= [V[i] + v1[i] for i in range(len(v_point))] 
            M= [M[i] + m1[i] for i in range(len(v_point))]
            Z= [Z[i] + z1[i] for i in range(len(v_point))]
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str4="R2 ="+str(round(R2,2))+" KN"
            canvas.itemconfigure(text4,text=str4)
            
        if((u.get())==2):
            r1=p
            m11=p*a
            
            R1=R1+r1
            M1=M1+m11

            x1,x2=[],[]
            v1,v2=[],[]
            m1,m2=[],[]
            z1,z2=[],[]
            b=Decimal(a+Decimal(0.1))
            q,r=Decimal(0.0),Decimal(b)
            while (q<=b):
                x1.append(q)
                q=Decimal(q+Decimal(0.1))
            while (r>=(b) and r<=(l+Decimal(0.1))):
                x2.append(r)
                r=Decimal(r+Decimal(0.1))
            l1,l2=len(x1),len(x2)
            p1,p2=0,0
            while (p1<=(l1-1)):
                v1.append(float(r1))
                m1.append(float(r1*x1[p1]))
                z1.append(float((p*(x1[p1]**2)/6)*((3*a)-x1[p1])))
                p1=(p1)+1
            while (p2<=(l2-1)):
                v1.append(float(0))
                m1.append(float(0))
                z1.append(float((p*(a**2)/6)*((3*x2[p2])-a)))
                p2=(p2)+1
            v_point=v1
            m_point=m1
            x=x1+x2
            V= [V[i] + v1[i] for i in range(len(v_point))] 
            M= [M[i] + m1[i] for i in range(len(v_point))]
            Z= [Z[i] + z1[i] for i in range(len(v_point))]
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str4="M1 ="+str(round(M1,2))+" KN.m"
            canvas.itemconfigure(text5,text=str4)

        f11()
    def f11():
        window2.destroy()
        
        
    btn6=Button(window2,text="ADD LOAD",fg="black",bg="red",width=18,command=f4,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn6.place(x=0,y=247)
    
    btn7=Button(window2,text="CANCEL",fg="black",bg="red",width=18,command=f11,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn7.place(x=285,y=247)

    btn8=Button(window2,text="EXIT",fg="black",bg="red",width=10,command=f11,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn8.place(x=450,y=0)

    window2.mainloop()


def com_udl():
    window_udl=Toplevel()
    window_udl.title("Add Uniformly Distributed Load")
    window_udl.geometry("585x300")
    window_udl.configure(bg="white")

    global w,a,b
    global R1,R2,V,M,x,M1,Z
    global text3,text4

    canvas7=Canvas(window_udl,width=575,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas7.place(x=0,y=40)

    label2_udl=Label(window_udl,text="Load Magnitude(KN/m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label2_udl.place(x=15,y=50)

    label2_udl=Label(window_udl,text="Load Start Position(m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label2_udl.place(x=15,y=120)

    label3_udl=Label(window_udl,text="Load End Position(m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label3_udl.place(x=15,y=190)

    entry2_udl=Entry(window_udl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry2_udl.place(x=375,y=50)
    
    entry3_udl=Entry(window_udl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry3_udl.place(x=375,y=120)

    entry4_udl=Entry(window_udl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry4_udl.place(x=375,y=190)

    def f4():
        global l
        global w,a,b
        global R1,R2,V,M,x,M1,Z
        global text3,text4
        w=Decimal(entry2_udl.get())
        a=Decimal(entry3_udl.get())
        b=Decimal(entry4_udl.get())

        m_udl1=Decimal(a/l)
        n_udl1=Decimal(b/l)

        line3_udl=canvas.create_line((50)+(m_udl1)*800,140,(50)+(m_udl1)*800,200,arrow=LAST,fill="black",width=2)
        line4_udl=canvas.create_line((50)+(m_udl1)*800,140,(50)+(n_udl1)*800,140,fill="black",width=2)
        line5_udl=canvas.create_line((50)+(n_udl1)*800,140,(50)+(n_udl1)*800,200,arrow=LAST,fill="black",width=2)

        str2_udl="W ="+str(round(w,2))+" KN/m"
        text2_udl=canvas.create_text((50)+((m_udl1+n_udl1)/2)*800,130,fill="black",font="Arial 15",text=str2_udl)
        if((u.get())==1):
            r2=((w*(b-a)*(b+a)/l)/2)
            r1=((w*(b-a))-r2)

            R1=R1+r1
            R2=R2+r2

            C5=(-r2*((b-l)**2)*(l+(2*b))/(6*l))+(w*((b-a)**3)*(a+(3*b))/(24*l))-(r1*(b**3)/(3*l))
            C6=-C5*l
            C1=(C5)+(r2*((b-l)**2)/2)-(w*((b-a)**3)/6)+(r1*(b**2)/2)


            
            x1_udl,x2_udl,x3_udl=[],[],[]
            v1_udl,v2_udl,v3_udl=[],[],[]
            m1_udl,m2_udl,m3_udl=[],[],[]
            z1_udl,z2_udl,z3_udl=[],[],[]
            q_udl,r_udl,s_udl=Decimal(0),Decimal(a+Decimal(0.1)),Decimal(b+Decimal(0.1))
            c1=Decimal(a+Decimal(0.1))
            c2=Decimal(b+Decimal(0.1))
            while (q_udl<=c1):
                x1_udl.append(q_udl)
                q_udl=Decimal(q_udl+Decimal(0.1))
            while (r_udl>=c1 and r_udl<=c2):
                x2_udl.append(r_udl)
                r_udl=Decimal(r_udl+Decimal(0.1))
            while (s_udl>=c2 and s_udl<=Decimal(l+Decimal(0.1))):
                x3_udl.append(s_udl)
                s_udl=Decimal(s_udl+Decimal(0.1))
            l1_udl,l2_udl,l3_udl=len(x1_udl),len(x2_udl),len(x3_udl)
            p1_udl,p2_udl,p3_udl=0,0,0
            while (p1_udl<=(l1_udl-1)):
                v1_udl.append(float(r1))
                m1_udl.append(float(r1*x1_udl[p1_udl]))
                z1_udl.append(float((-r1*(x1_udl[p1_udl]**3)/6)+(C1*x1_udl[p1_udl])))
                p1_udl=(p1_udl)+1
            while (p2_udl<=(l2_udl-1)):
                v2_udl.append(float(r1-w*(x2_udl[p2_udl]-a)))
                m2_udl.append(float((r1*x2_udl[p2_udl])-(w*((x2_udl[p2_udl]-a)**2)/2)))
                z2_udl.append(float((w*((x2_udl[p2_udl]-a)**4)/24)-(r1*((x2_udl[p2_udl])**3)/6)+(C1*x2_udl[p2_udl])))
                p2_udl=(p2_udl)+1
            while (p3_udl<=(l3_udl-1)):
                v3_udl.append(float(-r2))
                m3_udl.append(float(r2*(l-x3_udl[p3_udl])))
                z3_udl.append(float((r2*((x3_udl[p3_udl]-l)**3)/6)+(C5*x3_udl[p3_udl])+(C6)))
                p3_udl=(p3_udl)+1

            v_udl=v1_udl+v2_udl+v3_udl
            m_udl=m1_udl+m2_udl+m3_udl
            z_udl=z1_udl+z2_udl+z3_udl
            x=x1_udl+x2_udl+x3_udl
            
            #canvas.itemconfigure(text100,text=len(x))
            
            V= [V[i] + v_udl[i] for i in range(len(v_udl))] 
            M= [M[i] + m_udl[i] for i in range(len(m_udl))]
            Z= [Z[i] + z_udl[i] for i in range(len(z_udl))]
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str4="R2 ="+str(round(R2,2))+" KN"
            canvas.itemconfigure(text4,text=str4)
        if((u.get())==2):
            r1=w*(b-a)
            m11=(w*(b-a)*(b+a))/2

            R1=R1+r1
            M1=M1+m11

            C5=(m11*b)-(r1*(b**2)/2)+(w*((b-a)**3)/6)
            C6=(-m11*(b**2)/2)+(r1*(b**3)/3)+(w*((b-a)**4)/24)-(w*b*((b-a)**3)/6)

            x1_udl,x2_udl,x3_udl=[],[],[]
            v1_udl,v2_udl,v3_udl=[],[],[]
            m1_udl,m2_udl,m3_udl=[],[],[]
            z1_udl,z2_udl,z3_udl=[],[],[]
            q_udl,r_udl,s_udl=Decimal(0),Decimal(a+Decimal(0.1)),Decimal(b+Decimal(0.1))
            c1=Decimal(a+Decimal(0.1))
            c2=Decimal(b+Decimal(0.1))
            while (q_udl<=c1):
                x1_udl.append(q_udl)
                q_udl=Decimal(q_udl+Decimal(0.1))
            while (r_udl>=c1 and r_udl<=c2):
                x2_udl.append(r_udl)
                r_udl=Decimal(r_udl+Decimal(0.1))
            while (s_udl>=c2 and s_udl<=Decimal(l+Decimal(0.1))):
                x3_udl.append(s_udl)
                s_udl=Decimal(s_udl+Decimal(0.1))
            l1_udl,l2_udl,l3_udl=len(x1_udl),len(x2_udl),len(x3_udl)
            p1_udl,p2_udl,p3_udl=0,0,0
            while (p1_udl<=(l1_udl-1)):
                v1_udl.append(float(r1))
                m1_udl.append(float((r1*x1_udl[p1_udl])-m11))
                z1_udl.append(float((m11*(x1_udl[p1_udl]**2)/2)-(r1*(x1_udl[p1_udl]**3)/6)))
                p1_udl=(p1_udl)+1
            while (p2_udl<=(l2_udl-1)):
                v2_udl.append(float(r1-w*(x2_udl[p2_udl]-a)))
                m2_udl.append(float((r1*x2_udl[p2_udl])-(w*((x2_udl[p2_udl]-a)**2)/2)-(m11)))
                z2_udl.append(float((m11*(x2_udl[p2_udl]**2)/2)-(r1*(x2_udl[p2_udl]**3)/6)+(w*((x2_udl[p2_udl]-a)**4)/24)))
                p2_udl=(p2_udl)+1
            while (p3_udl<=(l3_udl-1)):
                v3_udl.append(float(0))
                m3_udl.append(float(0))
                z3_udl.append(float((C5*x3_udl[p3_udl])+(C6)))
                p3_udl=(p3_udl)+1

            v_udl=v1_udl+v2_udl+v3_udl
            m_udl=m1_udl+m2_udl+m3_udl
            z_udl=z1_udl+z2_udl+z3_udl
            x=x1_udl+x2_udl+x3_udl
            
            #canvas.itemconfigure(text100,text=len(x))
            
            V= [V[i] + v_udl[i] for i in range(len(v_udl))] 
            M= [M[i] + m_udl[i] for i in range(len(m_udl))]
            Z= [Z[i] + z_udl[i] for i in range(len(z_udl))]
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str4="M1 ="+str(round(M1,2))+" KN.m"
            canvas.itemconfigure(text5,text=str4)

            
        
        f11()
    def f11():
        window_udl.destroy()
        
        
    btn6=Button(window_udl,text="ADD LOAD",fg="black",bg="red",width=18,command=f4,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn6.place(x=0,y=247)
    
    btn7=Button(window_udl,text="CANCEL",fg="black",bg="red",width=18,command=f11,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn7.place(x=285,y=247)

    btn8=Button(window_udl,text="EXIT",fg="black",bg="red",width=10,command=f11,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn8.place(x=450,y=0)

    window_udl.mainloop()


def com_uvl():
    window_uvl=Toplevel()
    window_uvl.title("Add Uniformly Varying Load")
    window_uvl.geometry("640x300")
    window_uvl.configure(bg="white")

    global w1,w2,a,b
    global R1,R2,V,M,x,M1,Z
    global text3,text4,text100

    canvas8=Canvas(window_uvl,width=630,height=200,borderwidth=2,relief="solid",bg="wheat1")
    canvas8.place(x=0,y=40)

    label1_uvl=Label(window_uvl,text="Load Start Magnitude(KN/m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label1_uvl.place(x=10,y=50)

    label2_uvl=Label(window_uvl,text="Load End Magnitude(KN/m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label2_uvl.place(x=10,y=100)

    label3_uvl=Label(window_uvl,text="Load Start Position(m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label3_uvl.place(x=10,y=150)

    label4_uvl=Label(window_uvl,text="Load End Position(m)",fg="black",font=("Arial Bold",25),bg="wheat1")
    label4_uvl.place(x=10,y=200)

    entry1_uvl=Entry(window_uvl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry1_uvl.place(x=440,y=50)
    
    entry2_uvl=Entry(window_uvl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry2_uvl.place(x=440,y=100)

    entry3_uvl=Entry(window_uvl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry3_uvl.place(x=440,y=150)

    entry4_uvl=Entry(window_uvl,width=10,borderwidth=2,relief="solid",font=("Arial Bold",25))
    entry4_uvl.place(x=440,y=200)

    def f4():
        global l
        global w1,w2,a,b
        global R1,R2,V,M,x,M1,Z
        global text3,text4,text100
        w1=Decimal(entry1_uvl.get())
        w2=Decimal(entry2_uvl.get())
        a=Decimal(entry3_uvl.get())
        b=Decimal(entry4_uvl.get())

        m_uvl1=Decimal(a/l)
        n_uvl1=Decimal(b/l)

        if(w1<=w2):
            line3_uvl=canvas.create_line((50)+(m_uvl1)*800,160,(50)+(m_uvl1)*800,200,arrow=LAST,fill="black",width=2)
            line4_uvl=canvas.create_line((50)+(m_uvl1)*800,160,(50)+(n_uvl1)*800,120,fill="black",width=2)
            line5_uvl=canvas.create_line((50)+(n_uvl1)*800,120,(50)+(n_uvl1)*800,200,arrow=LAST,fill="black",width=2)
        else:
            line3_uvl=canvas.create_line((50)+(m_uvl1)*800,120,(50)+(m_uvl1)*800,200,arrow=LAST,fill="black",width=2)
            line4_uvl=canvas.create_line((50)+(m_uvl1)*800,120,(50)+(n_uvl1)*800,160,fill="black",width=2)
            line5_uvl=canvas.create_line((50)+(n_uvl1)*800,160,(50)+(n_uvl1)*800,200,arrow=LAST,fill="black",width=2)

        str3_uvl="w1 ="+str(round(w1,2))+" KN/m"
        str4_uvl="w2 ="+str(round(w2,2))+" KN/m"
        text3_uvl=canvas.create_text((75)+m_uvl1*800,180,fill="black",font="Arial 15",text=str3_uvl)
        text4_uvl=canvas.create_text((55)+n_uvl1*800,180,fill="black",font="Arial 15",text=str4_uvl)
        if((u.get())==1):
            r2=((b-a)/(6*l))*((w1*(2*a+b))+(w2*(2*b+a)))
            r1=((w1+w2)*(b-a)/2)-r2

            R1=R1+r1
            R2=R2+r2

            C5=(r2*((b-l)**3)/(6*l))-(r1*(b**3)/(3*l))-(r2*((b-l)**2)*b/(2*l))+(w1*((b-a)**3)*b/(6*l))-(w1*((b-a)**4)/(24*l))-((w2-w1)*((b-a)**4)*b/(120*l))
            C6=-C5*l
            C1=C5+(r2*((b-l)**2)/2)+(r1*(b**2)/2)-(w1*((b-a)**3)/6)-((w2-w1)*((b-a)**3)/24)
            
            x1_uvl,x2_uvl,x3_uvl=[],[],[]
            v1_uvl,v2_uvl,v3_uvl=[],[],[]
            m1_uvl,m2_uvl,m3_uvl=[],[],[]
            z1_uvl,z2_uvl,z3_uvl=[],[],[]
            q_uvl,r_uvl,s_uvl=Decimal(0),Decimal(a+Decimal(0.1)),Decimal(b+Decimal(0.1))
            c1=Decimal(a+Decimal(0.1))
            c2=Decimal(b+Decimal(0.1))
            while (q_uvl<=c1):
                x1_uvl.append(q_uvl)
                q_uvl=Decimal(q_uvl+Decimal(0.1))
            while (r_uvl>=c1 and r_uvl<=c2):
                x2_uvl.append(r_uvl)
                r_uvl=Decimal(r_uvl+Decimal(0.1))
            while (s_uvl>=c2 and s_uvl<=Decimal(l+Decimal(0.1))):
                x3_uvl.append(s_uvl)
                s_uvl=Decimal(s_uvl+Decimal(0.1))
            l1_uvl,l2_uvl,l3_uvl=len(x1_uvl),len(x2_uvl),len(x3_uvl)
            p1_uvl,p2_uvl,p3_uvl=0,0,0
            while (p1_uvl<=(l1_uvl-1)):
                v1_uvl.append(float(r1))
                m1_uvl.append(float(r1*x1_uvl[p1_uvl]))
                z1_uvl.append(float((-r1*(x1_uvl[p1_uvl]**3)/6)+(C1*x1_uvl[p1_uvl])))
                p1_uvl=(p1_uvl)+1
            while (p2_uvl<=(l2_uvl-1)):
                if(w1<=w2):
                    v2_uvl.append(float((r1)-(w1*(x2_uvl[p2_uvl]-a))-(Decimal(0.5)*(w2-w1)*((x2_uvl[p2_uvl]-a)**2)/(b-a))))
                    m2_uvl.append(float((r1*x2_uvl[p2_uvl])-(w1*((x2_uvl[p2_uvl]-a)**2)/2)-(Decimal(1/6)*(w2-w1)*((x2_uvl[p2_uvl]-a)**3)/(b-a))))
                    z2_uvl.append(float((-r1*(x2_uvl[p2_uvl]**3)/6)+(w1*((x2_uvl[p2_uvl]-a)**4)/24)+((w2-w1)*((x2_uvl[p2_uvl]-a)**5)/(120*(b-a)))+(C1*x2_uvl[p2_uvl])))
                else:
                    v2_uvl.append(float((r1)-(w2*(x2_uvl[p2_uvl]-a))-(Decimal(0.5)*(w2-w1)*((x2_uvl[p2_uvl]-a)**2)/(b-a))))
                    m2_uvl.append(float((r1*x2_uvl[p2_uvl])-(w2*((x2_uvl[p2_uvl]-a)**2)/2)-(Decimal(1/6)*(w2-w1)*((x2_uvl[p2_uvl]-a)**3)/(b-a))))
                    z2_uvl.append(float((-r1*(x2_uvl[p2_uvl]**3)/6)+(w1*((x2_uvl[p2_uvl]-a)**4)/24)+((w2-w1)*((x2_uvl[p2_uvl]-a)**5)/(120*(b-a)))+(C1*x2_uvl[p2_uvl])))
                p2_uvl=(p2_uvl)+1
            while (p3_uvl<=(l3_uvl-1)):
                v3_uvl.append(float(-r2))
                m3_uvl.append(float(r2*(l-x3_uvl[p3_uvl])))
                z3_uvl.append(float((r2*((x3_uvl[p3_uvl]-l)**3)/6)+(C5*x3_uvl[p3_uvl])+(C6)))
                p3_uvl=(p3_uvl)+1

            v_uvl=v1_uvl+v2_uvl+v3_uvl
            m_uvl=m1_uvl+m2_uvl+m3_uvl
            z_uvl=z1_uvl+z2_uvl+z3_uvl
            x=x1_uvl+x2_uvl+x3_uvl
            
            #canvas.itemconfigure(text100,text=len(x))
            
            V= [V[i] + v_uvl[i] for i in range(len(v_uvl))] 
            M= [M[i] + m_uvl[i] for i in range(len(m_uvl))]
            Z= [Z[i] + z_uvl[i] for i in range(len(z_uvl))]
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str4="R2 ="+str(round(R2,2))+" KN"
            canvas.itemconfigure(text4,text=str4)
        if((u.get())==2):
            r1=((w1+w2)*(b-a)/2)
            m11=((b-a)/6)*((w1*(2*a+b))+(w2*(a+2*b)))

            R1=R1+r1
            M1=M1+m11
            
            C5=(m11*b)-(r1*(b**2)/2)+(w1*((b-a)**3)/6)+((w2-w1)*((b-a)**3)/24)
            C6=(-m11*(b**2)/2)+(r1*(b**3)/3)+(w1*((b-a)**4)/24)-(w1*b*((b-a)**3)/6)+((w2-w1)*((b-a)**4)/120)-((w2-w1)*((b-a)**3)*b/24)

            x1_uvl,x2_uvl,x3_uvl=[],[],[]
            v1_uvl,v2_uvl,v3_uvl=[],[],[]
            m1_uvl,m2_uvl,m3_uvl=[],[],[]
            z1_uvl,z2_uvl,z3_uvl=[],[],[]
            q_uvl,r_uvl,s_uvl=Decimal(0),Decimal(a+Decimal(0.1)),Decimal(b+Decimal(0.1))
            c1=Decimal(a+Decimal(0.1))
            c2=Decimal(b+Decimal(0.1))
            while (q_uvl<=c1):
                x1_uvl.append(q_uvl)
                q_uvl=Decimal(q_uvl+Decimal(0.1))
            while (r_uvl>=c1 and r_uvl<=c2):
                x2_uvl.append(r_uvl)
                r_uvl=Decimal(r_uvl+Decimal(0.1))
            while (s_uvl>=c2 and s_uvl<=Decimal(l+Decimal(0.1))):
                x3_uvl.append(s_uvl)
                s_uvl=Decimal(s_uvl+Decimal(0.1))
            l1_uvl,l2_uvl,l3_uvl=len(x1_uvl),len(x2_uvl),len(x3_uvl)
            p1_uvl,p2_uvl,p3_uvl=0,0,0
            while (p1_uvl<=(l1_uvl-1)):
                v1_uvl.append(float(r1))
                m1_uvl.append(float(r1*x1_uvl[p1_uvl]))
                z1_uvl.append(float((m11*(x1_uvl[p1_uvl]**2)/2)-(r1*(x1_uvl[p1_uvl]**3)/6)))
                p1_uvl=(p1_uvl)+1
            while (p2_uvl<=(l2_uvl-1)):
                if(w1<=w2):
                    v2_uvl.append(float((r1)-(w1*(x2_uvl[p2_uvl]-a))-(Decimal(0.5)*(w2-w1)*((x2_uvl[p2_uvl]-a)**2)/(b-a))))
                    m2_uvl.append(float((r1*x2_uvl[p2_uvl])-(w1*((x2_uvl[p2_uvl]-a)**2)/2)-(Decimal(1/6)*(w2-w1)*((x2_uvl[p2_uvl]-a)**3)/(b-a))))
                    z2_uvl.append(float((m11*(x2_uvl[p2_uvl]**2)/2)-(r1*(x2_uvl[p2_uvl]**3)/6)+(w1*((x2_uvl[p2_uvl]-a)**4)/24)+((w2-w1)*((x2_uvl[p2_uvl]-a)**5)/(120*(b-a)))))
                else:
                    v2_uvl.append(float((r1)-(w2*(x2_uvl[p2_uvl]-a))-(Decimal(0.5)*(w2-w1)*((x2_uvl[p2_uvl]-a)**2)/(b-a))))
                    m2_uvl.append(float((r1*x2_uvl[p2_uvl])-(w2*((x2_uvl[p2_uvl]-a)**2)/2)-(Decimal(1/6)*(w2-w1)*((x2_uvl[p2_uvl]-a)**3)/(b-a))))
                    z2_uvl.append(float((m11*(x2_uvl[p2_uvl]**2)/2)-(r1*(x2_uvl[p2_uvl]**3)/6)+(w1*((x2_uvl[p2_uvl]-a)**4)/24)+((w2-w1)*((x2_uvl[p2_uvl]-a)**5)/(120*(b-a)))))
                p2_uvl=(p2_uvl)+1
            while (p3_uvl<=(l3_uvl-1)):
                v3_uvl.append(float(0))
                m3_uvl.append(float(0))
                z3_uvl.append(float((C5*x3_uvl[p3_uvl])+(C6)))
                p3_uvl=(p3_uvl)+1

            v_uvl=v1_uvl+v2_uvl+v3_uvl
            m_uvl=m1_uvl+m2_uvl+m3_uvl
            z_uvl=z1_uvl+z2_uvl+z3_uvl
            x=x1_uvl+x2_uvl+x3_uvl
            
            #canvas.itemconfigure(text100,text=len(x))
            
            V= [V[i] + v_uvl[i] for i in range(len(v_uvl))] 
            M= [M[i] + m_uvl[i] for i in range(len(m_uvl))]
            Z= [Z[i] + z_uvl[i] for i in range(len(z_uvl))]
        
            str3="R1 ="+str(round(R1,2))+" KN"
            canvas.itemconfigure(text3,text=str3)

            str4="M1 ="+str(round(M1,2))+" KN.m"
            canvas.itemconfigure(text5,text=str4)

            
        
        f11()
    def f11():
        window_uvl.destroy()
        
        
    btn6=Button(window_uvl,text="Add Load",fg="black",bg="red",width=20,command=f4,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn6.place(x=0,y=247)
    
    btn7=Button(window_uvl,text="Cancel",fg="black",bg="red",width=20,command=f11,borderwidth=2,relief="raised",font=("Arial Bold",20))
    btn7.place(x=310,y=247)

    btn8=Button(window_uvl,text="Exit",fg="black",bg="red",width=10,command=f11,borderwidth=2,relief="raised",font=("Arial Bold",15))
    btn8.place(x=510,y=0)

    window_uvl.mainloop()


def f2():
    m=u.get()
    x=var1.get()
    y=var2.get()
    
    global i

    Mi,Vi,Zi=0,0,0
    Mi=max(max(M),-min(M))
    Vi=max(max(V),-min(V))
    Zi=max(max(Z),-min(Z))
                        
        
    window4=Toplevel()
    window4.title("Analysis Result")
    #window4.geometry("1100x600")
    #window4.attributes('-fullscreen', True)
    window4.state('zoomed')
    window4.configure(bg="lavender")

    if (y==1):
        ISMB=["ISLB75","ISLB100","ISLB125","ISLB150","ISLB175","ISLB200","ISLB225","ISLB250","ISLB275","ISLB300","ISLB325","ISLB350","ISLB400","ISLB450","ISLB500","ISLB550","ISLB600"]
        w=[6.1,8.0,11.9,14.2,16.7,19.8,23.5,27.9,33.0,37.7,43.1,49.5,56.9,65.3,75.0,86.3,99.5]
        h=[75,100,125,150,175,200,225,250,275,300,325,350,400,450,500,550,600]
        Ze=[19.4,33.6,65.1,91.8,125.3,169.7,222.4,297.4,392.4,488.9,607.7,751.9,965.3,1223.8,1543.2,1933.2,2428.9]
        Zp=[22.35,38.89,73.93,104.50,143.30,184.34,254.72,338.69,443.09,554.32,687.76,851.11,1099.45,1401.35,1773.67,2228.16,2798.56]
        Tf=[5.0,6.4,6.5,6.8,6.9,7.3,8.6,8.2,8.8,9.4,9.8,11.4,12.5,13.4,14.1,15.0,15.5]
        Bf=[50,50,75,80,90,100,100,125,140,150,165,165,165,170,180,190,210]
        Tw=[3.7,4.0,4.4,4.8,5.1,5.4,5.8,6.1,6.4,6.7,7.0,7.4,8.0,8.6,9.2,9.9,10.5]
        Rf=[6.5,7.0,8.0,9.5,9.5,9.5,12.0,13.0,14.0,15.0,16.0,16.0,16.0,16.0,17.0,18.0,20.0]
        ry=[1.14,1.12,1.69,1.75,1.93,2.13,1.94,2.33,2.61,2.80,3.05,3.17,3.15,3.20,3.34,3.48,3.79]
        Iy=[1.0,12.7,43.4,55.2,79.6,115.4,112.7,193.4,287.0,376.2,510.8,631.9,716.4,853.0,1063.9,1335.1,1821.9]
        Ix=[72.7,168.0,406.8,688.2,1096.2,1696.6,2501.9,3717.8,5375.3,7332.9,9874.6,13158.3,19306.3,27536.1,38579.0,53161.6,72867.6]
        ntimes=len(ISMB)
    elif (y==2):
        ISMB=["ISMB100","ISMB125","ISMB150","ISMB175","ISMB200","ISMB225","ISMB250","ISMB300","ISMB350","ISMB400","ISMB450","ISMB500","ISMB550","ISMB600"]
        w=[11.5,13.0,14.9,19.3,35.4,31.2,37.3,44.2,52.4,61.6,72.4,86.9,103.7,122.6]
        h=[100,125,150,175,200,225,250,300,350,400,450,500,550,600]
        Ze=[51.5,71.8,96.9,145.4,223.5,305.9,410.5,573.6,778.9,1022.9,1350.7,1808.7,2359.8,3060.4]
        Zp=[41.68,81.85,110.48,166.08,253.86,348.27,465.71,651.74,889.57,1176.18,1533.36,2074.67,2711.98,3510.63]
        Tf=[7.2,7.6,7.6,8.6,10.8,11.8,12.5,12.4,14.2,16.0,17.4,17.2,19.3,20.8]
        Bf=[75,75,80,90,100,110,125,140,140,140,150,180,190,210]
        Tw=[4.0,4.4,4.8,5.5,5.7,6.5,6.9,7.5,8.1,8.9,9.4,10.2,11.2,12.0]
        Rf=[9,9,9,10,11,12,13,14,14,14,15,17,18,20]
        ry=[1.67,1.62,1.66,1.86,2.15,2.34,2.65,2.84,2.84,2.82,3.01,3.52,3.73,4.12]
        Iy=[40.8,43.7,52.6,85.0,150.0,218.3,334.5,453.9,537.7,622.1,834.0,1369.8,1833.8,2651.0]
        Ix=[257.5,449.0,726.4,1272.0,2235.4,3441.8,5131.6,8603.6,13630.3,20458.4,30390.8,45218.3,64893.6,91813.0]
        ntimes=len(ISMB)
    elif (y==3):
        ISMB=["ISWB150","ISWB175","ISWB200","ISWB225","ISWB250","ISWB300","ISWB350","ISWB400","ISWB450","ISWB500","ISWB550","ISWB600","ISWB600"]
        w=[17.0,22.1,28.8,33.9,40.9,48.1,56.9,66.7,79.4,95.2,112.5,133.7,145.1]
        h=[150,175,200,225,250,300,350,400,450,500,550,600,600]
        Ze=[111.9,172.5,262.5,348.5,475.4,654.8,887.0,1171.3,1558.1,2091.6,2723.9,3540.0,3854.2]
        Zp=[126.86,194.20,293.99,389.93,527.57,731.21,995.49,1290.19,1760.59,2351.35,3066.29,3986.66,4341.63]
        Tf=[7.0,7.4,9.0,9.9,9.0,10.0,11.4,13.0,15.4,14.7,17.6,21.3,23.6]
        Bf=[100,125,140,150,200,200,200,200,200,250,250,250,250]
        Tw=[5.4,5.8,6.1,6.4,6.7,7.4,8.0,8.6,9.2,9.9,10.5,11.2,11.8]
        Rf=[8.0,8.0,9.0,9.0,10.0,11.0,12,13,14,15,16,17,18]
        ry=[2.09,2.59,2.99,3.22,4.06,4.02,4.03,4.04,4.11,4.96,5.11,5.25,5.35]
        Iy=[94.8,188.6,328.8,448.6,857.5,990.1,1175.9,1388.0,1706.7,2987.8,3740.6,4702.5,5298.3]
        Ix=[839.1,1509.4,2624.5,3920.5,5943.1,9821.6,15521.7,23426.7,35057.6,52290.9,74906.1,106198.5,115626.6]
        ntimes=len(ISMB)
    elif (y==4):
        ISMB=["ISJB150","ISJB175","ISJB200","ISJB225","ISLB175","ISMB175","ISLB200","ISLB225","ISLB250","ISLB275","ISLB300","ISMB300","ISLB325","ISLB400","ISMB400","ISLB450","ISMB450","ISLB500","ISLB550","ISWB500","ISLB600","ISWB550","ISMB600","ISWB600","ISWB600"]
        w=[7.1,8.1,9.9,12.8,16.7,19.3,19.8,23.5,27.9,33.0,37.7,44.2,43.1,56.9,61.5,65.3,72.4,75.0,86.3,95.2,99.5,112.5,122.6,133.7,145.1]
        h=[150,175,200,225,175,175,200,225,250,275,300,300,325,400,400,450,450,500,550,500,600,550,600,600,600]
        Ze=[42.9,54.8,78.1,116.3,125.3,145.4,169.7,222.4,297.4,392.4,488.9,573.6,607.7,965.3,1020.0,1223.8,1350.7,1558.1,1993.2,2091.6,2428.9,2723.9,3060.4,3540.0,3854.2]
        Zp=[49.57,64.22,90.89,134.15,143.30,166.08,184.34,254.72,338.69,443.09,554.32,651.74,687.76,1099.45,1176.18,1401.35,1533.36,1773.67,2228.16,2351.35,2798.56,3066.29,3510.63,3986.66,4341.63]
        Tf=[4.6,4.6,5.0,5.0,6.9,8.6,7.3,8.6,8.2,8.8,9.4,12.4,9.8,12.5,16.0,13.4,17.4,14.1,15.0,14.7,15.5,17.6,20.8,21.3,23.6]
        Bf=[50,50,60,80,90,90,100,100,125,140,150,140,165,165,140,170,150,180,190,250,210,250,210,250,250]
        Tw=[3.0,3.0,3.4,3.7,5.1,5.5,5.4,5.8,6.1,6.4,6.7,7.5,7.0,8,8.9,8.6,9.4,9.2,9.9,9.9,10.5,10.5,12,11.2,11.8]
        Rf=[5.0,5.0,5.0,6.5,9.5,10.0,9.5,12.0,13.0,14.0,15.0,14.0,16.0,16.0,14.0,16.0,15.0,17.0,18.0,15.0,20,16,20,17.0,18.0]
        ry=[1.01,0.97,1.17,1.58,1.93,1.86,2.13,1.94,2.33,2.61,2.80,2.84,3.05,3.15,2.84,3.20,3.01,3.34,3.48,4.96,3.79,5.11,4.12,5.25,5.35]
        Iy=[9.2,9.7,17.3,40.5,79.6,85.0,115.4,112.7,193.4,287.0,376.2,453.9,510.8,716.4,622.1,853.0,834.0,1063.9,1335.1,2987.8,1821.9,3740.6,2651.0,4702.5,5298.3]
        Ix=[322.1,479.3,780.7,1308.5,1096.2,1272.0,1696.6,2501.9,3717.8,5375.3,7332.9,8603.6,9874.6,19306.3,20458.4,27536.1,30390.8,38579.0,53161.6,52290.9,72867.6,74906.1,91813.0,106198.5,115626.6]
        ntimes=len(ISMB)
            
    j=int(0)
    while (j<=(ntimes-1)):
        h[j]=h[j]/1000
        Ze[j]=Ze[j]/1000000
        Zp[j]=Zp[j]/1000000
        Tf[j]=Tf[j]/1000
        Bf[j]=Bf[j]/1000
        Tw[j]=Tw[j]/1000
        Rf[j]=Rf[j]/1000
        ry[j]=ry[j]/100
        Iy[j]=Iy[j]/(10**(8))
        Ix[j]=Ix[j]/(10**(8))
        j=j+1

    Fy=250000
    E=2*(10**8)
    Mew=0.3
    G=E/(2*(1+Mew))
    Gamma=1.1
    result=int(0)
    Za=0
    if(m==1):
        Za=l*1000/300
    else:
        Za=l*1000/150

                        
    if (x==1):
        while (i<=(ntimes-1)):
            D=h[i]-(2*(Tf[i]+Rf[i]))                        
            X1=(Bf[i])/(2*(Tf[i]))
            X2=D/Tw[i]
            if (X1<=10.5) and (X2<=105):
                Betab=1
            else:
                Betab=Ze[i]/Zp[i]
            Vd=(Fy*Tw[i]*h[i]/Gamma)/(1.732)
            X3=0.6*Vd
            if (Vi<=Vd):
                if (Vi<=X3):
                    Md=(Betab*Zp[i]*Fy)/Gamma;
                    if (Mi<=Md):
                        b=0.1
                        Area=(b+(h[i]/2))*Tw[i]
                        r=(Tw[i]/3.4641)
                        Fcc=(((math.pi)**2)*2*(10**8))/((0.7*D/r)**2)
                        Lambda=math.sqrt(Fy/Fcc)
                        Phi=0.5*(1+(0.49*(Lambda-0.2))+(Lambda**2))
                        Fcd=(Fy/Gamma)/(Phi+(((Phi**2)-(Lambda**2))**0.5))
                        Fwb=Fcd*Area
                        if (Vi<=Fwb):
                            n2=2.5*(Rf[i]+Tf[i])
                            Fwc=(b+n2)*(Tw[i])*(Fy/Gamma)
                            if (Vi<=Fwc):
                                Zd=(Zi*1000)/(E*Ix[i])
                                if (Zd<=Za):
                                    result=int(1)
                                    break
                            
                                        
                else:
                    if (Betab==1):
                        Md=(Betab*Zp[i]*Fy)/Gamma
                        Beta=((2*(Vi/Vd))-1)**2
                        Mfd=(h[i]*h[i]*Tw[i]/4)*Fy
                        Mdv=Md-(Beta*(Md-Mfd))
                        if (Mi<=Mdv):
                            b=0.1
                            Area=(b+(h[i]/2))*Tw[i]
                            r=(Tw[i]/3.4641)
                            Fcc=(((math.pi)**2)*2*(10**8))/((0.7*D/r)**2)
                            Lambda=math.sqrt(Fy/Fcc)
                            Phi=0.5*(1+(0.49*(Lambda-0.2))+(Lambda**2))
                            Fcd=(Fy/Gamma)/(Phi+(((Phi**2)-(Lambda**2))**0.5))
                            Fwb=Fcd*Area
                            if (Vi<=Fwb):
                                n2=2.5*(Rf[i]+Tf[i])
                                Fwc=(b+n2)*(Tw[i])*(Fy/Gamma)
                                if (Vi<=Fwc):
                                    Zd=(Zi*1000)/(E*Ix[i])
                                    if (Zd<=Za):
                                        result=int(1)
                                        break
                                    
                    else:
                        Mdv=Ze[i]*Fy/Gamma
                        if (Mi<=Mdv):
                            b=0.1
                            Area=(b+(h[i]/2))*Tw[i]
                            r=(Tw[i]/3.4641)
                            Fcc=(((math.pi)**2)*2*(10**8))/((0.7*D/r)**2)
                            Lambda=math.sqrt(Fy/Fcc)
                            Phi=0.5*(1+(0.49*(Lambda-0.2))+(Lambda**2))
                            Fcd=(Fy/Gamma)/(Phi+(((Phi**2)-(Lambda**2))**0.5))
                            Fwb=Fcd*Area
                            if (Vi<=Fwb):
                                n2=2.5*(Rf[i]+Tf[i])
                                Fwc=(b+n2)*(Tw[i])*(Fy/Gamma)
                                if (Vi<=Fwc):
                                    Zd=(Zi*1000)/(E*Ix[i])
                                    if (Zd<=Za):
                                        result=int(1)
                                        break
                                    
            i=i+1
                        
    elif (x==2):
        while (i<=(ntimes-1)):
            Hf=h[i]-Tf[i]
            D=h[i]-(2*(Tf[i]+Rf[i]))                        
            X1=(Bf[i])/(2*(Tf[i]))
            X2=D/Tw[i]
            if (X1<=10.5) and (X2<=105):
                Betab=1
            else:
                Betab=Ze[i]/Zp[i]
            t1=2*Bf[i]*(Tf[i]**3)/3;
            t2=Hf*(Tw[i]**3)/3;
            It=t1+t2;
            Betaf=0.5
            Iw=(1-Betaf)*Betaf*Iy[i]*(Hf**2)
            y1=((math.pi)**2)*E*Iy[i]/(float(l)**2)
            y2=G*It
            y3=((math.pi)**2)*E*Iw/(float(l)**2)
            Mcr=math.sqrt(y1*(y2+y3))
            LambdaLT=math.sqrt(Betab*Zp[i]*Fy/Mcr)
            AlphaLT=0.21
            PhiLT=(0.5)*(1+(AlphaLT*(LambdaLT-0.2))+((LambdaLT)**2))
            XLT=1/(PhiLT+(((PhiLT**2)-(LambdaLT**2))**0.5))
            Fbd=XLT*(Fy)/Gamma
            Md=Betab*Zp[i]*Fbd
            if (Mi<=Md):
                Vd=(Fy*Tw[i]*h[i]/Gamma)/(math.sqrt(3))
                if (Vi<=Vd):
                    b=0.1
                    Area=(b+(h[i]/2))*Tw[i]
                    r=(Tw[i]/3.4641)
                    Fcc=(((math.pi)**2)*2*(10**8))/((0.7*D/r)**2)
                    Lambda=math.sqrt(Fy/Fcc)
                    Phi=0.5*(1+(0.49*(Lambda-0.2))+(Lambda**2))
                    Fcd=(Fy/Gamma)/(Phi+(((Phi**2)-(Lambda**2))**0.5))
                    Fwb=Fcd*Area
                    if (Vi<=Fwb):
                        n2=2.5*(Rf[i]+Tf[i])
                        Fwc=(b+n2)*(Tw[i])*(Fy/Gamma)
                        if (Vi<=Fwc):
                            Zd=(Zi*1000)/(E*Ix[i])
                            if (Zd<=Za):
                                result=int(1)
                                break

            i=i+1
                                    

    if (result==1):
        h[i]=h[i]*1000
        Ze[i]=Ze[i]*1000000
        Zp[i]=Zp[i]*1000000
        Tf[i]=Tf[i]*1000
        Bf[i]=Bf[i]*1000
        Tw[i]=Tw[i]*1000
        Rf[i]=Rf[i]*1000
        Iy[i]=Iy[i]*(10**(8))
        Ix[i]=Ix[i]*(10**(8))
                
                
        canvas6=Canvas(window4,width=550,height=650,bg="lavender",borderwidth=2,relief="solid")
        canvas6.place(x=5,y=5)
        label8=Label(window4,text="SELECTED SECTION",fg="blue",font=("Verdana Bold",30),bg="lavender")
        label8.place(x=20,y=9)
        label9=Label(window4,text="Name of Section=",fg="black",font=("Sitka Small Bold",20),bg="lavender")
        label9.place(x=10,y=60)
        label10=Label(window4,text=ISMB[i],fg="black",bg="cyan",width=10,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label10.place(x=330,y=65)
        label11=Label(window4,text="Depth of Section(h)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label11.place(x=10,y=160)
        label12=Label(window4,text=round(h[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label12.place(x=370,y=165)
        label13=Label(window4,text="Section Modulus(Ze)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label13.place(x=10,y=210)
        label14=Label(window4,text=round(Ze[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label14.place(x=370,y=215)
        label15=Label(window4,text="Plastic Modulus(Zp)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label15.place(x=10,y=260)
        label16=Label(window4,text=round(Zp[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label16.place(x=370,y=265)
        label17=Label(window4,text="Thickness of Flange(Tf)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label17.place(x=10,y=310)
        label18=Label(window4,text=round(Tf[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label18.place(x=370,y=315)
        label19=Label(window4,text="Width of Flange(Bf)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label19.place(x=10,y=360)
        label20=Label(window4,text=round(Bf[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label20.place(x=370,y=365)
        label21=Label(window4,text="Thickness of Web(Tw)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label21.place(x=10,y=410)
        label21=Label(window4,text=round(Tw[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label21.place(x=370,y=415)
        label22=Label(window4,text="Root Radius(r1)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label22.place(x=10,y=460)
        label23=Label(window4,text=round(Rf[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label23.place(x=370,y=465)
        
        label022=Label(window4,text="Weight per metre(w)=",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label022.place(x=10,y=110)
        label023=Label(window4,text=round(w[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label023.place(x=370,y=115)

        label_22=Label(window4,text="KN/m",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_22.place(x=484,y=120)
        
        label_23=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_23.place(x=489,y=170)

        label_231=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_231.place(x=489,y=220)

        label_2311=Label(window4,text="3",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_2311.place(x=525,y=216)

        label_232=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_232.place(x=489,y=270)

        label_2322=Label(window4,text="3",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_2322.place(x=525,y=266)

        label_233=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_233.place(x=489,y=320)

        label_234=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_234.place(x=489,y=370)

        label_235=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_235.place(x=489,y=420)

        label_236=Label(window4,text="mm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_236.place(x=489,y=470)

        label_237=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_237.place(x=489,y=520)

        label_2377=Label(window4,text="4",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_2377.place(x=525,y=516)

        label_238=Label(window4,text="cm",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_238.place(x=489,y=570)

        label_2388=Label(window4,text="4",fg="black",bg="lavender",font=("Verdana Bold",15))
        label_2388.place(x=525,y=566)
        
        label122=Label(window4,text="Moment of Inertia(Ixx) = ",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label122.place(x=10,y=510)
        label123=Label(window4,text=round(Ix[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label123.place(x=370,y=515)
        label222=Label(window4,text="Moment of Inertia(Iyy) = ",fg="black",bg="lavender",font=("Sitka Small Bold",20))
        label222.place(x=10,y=560)
        label223=Label(window4,text=round(Iy[i],2),fg="black",bg="cyan",width=6,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label223.place(x=370,y=565)
        
        if(x==1):
            canvas7=Canvas(window4,width=780,height=650,bg="greenyellow",borderwidth=2,relief="solid")
            canvas7.place(x=570,y=5)
        if(x==2):
            canvas7=Canvas(window4,width=780,height=670,bg="greenyellow",borderwidth=2,relief="solid")
            canvas7.place(x=570,y=5)
        label25=Label(window4,text="Design Shear Force(V) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label25.place(x=580,y=60)
        label24=Label(window4,text="SECTION SUITABILITY CHECK",fg="blue",bg="greenyellow",font=("Verdana Bold",30))
        label24.place(x=580,y=9)
        label26=Label(window4,text=round(Vi,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label26.place(x=1130,y=60)
        label27=Label(window4,text="Shear Capacity of Section(Vd) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label27.place(x=580,y=100)
        label28=Label(window4,text=round(Vd,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label28.place(x=1130,y=100)
        label35=Label(window4,text="V < Vd i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",20),borderwidth=2,relief="solid")
        label35.place(x=600,y=140)
        label29=Label(window4,text="Design Bending Moment(M) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label29.place(x=580,y=190)
        label30=Label(window4,text=round(Mi,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label30.place(x=1130,y=190)
        label31=Label(window4,text="Moment Capacity of Section(Md) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label31.place(x=580,y=230)
        label32=Label(window4,text=round(Md,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label32.place(x=1130,y=230)
        label36=Label(window4,text="M < Md i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",20),borderwidth=2,relief="solid")
        label36.place(x=600,y=270)
        label37=Label(window4,text="Web Buckling Resistance(Fwb) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label37.place(x=580,y=320)
        label38=Label(window4,text=round(Fwb,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label38.place(x=1130,y=320)
        label41=Label(window4,text="V < Fwb i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",20),borderwidth=2,relief="solid")
        label41.place(x=600,y=360)
        label39=Label(window4,text="Web Crippling Resistance(Fwc) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label39.place(x=580,y=410)
        label40=Label(window4,text=round(Fwc,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label40.place(x=1130,y=410)
        label42=Label(window4,text="V < Fwc i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",20),borderwidth=2,relief="solid")
        label42.place(x=600,y=450)

        label43=Label(window4,text="Max. Deflection(mm) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
        label43.place(x=580,y=500)
        label44=Label(window4,text=round(Zd,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label44.place(x=1130,y=500)
        if(m==1):
            label45=Label(window4,text="L/300(Allowable Deflection) (mm) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
            label45.place(x=580,y=540)
        else:
            label45=Label(window4,text="L/150(Allowable Deflection) (mm) = ",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
            label45.place(x=580,y=540)
        label46=Label(window4,text=round(Za,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
        label46.place(x=1130,y=540)
        label47=Label(window4,text="Max. Deflection < Allowable Deflection i.e (SAFE)",fg="black",bg="red",font=("Sitka Small Bold",20),borderwidth=2,relief="solid")
        label47.place(x=580,y=580)

        label_35=Label(window4,text=" KN ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_35.place(x=1290,y=65)

        label_36=Label(window4,text=" KN ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_36.place(x=1290,y=105)

        label_37=Label(window4,text=" KN.m ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_37.place(x=1270,y=195)

        label_38=Label(window4,text=" KN.m ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_38.place(x=1270,y=235)

        label_39=Label(window4,text=" KN ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_39.place(x=1290,y=325)

        label_40=Label(window4,text=" KN ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_40.place(x=1290,y=415)

        label_41=Label(window4,text=" mm ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_41.place(x=1290,y=505)

        label_42=Label(window4,text=" mm ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
        label_42.place(x=1290,y=545)

        label90=Label(window4,text="Do you want to get the next best design.....Click on NEXT Button",fg="black",font=("Sitka Small Bold",14),bg="green")
        label90.place(x=300,y=655)
        
            
        if (x==2):
            label33=Label(window4,text="Torsional Buckling Moment(Mcr)=",fg="black",bg="greenyellow",font=("Sitka Small Bold",20))
            label33.place(x=580,y=630)
            label34=Label(window4,text=round(Mcr,2),fg="black",bg="yellow",width=7,font=("Verdana Bold",20),borderwidth=2,relief="solid")
            label34.place(x=1130,y=630)
            label_34=Label(window4,text=" KN/m ",fg="black",bg="greenyellow",font=("Verdana Bold",15))
            label_34.place(x=1270,y=635)
        def next_page():
            global i
            i=i+1
            window4.destroy()
            f2()
        def previous_page():
            global i
            i=i-1
            window4.destroy()
            f2()
        def exit_window4():
            window4.destroy()
            global i
            i=0
                
                
            
        
        btn4=Button(window4,text="NEXT",fg="black",bg="red",width=9,command=next_page,borderwidth=2,relief="raised",font=("Verdana Bold",15))
        btn4.place(x=1250,y=650)

        previousbtn=Button(window4,text="PREVIOUS",fg="black",bg="red",width=10,command=previous_page,borderwidth=2,relief="raised",font=("Verdana Bold",15))
        previousbtn.place(x=0,y=650)

        exitbtn4=Button(window4,text="EXIT",fg="black",bg="red",width=9,command=exit_window4,borderwidth=2,relief="raised",font=("Verdana Bold",15))
        exitbtn4.place(x=1250,y=0)
                    

        window4.mainloop()
            
    elif (result==0) and (i>ntimes-1):
        label8=Label(window4,text="Warning",fg="red",font=("Arial Bold",30),bg="lavender")
        label8.place(x=20,y=20)

def exit_window():
    window.destroy()

def shear_force():
    plt.plot(x,V,color="red",label="Shear Force")
    plt.plot([0,0],[0,V[0]],color="red")
    plt.plot([l,l],[V[-1],0],color="red")
    plt.plot([0,l],[0,0],color="black",label="Beam")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Shear Force Diagram")
    plt.legend()
    plt.show()

def bending_moment():
    plt.plot(x,M,color="red",label="Bending Moment")
    plt.plot([0,0],[0,M[0]],color="red")
    plt.plot([l,l],[M[-1],0],color="red")
    plt.plot([0,l],[0,0],color="black",label="Beam")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Bending Moment Diagram")
    plt.legend()
    plt.show()

def deflected_diagram():
    Z1= [(-1*Z[i])/(2*10**4) for i in range(len(Z))]
    plt.plot(x,Z1,color="red",label="Deflected Beam")
    plt.plot([0,l],[0,0],color="black",label="Beam")
    #plt.axis('equal')
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Deflected Beam Diagram")
    plt.legend()
    plt.show()

def reset_all():
    canvas.delete("all")
    reset_life()
    global V,M
    V.clear()
    M.clear()
    Z.clear()

    
btn1=Button(window,text="RESULTS",fg="black",bg="red",width=13,command=f2,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn1.place(x=1187,y=650)

exitbtn1=Button(window,text="EXIT",fg="black",bg="red",width=9,command=exit_window,borderwidth=2,relief="raised",font=("Verdana Bold",15))
exitbtn1.place(x=1250,y=0)

resetbtn1=Button(window,text="RESET",fg="black",bg="red",width=9,command=reset_all,borderwidth=2,relief="raised",font=("Verdana Bold",15))
resetbtn1.place(x=1124,y=0)

btn_sf=Button(window,text="SFD",fg="black",bg="deepskyblue",width=10,command=shear_force,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn_sf.place(x=915,y=650)

btn_bm=Button(window,text="BMD",fg="black",bg="deepskyblue",width=10,command=bending_moment,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn_bm.place(x=1046,y=650)

btn_deflection=Button(window,text="DEFLECTED SHAPE",fg="black",bg="deepskyblue",width=20,command=deflected_diagram,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn_deflection.place(x=915,y=612)

btn1_n=Button(window,text="Add Beam",fg="black",bg="red",width=10,command=f1,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn1_n.place(x=290,y=204)

btn5=Button(window,text="Add Point Load",fg="black",bg="red",width=15,command=f3,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn5.place(x=290,y=244)

btn_udl=Button(window,text="Add Uniformly Distributed Load",fg="black",bg="red",width=27,command=com_udl,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn_udl.place(x=290,y=284)

btn_uvl=Button(window,text="Add Uniformly Varying Load",fg="black",bg="red",width=27,command=com_uvl,borderwidth=2,relief="raised",font=("Verdana Bold",15))
btn_uvl.place(x=290,y=324)

window.mainloop()
