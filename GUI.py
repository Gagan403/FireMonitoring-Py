from tkinter import *
from main import *
from mapcreater import *

def about():
    abt=Tk()
    abt.title("ABOUT")
    l1=Label(abt,text=" MINI PROJECT IN PYTHON FOR 5TH SEM").pack()
    l12=Label(abt,text="  ").pack()
    l2=Label(abt,text=" -> THIS PROJECT  SHALL DETECT FIRE IN DARK PLACE WHERE NO LIGHT IS PRESENT").pack()
    l3=Label(abt,text=" -> IN THIS PROJECT WE HAVE UTILIZED SOME OF THE LIBRARIES AVAILABLE IN PYTHON ").pack()
    l4=Label(abt,text=" -> EXAMPLE:-Tkinter, Webbrowser,Opencv2,Folium,Geocoders,PlaySound  ").pack()
    l5=Label(abt,text=" -> THIS PROJECT USES HAAR CASCADE FILE TO RECONGNIZE THE FIRE,AND THIS HAAR FILE IS GENERATED USING CASCADE TRAINNER APPLICATION ").pack()
    l6=Label(abt,text=" -> THIS PROJECT IS BUILT WITH TWO BASIC FEATURES NAMELY SURVAILLANCE AND MAP(LOCATION)  ").pack()
    l7=Label(abt,text=" -> AS SOON AS THE FIRE GETS DETECTED IT GIVES A BUZZER AND CAPUTRES THE CURRENT LOCATION ").pack()
    l8=Label(abt,text=" -> THE USER CAN CHECK THE LOCATION BY CLICKING THE MAP OPTION ").pack()
    l9=Label(abt,text=" -> PROJECT IS DEVELOPED UNDER THE GUIDANCE OF "" LAKSHMI HANNE MAAM " "").pack()
    l10=Label(abt,text=" -> ALSO REFERED GOOGLE,YOUTUBE. ").pack()
    l11=Label(abt,text="   THANK YOU ",font=('arial',30)).pack()
    abt.mainloop()

win1 = Tk()
win1.title("WELCOME PAGE")
win1.geometry('400x150')
l1=Label(win1,text="WELCOME",font=('arial',20)).pack()
b1 = Button(win1, text=" SURVAILLANCE  ",command=fire,bg='orange').place(relx=0.5, rely=0.1, anchor=CENTER)
b2 = Button(win1, text="MAP(LOCATION)",command= map1,bg='orange').place(relx=0.5, rely=0.2, anchor=CENTER)
b3 = Button(win1, text="         ABOUT          ",command= about,bg='orange').place(relx=0.5, rely=0.3, anchor=CENTER)

win1.mainloop()