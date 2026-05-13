from .store import get_store
from colorama import Fore

def show_contact(name: str, phone = None):
    if name is None:
        raise Exception("show_contact")
    
    store = get_store()
    phone = store.get(name)
    if phone:
        print(f"{Fore.GREEN}{phone}")
    else:
        print(f"{Fore.YELLOW}No such a contact")

def show_all(name = None, phone = None):
    store = get_store()
    if store == {}:
        print(f"{Fore.YELLOW}No contacts")
        return

    for name, phone in store.items():
        print(f"{name}    {phone}")