#Aplikacja, która oblicza najważniejsze charakterystyki trójkąta: pole,
#obwód, wszystkie wysokości oraz miary wszystkich kątów. Program
#powinien zawierać trzy pola wejściowe (długości boków trójkąta) oraz
#osiem pól tekstowych (pole obwód, trzy wysokości, trzy kąty).
#Zabezpieczyć program przed błędnymi danymi wejściowymi (długości
#boków trójkąta powinny być liczbami, powinny być dodatnie, musi się
#dać zbudować z nich trójkąt). Zabezpieczyć program przed
#wprowadzaniem błędnych danych, wykorzystując okna dialogowe.
from tkinter import *
from tkinter import messagebox
from math import pi,asin
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.etykieta=Label(self)
        self.etykieta["text"]="Podaj bok a:"
        self.etykieta.grid(row=0,column=0,sticky=W)
        self.polewej=Entry(self,width=10)
        self.polewej.grid(row=0,column=1,sticky=W)
        
        self.etykieta2=Label(self)
        self.etykieta2["text"]="Podaj bok b:"
        self.etykieta2.grid(row=1,column=0,sticky=W)
        
        self.polewej2=Entry(self,width=10)
        self.polewej2.grid(row=1,column=1,sticky=W)
        
        self.etykieta3=Label(self)
        self.etykieta3["text"]="Podaj bok c:"
        self.etykieta3.grid(row=2,column=0,sticky=W)
        self.polewej3=Entry(self,width=10)
        self.polewej3.grid(row=2,column=1,sticky=W)
        
        self.przycisk=Button(self,width=20,height=1)
        self.przycisk["text"]="Oblicz charakterystyki"
        self.przycisk.grid(row=4,column=0,sticky=W)
        self.przycisk["command"]=self.update
        
        self.etykieta4=Label(self)
        self.etykieta4["text"]="Pole trójkąta:"
        self.etykieta4.grid(row=5,column=0,sticky=W)
        
        self.poletext=Text(self,width=10,height=1)
        self.poletext.grid(row=5,column=1,sticky=W)
        
        self.etykieta5=Label(self)
        self.etykieta5["text"]="Obwód trójkąta:"
        self.etykieta5.grid(row=6,column=0,sticky=W)
        
        self.poletext2=Text(self,width=10,height=1)
        self.poletext2.grid(row=6,column=1,sticky=W)

        self.etykieta6=Label(self)
        self.etykieta6["text"]="Wysokosc na bok a trójkąta:"
        self.etykieta6.grid(row=7,column=0,sticky=W)
        
        self.poletext3=Text(self,width=10,height=1)
        self.poletext3.grid(row=7,column=1,sticky=W)

        self.etykieta7=Label(self)
        self.etykieta7["text"]="Wysokosc na bok b trójkąta:"
        self.etykieta7.grid(row=8,column=0,sticky=W)
        
        self.poletext4=Text(self,width=10,height=1)
        self.poletext4.grid(row=8,column=1,sticky=W)
        
        self.etykieta8=Label(self)
        self.etykieta8["text"]="Wysokosc na bok c trójkąta:"
        self.etykieta8.grid(row=9,column=0,sticky=W)
        
        self.poletext5=Text(self,width=10,height=1)
        self.poletext5.grid(row=9,column=1,sticky=W)

        self.etykieta9=Label(self)
        self.etykieta9["text"]="Kąt alfa:"
        self.etykieta9.grid(row=10,column=0,sticky=W)
        
        self.poletext6=Text(self,width=10,height=1)
        self.poletext6.grid(row=10,column=1,sticky=W)

        self.etykieta10=Label(self)
        self.etykieta10["text"]="Kąt beta:"
        self.etykieta10.grid(row=11,column=0,sticky=W)
        
        self.poletext7=Text(self,width=10,height=1)
        self.poletext7.grid(row=11,column=1,sticky=W)
        
        self.etykieta11=Label(self)
        self.etykieta11["text"]="Kąt gamma:"
        self.etykieta11.grid(row=12,column=0,sticky=W)
        
        self.poletext8=Text(self,width=10,height=1)
        self.poletext8.grid(row=12,column=1,sticky=W)


    def update(self):
        self.poletext.delete(0.0,END)
        self.poletext2.delete(0.0,END)
        self.poletext3.delete(0.0,END)
        self.poletext4.delete(0.0,END)
        self.poletext5.delete(0.0,END)
        self.poletext6.delete(0.0,END)
        self.poletext7.delete(0.0,END)
        self.poletext8.delete(0.0,END)
        try:
            obw=float(self.polewej.get())+float(self.polewej2.get())+float(self.polewej3.get())
            p=obw/2
            pole=(p*(p-float(self.polewej.get()))*(p-float(self.polewej2.get()))*(p-float(self.polewej3.get())))**(1/2)
            wysa=pole*2/float(self.polewej.get())
            wysb=pole*2/float(self.polewej2.get())
            wysc=pole*2/float(self.polewej3.get())
            alfa=asin(pole*2/(float(self.polewej.get())*(float(self.polewej2.get()))))/pi*180
            beta=asin(pole*2/(float(self.polewej.get())*(float(self.polewej3.get()))))/pi*180
            gama=asin(pole*2/(float(self.polewej2.get())*(float(self.polewej3.get()))))/pi*180
            if float(self.polewej.get())<=0 or float(self.polewej2.get())<=0 or float(self.polewej3.get())<=0:
                raise ValueError
        except:
            messagebox.showerror("BŁĄD", "Błędne dane!")
        else:
            self.poletext.insert(0.0,pole)
            self.poletext2.insert(0.0,obw)
            self.poletext3.insert(0.0,wysa)
            self.poletext4.insert(0.0,wysb)
            self.poletext5.insert(0.0,wysc)
            self.poletext6.insert(0.0,round(alfa,2))
            self.poletext7.insert(0.0,round(beta,2))
            self.poletext8.insert(0.0,round(gama,2))
            
            
okno=Tk()
okno.title("Pole kwadratu")
okno.geometry("600x400")
ap=Application(okno)
okno.mainloop()
