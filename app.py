from tkinter import *
from googletrans import Translator

def translate():
  message = text1.get('1.0','end-1c') #fletch message from text1 and store in variable
  translator = Translator()
  output = translator.translate(text=message,src='en',dest='th')
  text2.insert('end',output.text)
  
def reset():
  text1.delete(1.0,'end')
  text2.delete(1.0,'end')
    
#screen size
root = Tk()
root.title("Google Translate (EN-TH)")
root.geometry('530x300')
root.maxsize(530.300)
root.minsize(530.300)

#widget
label=Label(text="English - Thai", font=('Arial',25,'bold'))
label.place(x=10,y=70)

#store Thai message
text2 = Text(root,width=30,height=10)
text2.place(x=260,y=70)

#button
translateBtn = Button(root,text="translate",command=translate)
translateBtn.place(x=180,y=250)

clearBtn = Button(root,text='clear',command=reset)
clearBtn.place(x=280,y=250)
root.mainloop()