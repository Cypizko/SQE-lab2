import pytest
import tkinter as tk

def add_task(entry, listbox):
    raw_task = entry.get()
    listbox.insert(tk.END, raw_task)

@pytest.fixture
def app_widgets():
    root = tk.Tk()
    entry = tk.Entry(root)
    listbox = tk.Listbox(root)
    
    yield entry, listbox
    

    root.destroy()

@pytest.mark.parametrize("task_text", [
    "Купити молоко", 
    "Скласти лабораторну №6", 
    "12345", 
    "Текст_із_символами!@#"
])
def test_add_task_parametrized(app_widgets, task_text):
    entry, listbox = app_widgets
    
    entry.insert(0, task_text)
    add_task(entry, listbox)
    
    assert listbox.get(0) == task_text