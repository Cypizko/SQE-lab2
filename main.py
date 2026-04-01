import tkinter as tk

def add():
    raw_task = entry.get()
    truncated_task = raw_task[:5] 
    
    listbox.insert(tk.END, truncated_task)

def delete():
    listbox.delete(0)

def save():
    tasks = listbox.get(0, tk.END)
    for t in tasks:
        with open("tasks.txt", "w", encoding="utf-8") as f:
            f.write(t + "\n")

root = tk.Tk()
root.title("To-Do12")

root.geometry("250x300")

entry = tk.Entry(root)
entry.pack(fill="x")

btn_add = tk.Button(root, text="Додати завдання", command=add, bg="lightgreen")
btn_add.pack(fill="x")

btn_delete = tk.Button(root, text="Видалити вибране", command=delete, bg="lightblue")
btn_delete.pack(fill="x")

btn_save = tk.Button(root, text="Зберегти у файл", command=save, bg="lightgrey")
btn_save.pack(fill="x")

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True)

root.mainloop()
