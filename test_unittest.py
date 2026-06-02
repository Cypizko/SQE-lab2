import unittest
import tkinter as tk

def add_task(entry, listbox):
    raw_task = entry.get()
    listbox.insert(tk.END, raw_task)

def delete_task(listbox):
    selected_indices = listbox.curselection()
    if selected_indices:
        listbox.delete(selected_indices[0])

class TestToDoApp(unittest.TestCase):
    
    def setUp(self):
        self.root = tk.Tk()
        self.entry = tk.Entry(self.root)
        self.listbox = tk.Listbox(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_add_task(self):
        self.entry.insert(0, "Прочитати книгу")
        add_task(self.entry, self.listbox)
        
        self.assertEqual(self.listbox.size(), 1)
        self.assertEqual(self.listbox.get(0), "Прочитати книгу")

    def test_delete_task(self):
        self.listbox.insert(tk.END, "Завдання 1")
        self.listbox.insert(tk.END, "Завдання 2")
        
        self.listbox.selection_set(1)
        delete_task(self.listbox)
        
        self.assertEqual(self.listbox.size(), 1)
        self.assertEqual(self.listbox.get(0), "Завдання 1")

if __name__ == "__main__":
    unittest.main()