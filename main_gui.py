############## import portion####################
import PyPDF2
import os
import tkinter as tk
from tkinter import ttk,messagebox,filedialog
############## end of import portion####################
########### tkinter variable & geometery ########################
root=tk.Tk()
root.title('PDF Passworder')
root.wm_iconbitmap(r'C:\Users\RAKESH\PycharmProjects\PDFpassworder\protect-pdf-file-512.png')
###########end of tkinter variable & geometery ########################

###################### all label ################

welcome_label=tk.Label(root,text='Welcome to PDF Passworder',fg='red',font=('Arial',20))
welcome_label.grid(row=0,column=0,columnspan=3)

folder_path=tk.Label(root,text='Enter Folder Path',font=('Arial',20))
folder_path.grid(row=1,column=0,sticky=tk.W)

password=tk.Label(root,text='Enter Password',font=('Arial',20))
password.grid(row=2,column=0,sticky=tk.W)

save_folder_path=tk.Label(root,text='Enter Save Folder Path',font=('Arial',20))
save_folder_path.grid(row=3,column=0,sticky=tk.W)

###################### end of all label ################

###################### all variables ######################
folder_path_var=tk.StringVar()
password_var=tk.StringVar()
save_folder_path_var=tk.StringVar()
###################### end of all variables ######################

######################### all entry vaiables ######################
folder_path_entry=ttk.Entry(root,font=('Arial',20),textvariable=folder_path_var)
folder_path_entry.grid(row=1,column=1,padx=5,pady=5)

Enter_Password_entry=ttk.Entry(root,font=('Arial',20),textvariable=password_var)
Enter_Password_entry.grid(row=2,column=1,padx=5,pady=5)

save_folder_path_entry=ttk.Entry(root,font=('Arial',20),textvariable=save_folder_path_var)
save_folder_path_entry.grid(row=3,column=1,padx=5,pady=5)

######################### end of all entry vaiables ######################

###################### Buttons ############################
select_path_button=ttk.Button(text='Select')
select_path_button.grid(row=1,column=3)

select_save_button=ttk.Button(text='Select')
select_save_button.grid(row=3,column=3)

submit_button=ttk.Button(text='Submit')
submit_button.grid(row=4,columnspan=3,padx=5,pady=5)

###################### end of Buttons ############################

##################### Button Functionality #####################
def select_path_func():
    global folder_path_var
    select_path=filedialog.askopenfilename(title='Select Path')
    folder_path_var.set(select_path)
select_path_button.config(command=select_path_func)

def select_save_func():
    global save_folder_path_var
    save_path=filedialog.askopenfilename(title='Select Path')
    save_folder_path_var.set(save_path)

select_save_button.config(command=select_save_func)
count=5
def select_sabmit_func():
    try:
        global count
        count+=1
        save_folder_path_var_get=save_folder_path_var.get()
        folder_path_var_get=folder_path_var.get()
        password_var_get=password_var.get()
        a=PyPDF2.PdfFileReader(folder_path_var_get)
        b=PyPDF2.PdfFileWriter()

        for i in range(a.numPages):
            b.addPage(a.getPage(i))
        b.encrypt(password_var_get)
        with open(save_folder_path_var_get,'wb') as f:
            b.write(f)

        # ttk.Scrollbar(root).pack(side=tk.RIGHT,fill=tk.Y)

        ttk.Label(root,text="Your File Is sucessfully submitted \nThanks For Using Our App ",font=('Arial',20)).grid(row=count,columnspan=3,sticky=tk.W)

    except FileNotFoundError:
        messagebox.askretrycancel('Error','Please enter Right Path')
    except PyPDF2.utils.PdfReadError:
        messagebox.askretrycancel('Error','Please make sure your PDF has Decrepted')
    except OSError:
        a=messagebox.askyesnocancel('Warning','Please Restart Your App')
        if a==0:
            return
        if a==1:
            root.quit()
    save_folder_path_var.set('')
    password_var.set('')
    folder_path_var.set("")
submit_button.config(command=select_sabmit_func)
##################### end of Button Functionality #####################

###################3 ending #############################
root.mainloop()