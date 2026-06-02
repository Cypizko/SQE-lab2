import pytest


@pytest.mark.xfail(reason="Відомий дефект: функція видалення некоректно обробляє порожні списки")
def test_delete_from_empty_listbox():
    is_listbox_empty = True
    assert is_listbox_empty == False