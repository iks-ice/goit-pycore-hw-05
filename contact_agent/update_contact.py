from .store import set_store


def update_contact(name: str, phone: str):
    set_store(name,  phone)