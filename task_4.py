from colorama import Style, Fore
from contact_agent import (
    add_contact, 
    update_contact, 
    show_contact, 
    show_all,
    parse_input)


def  hello (name, phone):
    print(f"{Fore.LIGHTCYAN_EX}How can I help you?")


handlers = {
    "hello": hello,
    "add": add_contact,
    "change": update_contact,
    "all": show_all,
    "phone": show_contact,
}

printers = {
    "greetings": lambda: print(f"{Fore.MAGENTA}Welcome to the assistant bot!"),
    "enter": lambda: f"{Fore.LIGHTCYAN_EX}Enter the command: {Fore.LIGHTGREEN_EX}",
    "add": lambda: print(f"{Fore.BLUE}Contact added"),
    "change": lambda: print(f"{Fore.BLUE}Contact updated"),
    "exit": lambda: print(f"{Fore.BLUE}Good bye")
}

def create_print_error(message):
    return lambda: print(f"{Fore.RED}Error: {Style.RESET_ALL} {message}")
errors = {
    "add": create_print_error("'add' command should be: add <name> <phone>"),
    "change": create_print_error("'change' command should be: add <name> <phone>"),
    "show_contact": create_print_error("'phone' command should be: phone <name>"),
}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            decorated = input_error(func)
            func(*args, **kwargs)
        except Exception as e:
            errors[str(e)]()
            decorated(resume = True)
    return inner


@input_error
def main(resume = False):
    if not resume:
        printers["greetings"]()
    while True:
        answer = input(printers["enter"]())
        parsed_answer = parse_input(answer)

        command = parsed_answer.group("command").lower()
        name = parsed_answer.group("name")
        phone = parsed_answer.group("phone")
        
        handler = handlers.get(command)
        if handler:
            handler(name, phone)
            printer = printers.get(command)
            if printer:
                printer()
        elif command in ("exit", "close"):
            printers["exit"]()
            break
        else:
            print(f"{Fore.YELLOW}Invalid command")

if __name__ == "__main__":
    main()