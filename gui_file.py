import tkinter as tk
from tkinter import ttk,messagebox,filedialog
import os
import PyPDF2
root=tk.Tk()
root.title('PDF Passworder')
##################Welcome Lable###########################3

lable0=tk.Label(root,text='Welcome to PDF Passworder',font=("Arial",25),fg="Red")
lable0.grid(row=0,column=0,columnspan=3)

################# Enter Path ###########################

pdf_lable=tk.Label(root,text='Folder Path',font=("Arial",20))
pdf_lable.grid(row=1,column=0,sticky=tk.W)
pdf_main_var=tk.StringVar()
pdf_main_entry=ttk.Entry(root,font=("Arial",10),width=25,textvariable=pdf_main_var)
pdf_main_entry.grid(row=1,column=1)
def select_func():
    global pdf_path
    pdf_path = filedialog.askopenfilename(title='Select File')
    pdf_main_var.set(pdf_path)
select_button = ttk.Button(root,command=select_func,text='Select Path')
select_button.grid(row=1,column=3)

#################### Password ################
pass_var=tk.StringVar()
password_lable=ttk.Label(text="Enter Password",font=("Arial",20))
password_lable.grid(row=2,column=0,sticky=tk.W)
password_entry=ttk.Entry(font=("Arial",20),show='*')
password_entry.grid(row=2,column=1)
######################## saved Password  ####################
pdf_save=tk.Label(root,text='Save Folder Path',font=("Arial",20))
pdf_save.grid(row=3,column=0,sticky=tk.W)
pdf_save_var=tk.StringVar()
pdf_save_entry=ttk.Entry(root,font=("Arial",10),width=25,textvariable=pdf_save_var)
pdf_save_entry.grid(row=3,column=1)
def select_func():
    global pdf_save_path
    pdf_save_path = filedialog.askdirectory(title='Select File')
    pdf_main_var.set(pdf_save_path)
select_button = ttk.Button(root,command=select_func,text='Select Path')
select_button.grid(row=3,column=3)


##################### Submit Button ###############
def sub_func():
    try:
        pdf_path1=pdf_main_var.get()
        pdf_reader = PyPDF2.PdfFileReader(pdf_path1)
        pdf_writer = PyPDF2.PdfFileWriter()
        password=pass_var.get()
        save=pdf_save_var.get()
        for i in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(i))
        pdf_writer.encrypt(password)
        with open(save, 'wb') as f:
            pdf_writer.write(f)
            f.close()
        print("Submitted")
    except PyPDF2.utils.PdfReadError:
        ttk.Label(text="Sorry these is not a good pdf",font=("Arial",20)).grid(row=12,column=0)
    except ValueError:
        tk.messagebox.askretrycancel('Error', 'Please Select Right Value')
    except FileNotFoundError:
        tk.messagebox.askretrycancel('Error', 'Path Not Found')
    pass_var.set('')
submit_butt = ttk.Button(text="Submit", command=sub_func)
submit_butt.grid(row=4, columnspan=3)
submit_butt.focus()


root.mainloop()