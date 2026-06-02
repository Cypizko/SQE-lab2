import pytest
import tkinter as tk

def add_task(entry, listbox):
    raw_task = entry.get()
    listbox.insert(tk.END, raw_task)

def test_add_task_validation_failure():
    root = tk.Tk()
    entry = tk.Entry(root)
    listbox = tk.Listbox(root)
    
    entry.insert(0, "Купити хліб")
    add_task(entry, listbox)
    
    assert listbox.get(0) == "Помити машину"
    
    root.destroy()