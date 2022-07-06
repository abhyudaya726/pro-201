from tkinter import *

window = Tk()

window.title("Interest Rate Calculator")
window.geometry("380x400")
window.configure(bg='lightcyan')

def calc_interest():
    principle = int(principle_input.get())
    time = int(time_input.get())
    interest_rate = int(interest_input.get())

    interest = (principle*time*interest_rate)/100
    interest = round(interest,1)

    output_msg = Label(result_frame, text="Your Total Amount is is "+str(interest), bg="lightcyan",font=("Calibri", 12),width=45)
    output_msg.place(x=20,y=40)
    output_msg.pack()

app_label=Label(window, text="Interest Rate Calculator", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label=Label(window, text="Principle Amount", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principle_label.place(x=20, y=90)

principle_input = Entry(window, text="", bd=2, width=22)
principle_input.place(x=150, y=92)

time_label = Label(window, text="Enter The Time Period", fg="black", bg="lightcyan", font=("Calibri", 10), bd=1)
time_label.place(x=21,y=140)

time_input = Entry(window, text="", bd=2, width=15)
time_input.place(x=150,y=142)

interest_label = Label(window, text="Enter The Interest Rate", fg="black", bg="lightcyan", font=("Calibri", 10), bd=1)
interest_label.place(x=20,y=185)

interest_input = Entry(window, text="", bd=2, width=15)
interest_input.place(x=150,y=187)

calc_button = Button(window, text="Calculate", fg="black", bg="lightcyan", font=("Calibri", 12), bd=1,command=calc_interest)
calc_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Total Amount", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label = Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()