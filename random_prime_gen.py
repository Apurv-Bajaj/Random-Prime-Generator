from Tkinter import *
import random


root=None
my_text=None
ele = []
l = 0


def prime_gen():
	global my_text
	k=random.randint(0,l-1)
	#print str(k)
	my_text.set("Prime Number: %d"%ele[k])
    
def addTextLabel(root):
	global my_text
	my_text=StringVar()
	my_text.set("")
	myLabel=Label(root,textvariable=my_text)
	myLabel.pack()

    
def main():
	global root
	global ele
	global l
	file_name="prime.txt"
	data = []
	fp=open(file_name,'r')
	for line in fp:
			data = line.split(',')[:-1] 	# removes '' and '\n' here directly, this will directly remove the next for loop
			ele += [int(x) for x in data]       # Use += instead of + if you're extending same list, you can use `extend()` method as well 
	l=len(ele) 	
	root=Tk()
	root.geometry("300x200")
	root.title("Random Prime Generator")
	b=Button(root,text="Click here!",command=prime_gen)
	b.pack(side=TOP)
	addTextLabel(root)
	b1=Button(root,text="Exit",command=root.destroy)
	b1.pack(side=BOTTOM) 
	root.mainloop()


# good practice 
if __name__ == "__main__":      
	main() 
