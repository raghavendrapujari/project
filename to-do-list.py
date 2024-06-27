from tkinter import *
from tkinter import messagebox
no_of_tasks = 0
def add_task():
    global no_of_tasks
    task = new_task.get().strip()
    if task:
        no_of_tasks += 1
        tasks.insert(END, task)
        new_task.delete(0, END)
        update_listbox_height()
    else:
        messagebox.showwarning(title='WARNING!', message='Enter a task before adding')
def delete_task():
    global no_of_tasks
    selected_task_index = tasks.curselection()
    if selected_task_index:
        tasks.delete(selected_task_index)
        no_of_tasks -= 1
        update_listbox_height()
    else:
        messagebox.showwarning(title='WARNING!', message='Select a task to delete')
def update_listbox_height():
    tasks.config(height=tasks.size())
window = Tk()
window.geometry("900x500")
window.title("TO-DO LIST")
window.config(background='grey')
heading = Label(window,
                text='Enter the task',
                font=('Ubuntu Mono font pairing',25,'bold'),
                bd=2,
                relief=RAISED,
                padx=10,
                pady=10)
new_task = Entry(window,
                 font=('Cambria',25),
                 bd=2,
                 relief='solid')
new_task.place(x=20, y=70)
heading.place(x=20, y=20)
add = Button(window,
             font=('Ubuntu Mono font pairing',15),
             text="ADD",
             command=add_task,
             bd=2,
             relief='solid')
add.place(x=450, y=70)
delete = Button(window,
                font=('Arial',15),
                bd=2,
                text='DELETE',
                relief='solid',
                command=delete_task)
delete.place(x=520, y=70)
tasks = Listbox(window,
                bg='white',
                font=('Lucida Sans',20),
                width=45,
                height=0)
tasks.place(x=20, y=130)

window.mainloop()
