import pytest
import tkinter as tk

def delete_task(listbox):
    selected_indices = listbox.curselection()
    if selected_indices:
        listbox.delete(selected_indices[0])

def test_delete_raises_attribute_error():
    with pytest.raises(AttributeError):
        delete_task(None)