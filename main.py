import tkinter as tk

def add():
    raw_task = entry.get()
    listbox.insert(tk.END, raw_task)

def delete():
    selected_indices = listbox.curselection()
    if selected_indices:
        listbox.delete(selected_indices[0])

def save():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w", encoding="utf-8") as f:
        for t in tasks:
            f.write(t + "\n")

root = tk.Tk()
root.title("To-Do12")

root.geometry("250x300")

entry = tk.Entry(root)
entry.pack(fill="x", padx=10, pady=5)


btn_add = tk.Button(root, text="Додати завдання", command=add, bg="#2ecc71", fg="black", font=("Arial", 10, "bold"))
btn_add.pack(fill="x", padx=10, pady=5)


btn_delete = tk.Button(root, text="Видалити вибране", command=delete, bg="#e74c3c", fg="black", font=("Arial", 10))
btn_delete.pack(fill="x", padx=10, pady=5)


btn_save = tk.Button(root, text="Зберегти у файл", command=save, bg="#bdc3c7", fg="black", font=("Arial", 10))
btn_save.pack(fill="x", padx=10, pady=5)

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()
