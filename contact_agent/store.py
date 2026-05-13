
store = {}

def get_store ():
    global store
    return store

def set_store (name: str, phone: str):
    global store
    store[name] = phone
