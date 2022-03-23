from tkinter import*
import random

root=Tk()
root.title("my picnic bag")
root.geometry("600x400")
root.configure(background="teal" )

label1=Label(root)
label2=Label(root)
list1=["sandwich","water","ball","games","chips","pasta","bottle"]
label1["text"]="listed items storage:"+str(list1)
label1.place(relx=0.5,rely=0.4,anchor=CENTER)

def adding():
    random_no=random.sample(range(0,6),1)
    label2["text"]="put item no. "+str(random_no)+" in the bag"

button1=Button(root,bg="blue",fg="white",text="add item in my bag" , command=adding)
label2.place(relx=0.5,rely=0.5,anchor=CENTER)
button1.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()