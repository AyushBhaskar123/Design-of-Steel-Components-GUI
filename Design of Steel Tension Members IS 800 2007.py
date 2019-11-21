from tkinter import*
import math

window=Tk()
window.title("Design of Steel Tension Member")
window.state('zoomed')
window.configure(bg="lightblue1")

heading_label=Label(window,text="TENSION  MEMBER  DESIGN",fg="black",bg="lightblue1",font=("Sitka Small Bold",35))
heading_label.place(x=60,y=0)

canvas=Canvas(window,width=900,height=280,bg="white",borderwidth=2,relief="solid")
canvas.place(x=5,y=390)

u=IntVar()
v=IntVar()

Tdg,Tdn,Tdb1,Tdb2=[],[],[],[]

u.set(1)
v.set(1)

i=int(0)

canvas1=Canvas(window,width=590,height=300,bg="lavender",borderwidth=2,relief="solid")
canvas1.place(x=5,y=80)

canvas2=Canvas(window,width=390,height=300,bg="white",borderwidth=2,relief="solid")
canvas2.place(x=605,y=80)

canvas3=Canvas(window,width=350,height=300,bg="lemonchiffon",borderwidth=2,relief="solid")
canvas3.place(x=1005,y=80)

inputdetails_label=Label(window,text="INPUT DETAILS",fg="blue",bg="lavender",font=("Sitka Small Bold",20))
inputdetails_label.place(x=150,y=84)

label1=Label(window,text="Tension Force(T) = ",fg="black",font=("Sitka Small Bold",18),bg="lavender")
label1.place(x=10,y=130)

entry1=Entry(window,width=9,borderwidth=2,relief="solid",font=("Times New Roman Bold",20),justify="center")
entry1.place(x=420,y=140)

label2=Label(window,text="Fy (N/mm2) = ",fg="black",font=("Sitka Small Bold",18),bg="lavender")
label2.place(x=10,y=180)

entry2=Entry(window,width=9,borderwidth=2,relief="solid",font=("Times New Roman Bold",20),justify="center")
entry2.place(x=420,y=190)
entry2.insert(0,250)

label3=Label(window,text="Fu (N/mm2) = ",fg="black",font=("Sitka Small Bold",18),bg="lavender")
label3.place(x=10,y=230)

entry3=Entry(window,width=9,borderwidth=2,relief="solid",font=("Times New Roman Bold",20),justify="center")
entry3.place(x=420,y=240)
entry3.insert(0,410)

label4=Label(window,text="Bolt Diameter(mm) = ",fg="black",font=("Sitka Small Bold",18),bg="lavender")
label4.place(x=10,y=280)

entry4=Entry(window,width=9,borderwidth=2,relief="solid",font=("Times New Roman Bold",20),justify="center")
entry4.place(x=420,y=290)
entry4.insert(0,20)

GammaMb=float(1.25)
Gamma=float(1.1)

Fub=float(0)
Fuy=float(0)

def f2():

    canvas.delete("all")
    
    points1=[300,50,600,100]
    line1=canvas.create_line(points1,width=2)

    points2=[300,250,600,200]
    line2=canvas.create_line(points2,width=2)

    points3=[300,50,300,250]
    line3=canvas.create_line(points3,width=2)

    points4=[400,100,800,100]
    line4=canvas.create_line(points4,width=3)

    points5=[400,200,800,200]
    line5=canvas.create_line(points5,width=3)

    points6=[400,100,400,200]
    line6=canvas.create_line(points6,width=3)

    points7=[800,100,800,200]
    line7=canvas.create_line(points7,width=3)

    points8=[600,100,600,200]
    line8=canvas.create_line(points8,dash=(20,),width=2)

    points9=[400,120,800,120]
    line9=canvas.create_line(points9,width=3)

    points10=[425,140,450,165]
    circle1=canvas.create_oval(points10,dash=(20,),outline="black",fill="white",width=2)

    points11=[475,140,500,165]
    circle2=canvas.create_oval(points11,dash=(20,),outline="black",fill="white",width=2)

    points12=[525,140,550,165]
    circle3=canvas.create_oval(points12,dash=(20,),outline="black",fill="white",width=2)

    points13=[350,150,250,150]
    line10=canvas.create_line(points13,width=3,fill="red",arrow=LAST)

    points14=[750,150,850,150]
    line11=canvas.create_line(points14,width=3,fill="red",arrow=LAST)
    
    points15=[230,150]
    text1=canvas.create_text(points15,fill="red",font="Times 35",text="T")

    points16=[880,150]
    text2=canvas.create_text(points16,fill="red",font="Times 35",text="T")

    points18=[50,20,35,250]
    rectangle1=canvas.create_rectangle(points18,width=2)

    points19=[50,100,200,100]
    line13=canvas.create_line(points19,width=2)

    points20=[80,120,190,120]
    line14=canvas.create_line(points20,width=2)

    points21=[70,130,70,190]
    line15=canvas.create_line(points21,width=2)

    points22=[200,100,190,120]
    line16=canvas.create_line(points22,width=2)

    points23=[80,120,70,130]
    line17=canvas.create_line(points23,width=2)

    points24=[50,200,70,190]
    line18=canvas.create_line(points24,width=2)


f2()

def f3():
    points17=[400,180,800,180]
    line12=canvas.create_line(points17,width=3)


def f1():

    x=u.get()
    y=v.get()
    
    T=float(entry1.get())
    Fy=float(entry2.get())
    Fu=float(entry3.get())
    d=float(entry4.get())
    d0=float(d+2)

    name1,thick1,a1,b1,Ag1,w1,Treal1=[],[],[],[],[],[],[]
    Tdg1,Tdn1,Tdb11,Tdb21=[],[],[],[]
    Anc1,Ago1,Avn1,Avg1,Atn1,Atg1=[],[],[],[],[],[]
    name2,thick2,a2,b2,Ag2,w2,Treal2=[],[],[],[],[],[],[]
    Tdg2,Tdn2,Tdb12,Tdb22=[],[],[],[]
    Anc2,Ago2,Avn2,Avg2,Atn2,Atg2=[],[],[],[],[],[]

    if(y==1):
        Fub=float(400)
        Fuy=float(400*0.6)
    elif(y==2):
        Fub=float(800)
        Fuy=float(800*0.8)
    elif(y==3):
        Fub=float(1000)
        Fuy=float(1000*0.9)
    elif(y==4):
        Fub=float(1200)
        Fuy=float(1200*0.9)

    global i,Tdg,Tdn,Tdb1,Tdb2
    result=int(0)
    i=int(0)

    if(x==1):
        name=["ISA 2020","ISA 2020","ISA 2525","ISA 2525","ISA 2525","ISA 3030","ISA 3030","ISA 3030","ISA 3535","ISA 3535","ISA 3535","ISA 3535","ISA 4040","ISA 4040","ISA 4040","ISA 4040","ISA 4545","ISA 4545","ISA 4545","ISA 4545","ISA 5050","ISA 5050","ISA 5050","ISA 5050","ISA 5555","ISA 5555","ISA 5555","ISA 5555","ISA 6060","ISA 6060","ISA 6060","ISA 6060","ISA 6565","ISA 6565","ISA 6565","ISA 6565","ISA 7070","ISA 7070","ISA 7070","ISA 7070","ISA 7575","ISA 7575","ISA 7575","ISA 7575","ISA 8080","ISA 8080","ISA 8080","ISA 8080","ISA 9090","ISA 9090","ISA 9090","ISA 9090","ISA 100100","ISA 100100","ISA 100100","ISA 100100","ISA 110110","ISA 110110","ISA 110110","ISA 110110","ISA 130130","ISA 130130","ISA 130130","ISA 130130","ISA 150150","ISA 150150","ISA 150150","ISA 150150","ISA 200200","ISA 200200","ISA 200200","ISA 200200"]
        t=[3,4,3,4,5,3,4,5,3,4,5,6,3,4,5,6,3,4,5,6,3,4,5,6,5,6,8,10,5,6,8,10,5,6,8,10,5,6,8,10,5,6,8,10,6,8,10,12,6,8,10,12,6,8,10,12,8,10,12,15,8,10,12,15,10,12,15,18,12,15,18,25]
        a=[20,20,25,25,25,30,30,30,35,35,35,35,40,40,40,40,45,45,45,45,50,50,50,50,55,55,55,55,60,60,60,60,65,65,65,65,70,70,70,70,75,75,75,75,80,80,80,80,90,90,90,90,100,100,100,100,110,110,110,110,130,130,130,130,150,150,150,150,200,200,200,200]
        b=[20,20,25,25,25,30,30,30,35,35,35,35,40,40,40,40,45,45,45,45,50,50,50,50,55,55,55,55,60,60,60,60,65,65,65,65,70,70,70,70,75,75,75,75,80,80,80,80,90,90,90,90,100,100,100,100,110,110,110,110,130,130,130,130,150,150,150,150,200,200,200,200]
        Ag=[1.12,1.45,1.41,1.84,2.25,1.73,2.26,2.77,2.03,2.66,3.27,3.86,2.34,3.07,3.78,4.47,2.64,3.47,4.28,5.07,2.95,3.88,4.79,5.68,5.27,6.26,8.18,10.02,5.75,6.84,8.96,11.00,6.25,7.44,9.76,12.00,6.77,8.06,10.58,13.02,7.27,8.66,11.38,14.02,9.29,12.21,15.05,17.81,10.47,13.79,17.03,20.19,11.67,15.39,19.03,22.59,17.02,21.06,25.02,30.81,20.22,25.06,29.82,36.81,29.03,34.59,42.78,50.79,46.61,57.80,68.81,93.80]
        w=[0.9,1.1,1.1,1.4,1.8,1.4,1.8,2.2,1.6,2.1,2.6,3.0,1.8,2.4,3.0,3.5,2.1,2.7,3.4,4.0,2.3,3.0,3.8,4.5,4.1,4.9,6.4,7.9,4.5,5.4,7.0,8.6,4.9,5.8,7.7,9.4,5.3,6.3,8.3,10.2,5.7,6.8,8.9,11.0,7.3,9.6,11.8,14.0,8.2,10.8,13.4,15.8,9.2,12.1,14.9,17.7,13.4,16.5,19.6,24.2,15.9,19.7,23.4,28.9,22.8,27.2,33.6,39.9,36.6,45.4,54.0,73.6]
        ntimes=len(name)
    if(x==2):
        name=["ISA 3020","ISA 3020","ISA 3020","ISA 4025","ISA 4025","ISA 4025","ISA 4025","ISA 4530","ISA 4530","ISA 4530","ISA 4530","ISA 5030","ISA 5030","ISA 5030","ISA 5030","ISA 6040","ISA 6040","ISA 6040","ISA 6545","ISA 6545","ISA 6545","ISA 7045","ISA 7045","ISA 7045","ISA 7045","ISA 7550","ISA 7550","ISA 7550","ISA 7550","ISA 8050","ISA 8050","ISA 8050","ISA 8050","ISA 9060","ISA 9060","ISA 9060","ISA 9060","ISA 10065","ISA 10065","ISA 10065","ISA 10075","ISA 10075","ISA 10075","ISA 10075","ISA 12575","ISA 12575","ISA 12575","ISA 12595","ISA 12595","ISA 12595","ISA 12595","ISA 15075","ISA 15075","ISA 15075","ISA 150115","ISA 150115","ISA 150115","ISA 150115","ISA 200100","ISA 200100","ISA 200100","ISA 200150","ISA 200150","ISA 200150","ISA 200150"]
        t=[3,4,5,3,4,5,6,3,4,5,6,3,4,5,6,5,6,8,5,6,8,5,6,8,10,5,6,8,10,5,6,8,10,6,8,10,12,6,8,10,6,8,10,12,6,8,10,6,8,10,12,8,10,12,8,10,12,15,10,12,15,10,12,15,18]
        a=[30,30,30,40,40,40,40,45,45,45,45,50,50,50,50,60,60,60,65,65,65,70,70,70,70,75,75,75,75,80,80,80,80,90,90,90,90,100,100,100,100,100,100,100,125,125,125,125,125,125,125,150,150,150,150,150,150,150,200,200,200,200,200,200,200]
        b=[20,20,20,25,25,25,25,30,30,30,30,30,30,30,30,40,40,40,45,45,45,45,45,45,45,50,50,50,50,50,50,50,50,60,60,60,60,65,65,65,75,75,75,75,75,75,75,95,95,95,95,75,75,75,115,115,115,115,100,100,100,150,150,150,150]
        Ag=[1.41,1.84,2.25,1.88,2.46,3.02,3.56,2.18,2.86,3.52,4.16,2.34,3.07,3.78,4.47,4.76,5.65,7.37,5.26,6.25,8.17,5.52,6.56,8.58,10.52,6.02,7.16,9.38,11.52,6.27,7.46,9.78,12.02,8.65,11.37,14.01,16.57,9.55,12.57,15.51,10.14,13.36,16.50,19.56,11.66,15.38,19.02,12.86,16.98,21.02,24.98,17.42,21.56,25.62,20.58,25.52,30.38,37.52,29.03,34.59,42.78,34.0,40.56,50.25,59.76]
        w=[1.1,1.4,1.8,1.5,1.9,2.4,2.8,1.7,2.2,2.8,3.3,1.8,2.4,3.0,3.5,3.7,4.4,5.8,4.1,4.9,6.4,4.3,5.2,6.7,8.3,4.7,5.6,7.4,9.0,4.9,5.9,7.7,9.4,6.8,8.9,11.0,13.0,7.5,9.9,12.2,8.0,10.5,13.0,15.4,9.2,12.1,14.9,10.1,13.3,16.5,19.6,13.7,16.9,20.1,16.2,20.0,23.8,29.5,22.8,27.2,33.6,26.7,31.8,39.4,46.9]
        ntimes=len(name)
    if(x==3):
        name=["ISLC75","ISLC100","ISLC125","ISLC150","ISLC175","ISLC200","ISLC225","ISLC250","ISLC300","ISLC350","ISLC400","ISMC75","ISMC100","ISMC125","ISMC150","ISMC175","ISMC200","ISMC225","ISMC250","ISMC300","ISMC350","ISMC400"]
        tw=[3.7,4.0,4.4,4.8,5.1,5.5,5.8,6.1,6.7,7.4,8.0,4.4,4.7,5.0,5.4,5.7,6.1,6.4,7.1,7.6,8.1,8.6]
        tf=[6,6.4,6.6,7.8,9.5,10.8,10.2,10.7,11.6,12.5,14.0,7.3,7.5,8.1,9.0,10.2,11.4,12.4,14.1,13.6,13.5,15.3]
        h=[75,100,125,150,175,200,225,250,300,350,400,75,100,125,150,175,200,225,250,300,350,400]
        b=[40,50,65,75,75,75,90,100,100,100,100,40,50,65,75,75,75,80,80,90,100,100]
        Ag=[7.26,10.02,13.67,18.36,22.40,26.22,30.53,35.65,42.11,49.47,58.25,8.67,11.70,16.19,20.88,24.38,28.21,33.01,38.67,45.64,53.65,62.93]
        w=[5.7,7.9,10.7,14.4,17.6,20.6,24.0,28.0,33.1,38.8,45.7,6.8,9.2,12.7,16.4,19.1,22.1,25.9,30.4,35.8,42.1,49.4]
        ntimes=len(name)

    if(x==1 or x==2 or x==3):
        while(i<=(ntimes-1)):

            Vdsb=(Fub/1000)*(1*0.78*(math.pi)*(d**2)/4)/(math.sqrt(3)*GammaMb)
            A=[(1.7/3.0),((2.5*d/(3*d0))-0.25),(Fub/Fu),1.0]
            kb=min(A)
            if(x==1 or x==2):
                Vdpb=(2.5*kb*d*t[i]*Fu/GammaMb)/1000
            if(x==3):
                Vdpb=(2.5*kb*d*tw[i]*Fu/GammaMb)/1000
            BoltF=min(Vdsb,Vdpb)
            nbolt=math.ceil(T/BoltF)
            
            t1=(Ag[i]*100*Fy/Gamma)/1000
            Tdg.append(t1)

            if(x==1 or x==2):
                Beta0=(1.4)-(0.076*(Fy/Fu)*(a[i]/t[i])*(((a[i]+(0.5*b[i]))-t[i])/((nbolt-1)*(2.5*d))))
            if(x==3):
                Beta0=(1.4)-(0.076*(Fy/Fu)*(b[i]/tf[i])*(((b[i]+(0.5*h[i]))-((tf[i]+tw[i])/2))/((nbolt-1)*(2.5*d))))
            Beta1=float(0.7)
            Beta2=(Fu*Gamma/(Fy*GammaMb))
            Beta=float(0)
            if(Beta0<=Beta1 and Beta0<=Beta2):
                Beta=float(0.7)
            elif(Beta0>=Beta1 and Beta0<=Beta2):
                Beta=Beta0
            elif(Beta0>=Beta2):
                Beta=Beta2

            if(x==1 or x==2):
                Anc=(a[i]-(t[i]/2)-d0)*t[i]
                Ago=(a[i]-(t[i]/2))*t[i]
            if(x==3):
                Anc=(h[i]-tf[i]-d0)*tw[i]
                Ago=Ag[i]-(h[i]-tf[i]-d0)*tw[i]

            t2=((0.9*Anc*Fu/GammaMb)+(Beta*Ago*Fy/Gamma))/1000
            Tdn.append(t2)

            if(x==1 or x==2):
                Avg=t[i]*(((nbolt-1)*(2.5*d))+(1.7*d0))
                Avn=t[i]*(((nbolt-1)*(2.5*d))+(1.7*d0)-((nbolt-0.5)*d0))

                Atg=t[i]*((a[i]-(t[i]/2))/2)
                Atn=t[i]*(((a[i]-(t[i]/2))/2)-(0.5*d0))
            if(x==3):
                Avg=tw[i]*(((nbolt-1)*(2.5*d))+(1.7*d0))
                Avn=tw[i]*(((nbolt-1)*(2.5*d))+(1.7*d0)-((nbolt-0.5)*d0))

                Atg=tw[i]*(((h[i]-tf[i])/2)+(b[i]-(tw[i]/2)))
                Atn=tw[i]*((((h[i]-tf[i])/2)+(b[i]-(tw[i]/2)))-(0.5*d0))

            t3=((Avg*Fy/(math.sqrt(3)*Gamma))+(0.9*Atn*Fu/GammaMb))/1000
            t4=((0.9*Avn*Fu/(math.sqrt(3)*GammaMb))+(Atg*Fy/Gamma))/1000
            
            Tdb1.append(t3)
            Tdb2.append(t4)
            
            Td=min(t1,t2,t3,t4)
            
            if(T<=Td):

                Anc1.append(Anc)
                Ago1.append(Ago)
                Avg1.append(Avg)
                Avn1.append(Avn)
                Atg1.append(Atg)
                Atn1.append(Atn)

                Tdg1.append(t1)
                Tdn1.append(t2)
                Tdb11.append(t3)
                Tdb21.append(t4)
                
                Treal1.append(Td)
                name1.append(name[i])
                if(x==1 or x==2):
                    thick1.append(t[i])
                    a1.append(a[i])
                b1.append(b[i])
                if(x==3):
                    thick1.append(tw[i])
                    a1.append(h[i])
                Ag1.append(Ag[i])
                w1.append(w[i])
            i=i+1
            
        nlen=len(name1)
        j=int(0)
        
        while(j<=(nlen-1)):
            x1=min(w1)
            y1=w1.index(x1)

            Tdg2.append(Tdg1[y1])
            Tdn2.append(Tdn1[y1])
            Tdb12.append(Tdb11[y1])
            Tdb22.append(Tdb21[y1])

            Anc2.append(Anc1[y1])
            Ago2.append(Ago1[y1])
            Avg2.append(Avg1[y1])
            Avn2.append(Avn1[y1])
            Atg2.append(Atg1[y1])
            Atn2.append(Atn1[y1])
            
            Treal2.append(Treal1[y1])     
            name2.append(name1[y1])
            thick2.append(thick1[y1])
            a2.append(a1[y1])
            b2.append(b1[y1])
            Ag2.append(Ag1[y1])
            w2.append(w1[y1])

            Tdg1.pop(y1)
            Tdn1.pop(y1)
            Tdb11.pop(y1)
            Tdb21.pop(y1)
            Anc1.pop(y1)
            Ago1.pop(y1)
            Avg1.pop(y1)
            Avn1.pop(y1)
            Atg1.pop(y1)
            Atn1.pop(y1)
            Treal1.pop(y1)
            name1.pop(y1)
            thick1.pop(y1)
            a1.pop(y1)
            b1.pop(y1)
            Ag1.pop(y1)
            w1.pop(y1)
            
            j=j+1
    i=int(0)
    stoplen=len(name2)
    def f10():

        window4=Toplevel()
        window4.title("Analysis Result")
        window4.state('zoomed')
        window4.configure(bg="lavender")

        if(i<=(stoplen-1)):
            Tdnew=min(Tdg2[i],Tdn2[i],Tdb12[i],Tdb22[i])
            canvas7=Canvas(window4,width=670,height=210,bg="aquamarine",borderwidth=2,relief="solid")
            canvas7.place(x=685,y=0)
            label25=Label(window4,text="SINGLE ROW OF BOLTS",fg="blue",bg="aquamarine",font=("Times New Roman Bold",22))
            label25.place(x=820,y=5)
            label26=Label(window4,text="No. of Bolts Req.(n) = ",fg="black",bg="aquamarine",font=("Sitka Small Bold",17))
            label26.place(x=700,y=42)
            label27=Label(window4,text=round(nbolt,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label27.place(x=1105,y=46)
            label28=Label(window4,text="Bolts",fg="black",bg="aquamarine",font=("Verdana Bold",17))
            label28.place(x=1271,y=47)
            label29=Label(window4,text="Bolt Shear Strength = ",fg="black",bg="aquamarine",font=("Sitka Small Bold",17))
            label29.place(x=700,y=82)
            label30=Label(window4,text=round(Vdsb,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label30.place(x=1105,y=88)
            label31=Label(window4,text="KN",fg="black",bg="aquamarine",font=("Verdana Bold",17))
            label31.place(x=1285,y=90)
            label32=Label(window4,text="Bolt Bearing Strength = ",fg="black",bg="aquamarine",font=("Sitka Small Bold",17))
            label32.place(x=700,y=122)
            label33=Label(window4,text=round(Vdpb,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label33.place(x=1105,y=130)
            label34=Label(window4,text="KN",fg="black",bg="aquamarine",font=("Verdana Bold",17))
            label34.place(x=1285,y=130)
            label35=Label(window4,text="Bolt Strength = ",fg="black",bg="aquamarine",font=("Sitka Small Bold",17))
            label35.place(x=700,y=162)
            label36=Label(window4,text=round(BoltF,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label36.place(x=1105,y=172)
            label37=Label(window4,text="KN",fg="black",bg="aquamarine",font=("Verdana Bold",17))
            label37.place(x=1285,y=170)
            

            canvas8=Canvas(window4,width=670,height=210,bg="yellow",borderwidth=2,relief="solid")
            canvas8.place(x=5,y=0)
            label38=Label(window4,text="SELECTED SECTION",fg="blue",bg="yellow",font=("Times New Roman Bold",22))
            label38.place(x=150,y=5)
            label39=Label(window4,text="Name of Section = ",fg="black",font=("Sitka Small Bold",17),bg="yellow")
            label39.place(x=15,y=42)
            label40=Label(window4,text=name2[i],fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label40.place(x=410,y=46)
            label41=Label(window4,text="Weight (w) = ",fg="black",bg="yellow",font=("Sitka Small Bold",17))
            label41.place(x=15,y=82)
            label42=Label(window4,text=round(w2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label42.place(x=410,y=88)
            label43=Label(window4,text="Kg/m",fg="black",bg="yellow",font=("Verdana Bold",17))
            label43.place(x=576,y=90)
            label44=Label(window4,text="Cross-Section Area (Ag) =",fg="black",bg="yellow",font=("Sitka Small Bold",17))
            label44.place(x=15,y=122)
            label45=Label(window4,text=round(Ag2[i]*100,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label45.place(x=410,y=130)
            label46=Label(window4,text="mm2",fg="black",bg="yellow",font=("Verdana Bold",17))
            label46.place(x=576,y=130)
            label47=Label(window4,text="Thickness (t) = ",fg="black",bg="yellow",font=("Sitka Small Bold",17))
            label47.place(x=15,y=162)
            label48=Label(window4,text=round(thick2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label48.place(x=410,y=172)
            label49=Label(window4,text="mm",fg="black",bg="yellow",font=("Verdana Bold",17))
            label49.place(x=576,y=170)

            canvas9=Canvas(window4,width=670,height=210,bg="coral",borderwidth=2,relief="solid")
            canvas9.place(x=5,y=220)
            label50=Label(window4,text="YIELD & RUPTURE FAILURE",fg="blue",bg="coral",font=("Times New Roman Bold",22))
            label50.place(x=80,y=225)
            label51=Label(window4,text="Net Connected Area(Anc)=",fg="black",font=("Sitka Small Bold",17),bg="coral")
            label51.place(x=12,y=262)
            label52=Label(window4,text=round(Anc2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label52.place(x=410,y=265)
            label53=Label(window4,text="mm2",fg="black",bg="coral",font=("Verdana Bold",17))
            label53.place(x=586,y=265)
            label54=Label(window4,text="Gross Outstanding Area(Ago)=",fg="black",font=("Sitka Small Bold",15),bg="coral")
            label54.place(x=12,y=305)
            label55=Label(window4,text=round(Ago2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label55.place(x=410,y=307)
            label56=Label(window4,text="mm2",fg="black",bg="coral",font=("Verdana Bold",17))
            label56.place(x=586,y=305)
            label57=Label(window4,text="Rupture Strength(Tdn)=",fg="black",font=("Sitka Small Bold",17),bg="coral")
            label57.place(x=12,y=342)
            label58=Label(window4,text=round(Tdn2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label58.place(x=410,y=349)
            label59=Label(window4,text="KN",fg="black",bg="coral",font=("Verdana Bold",17))
            label59.place(x=596,y=345)
            label79=Label(window4,text="Yield Strength(Tdg)=",fg="black",font=("Sitka Small Bold",17),bg="coral")
            label79.place(x=12,y=382)
            label80=Label(window4,text=round(Tdg2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label80.place(x=410,y=391)
            label81=Label(window4,text="KN",fg="black",bg="coral",font=("Verdana Bold",17))
            label81.place(x=596,y=385)
            

            canvas10=Canvas(window4,width=670,height=210,bg="cyan2",borderwidth=2,relief="solid")
            canvas10.place(x=5,y=440)
            label60=Label(window4,text="BLOCK SHEAR FAILURE",fg="blue",bg="cyan2",font=("Times New Roman Bold",22))
            label60.place(x=100,y=445)
            label61=Label(window4,text="Avg = ",fg="black",font=("Sitka Small Bold",17),bg="cyan2")
            label61.place(x=10,y=490)
            label62=Label(window4,text=round(Avg2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label62.place(x=100,y=495)
            label63=Label(window4,text="mm2",fg="black",bg="cyan2",font=("Verdana Bold",13))
            label63.place(x=270,y=500)
            label64=Label(window4,text="Avn = ",fg="black",font=("Sitka Small Bold",17),bg="cyan2")
            label64.place(x=10,y=535)
            label65=Label(window4,text=round(Avn2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label65.place(x=100,y=540)
            label66=Label(window4,text="mm2",fg="black",bg="cyan2",font=("Verdana Bold",13))
            label66.place(x=270,y=545)
            label67=Label(window4,text="Atg = ",fg="black",font=("Sitka Small Bold",17),bg="cyan2")
            label67.place(x=350,y=490)
            label68=Label(window4,text=round(Atg2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label68.place(x=440,y=495)
            label69=Label(window4,text="mm2",fg="black",bg="cyan2",font=("Verdana Bold",13))
            label69.place(x=610,y=500)
            label70=Label(window4,text="Atn = ",fg="black",font=("Sitka Small Bold",17),bg="cyan2")
            label70.place(x=350,y=535)
            label71=Label(window4,text=round(Atn2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label71.place(x=440,y=540)
            label72=Label(window4,text="mm2",fg="black",bg="cyan2",font=("Verdana Bold",13))
            label72.place(x=610,y=545)
            label73=Label(window4,text="Tdb1=",fg="black",font=("Sitka Small Bold",17),bg="cyan2")
            label73.place(x=10,y=580)
            label74=Label(window4,text=round(Tdb12[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label74.place(x=100,y=585)
            label75=Label(window4,text="KN",fg="black",bg="cyan2",font=("Verdana Bold",13))
            label75.place(x=270,y=590)
            label76=Label(window4,text="Tdb2=",fg="black",font=("Sitka Small Bold",17),bg="cyan2")
            label76.place(x=350,y=580)
            label77=Label(window4,text=round(Tdb22[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label77.place(x=440,y=585)
            label78=Label(window4,text="KN",fg="black",bg="cyan2",font=("Verdana Bold",13))
            label78.place(x=610,y=590)
            
            
            canvas11=Canvas(window4,width=670,height=210,bg="aliceblue",borderwidth=2,relief="solid")
            canvas11.place(x=685,y=220)
            label90=Label(window4,text="BOLT ORIENTATION",fg="blue",bg="aliceblue",font=("Times New Roman Bold",22))
            label90.place(x=840,y=225)
            label91=Label(window4,text="Minimum Pitch(p) = ",fg="black",font=("Sitka Small Bold",17),bg="aliceblue")
            label91.place(x=692,y=262)
            label92=Label(window4,text=round(2.5*d,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label92.place(x=1125,y=265)
            label93=Label(window4,text="mm",fg="black",bg="aliceblue",font=("Verdana Bold",17))
            label93.place(x=1291,y=265)
            label94=Label(window4,text="Minimum Edge Distance(e)=",fg="black",font=("Sitka Small Bold",17),bg="aliceblue")
            label94.place(x=692,y=302)
            label95=Label(window4,text=round(1.7*d0,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label95.place(x=1125,y=307)
            label96=Label(window4,text="mm",fg="black",bg="aliceblue",font=("Verdana Bold",17))
            label96.place(x=1291,y=307)
            label97=Label(window4,text="Connection Length(Lc) = ",fg="black",font=("Sitka Small Bold",17),bg="aliceblue")
            label97.place(x=692,y=345)
            label98=Label(window4,text=round((nbolt-1)*(2.5*d),2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label98.place(x=1125,y=349)
            label99=Label(window4,text="mm",fg="black",bg="aliceblue",font=("Verdana Bold",17))
            label99.place(x=1291,y=350)
            label100=Label(window4,text="Shear Lag Width(Bs) = ",fg="black",font=("Sitka Small Bold",17),bg="aliceblue")
            label100.place(x=692,y=385)
            label101=Label(window4,text=round((a2[i]+(0.5*b2[i]))-thick2[i],2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label101.place(x=1125,y=391)
            label102=Label(window4,text="mm",fg="black",bg="aliceblue",font=("Verdana Bold",17))
            label102.place(x=1291,y=390)
            

            canvas12=Canvas(window4,width=670,height=210,bg="lightsalmon",borderwidth=2,relief="solid")
            canvas12.place(x=685,y=440)
            label82=Label(window4,text="FINAL RESULT",fg="blue",bg="lightsalmon",font=("Times New Roman Bold",22))
            label82.place(x=880,y=445)
            label83=Label(window4,text="Design Tension(T) = ",fg="black",font=("Sitka Small Bold",17),bg="lightsalmon")
            label83.place(x=700,y=505)
            label84=Label(window4,text=round(T,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label84.place(x=1115,y=505)
            label85=Label(window4,text="KN",fg="black",bg="lightsalmon",font=("Verdana Bold",17))
            label85.place(x=1285,y=505)
            label86=Label(window4,text="Section Strength(Td) = ",fg="black",font=("Sitka Small Bold",17),bg="lightsalmon")
            label86.place(x=700,y=555)
            label87=Label(window4,text=round(Tdnew,2),fg="black",bg="greenyellow",width=8,font=("Verdana Bold",17),borderwidth=2,relief="solid")
            label87.place(x=1115,y=555)
            label88=Label(window4,text="KN",fg="black",bg="lightsalmon",font=("Verdana Bold",17))
            label88.place(x=1285,y=555)
            label89=Label(window4,text="T < Td i.e (SAFE) ",fg="black",font=("Sitka Small Bold",17),bg="red")
            label89.place(x=880,y=602)

            label90=Label(window4,text="Do you want to get the next best design.....Click on NEXT Button",fg="black",font=("Sitka Small Bold",14),bg="green")
            label90.place(x=300,y=655)

        def next_page():
            global i
            i=i+1
            window4.destroy()
            f10()
        def previous_page():
            global i
            i=i-1
            window4.destroy()
            f10()
        def exit_window4():
            window4.destroy()
            global i
            i=0

        nextbtn=Button(window4,text="NEXT",fg="black",bg="red",width=8,command=next_page,borderwidth=2,relief="raised",font=("Arial Bold",14))
        nextbtn.place(x=1250,y=650)

        previousbtn=Button(window4,text="PREVIOUS",fg="black",bg="red",width=8,command=previous_page,borderwidth=2,relief="raised",font=("Arial Bold",14))
        previousbtn.place(x=0,y=650)

        exitbtn4=Button(window4,text="EXIT",fg="black",bg="red",width=5,command=exit_window4,borderwidth=2,relief="raised",font=("Arial Bold",14))
        exitbtn4.place(x=1290,y=0)
        
        window4.mainloop()

    f10()
        
def exit_window():
    window.destroy()

exitbtn1=Button(window,text="EXIT",fg="black",bg="red",width=7,command=exit_window,borderwidth=2,relief="raised",font=("Verdana Bold",18))
exitbtn1.place(x=1230,y=0)

helpbtn1=Button(window,text="HELP",fg="black",bg="red",width=7,command=exit_window,borderwidth=2,relief="raised",font=("Verdana Bold",18))
helpbtn1.place(x=1095,y=0)

resetbtn1=Button(window,text="RESET",fg="black",bg="red",width=7,command=exit_window,borderwidth=2,relief="raised",font=("Verdana Bold",18))
resetbtn1.place(x=960,y=0)

sectionpreference_label=Label(window,text="PREFERRED SECTION",fg="blue",bg="white",font=("Sitka Small Bold",20))
sectionpreference_label.place(x=609,y=85)

radio1=Radiobutton(window,text="Equal Angle Section",variable=u,value=1,command=f2,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio1.place(x=630,y=150)

radio2=Radiobutton(window,text="Unequal Angle Section",variable=u,value=2,command=f2,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio2.place(x=630,y=205)

radio3=Radiobutton(window,text="Channel Section",variable=u,value=3,command=f3,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio3.place(x=630,y=260)

radio4=Radiobutton(window,text="I Section",variable=u,value=4,command=f3,fg="black",bg="white",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio4.place(x=630,y=315)

boltpreference_label=Label(window,text="PREFERRED BOLT",fg="blue",bg="lemonchiffon",font=("Sitka Small Bold",20))
boltpreference_label.place(x=1020,y=85)

radio5=Radiobutton(window,text="Grade 4.6",variable=v,value=1,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio5.place(x=1020,y=150)

radio6=Radiobutton(window,text="Grade 8.8",variable=v,value=2,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio6.place(x=1020,y=205)

radio7=Radiobutton(window,text="Grade 10.9",variable=v,value=3,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio7.place(x=1020,y=260)

radio8=Radiobutton(window,text="Grade 12.9",variable=v,value=4,fg="black",bg="lemonchiffon",font=("Sitka Small Bold",15),borderwidth=2,relief="solid")
radio8.place(x=1020,y=315)

resultbtn=Button(window,text="RESULT",fg="black",bg="red",width=10,command=f1,borderwidth=2,relief="raised",font=("Verdana Bold",15))
resultbtn.place(x=1195,y=635)

window.mainloop()
