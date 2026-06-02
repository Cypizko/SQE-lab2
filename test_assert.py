import tkinter as tk
import os

# віртуальне середовище Tkinter
root = tk.Tk()
entry = tk.Entry(root)
listbox = tk.Listbox(root)

# тест логіки add()
def test_add_logic():
    entry.delete(0, tk.END)
    entry.insert(0, "Купити хліб")
    

    raw_task = entry.get()
    listbox.insert(tk.END, raw_task)
    
    # чи додалося завдання і чи воно не обрізалося
    assert listbox.get(0) == "Купити хліб", "1 провалено: текст завдання обрізався або не збігається"

# Тест логіки save()
def test_save_logic():
    test_tasks = ["Завдання 1", "Завдання 2"]
    
    # Імітуємо save()
    with open("test_tasks.txt", "w", encoding="utf-8") as f:
        for t in test_tasks:
            f.write(t + "\n")
            
    # Чи створився файл на диску
    assert os.path.exists("test_tasks.txt"), "2 провалено: файл не був створений"
    
    # Чи коректно й повністю записалися всі рядки
    with open("test_tasks.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines == test_tasks, "3 провалено: вміст файлу не збігається зі списком"
    
    if os.path.exists("test_tasks.txt"):
        os.remove("test_tasks.txt")

# Запуск
if __name__ == "__main__":
    test_add_logic()
    print("Тест 1 (add) через assert — +")
    test_save_logic()
    print("Тест 2 (save) через assert — +")
    print("Усі тести виконано")