from .store import set_store


def add_contact(name: str, phone: str):
    if not all((name, phone)):
        raise Exception("add")
    set_store(name, phone)