from Tkinter import *
import random
root=None
my_text=None
ele=[]
int_list=[]
def prime_gen():
    global my_text
    k=random.randint(0,l-1)
    #print str(k)
    my_text.set("Prime Number: %d"%int_list[k])
    
def addTextLabel(root):
    global my_text
    my_text=StringVar()
    my_text.set("")
    myLabel=Label(root,textvariable=my_text)
    myLabel.pack()

    
def main():
    global root
    root=Tk()
    root.geometry("300x200")
    root.title("Random Prime Generator")
    b=Button(root,text="Click here!",command=prime_gen)
    b.pack(side=TOP)
    addTextLabel(root)
    b1=Button(root,text="Exit",command=root.destroy)
    b1.pack(side=BOTTOM) 
    root.mainloop()
n="prime.txt"
data=" "
fp=open(n)
while data!="":
        data=fp.readline()
        ele=ele+data.split(',')       
for i in ele:
        if i!='\n' and i!='':
            int_list.append(int(i))
l=len(int_list) 
#print str(l)               
main()    
