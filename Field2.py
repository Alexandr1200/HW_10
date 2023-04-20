from Field1 import AdressBook, Record, Name, Phone


adressbook = AdressBook()

contacts = {'Alina': ['+290424'],
            'Ira': ['+3425590', '+15305383'],
            'Vitalina': ['+14293798']}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Something wrong. Type help.'
    return inner

@input_error
def list_of_params(*args):
    conteiner = args[0].split()
    if not conteiner:
        raise IndexError
    return conteiner

def help(*args):
    return """
Show all contacts >> input show_all
Add new contact >>>> input add
Get contact >>>>>>>> input phone (Name)
Change number >>>>>> input change_contact (Name) (current number) (new number)
Remove contact >>>>> input remove (Name)
For exit ----------- enter exit
"""

def hello(*args):
    return 'For information - input help'

@input_error
def add(*args):
    lst = list_of_params(*args)
    if len(lst) == 2:
        name = Name(lst[0])
        numb_of_phone = Phone(int(lst[1]))
        new_contact = Record(name, numb_of_phone)
        adressbook.add_record(new_contact)
    else:
        raise IndexError


def exit(*args):
    return 'Bye'

def no_command(*args):
    return 'Unknown command. Try again'

def show_all(*args):
    return '\n'.join([f'{k}: {v.phones}' for k, v in adressbook.items()])

@input_error
def get_number(*args):
    lst = list_of_params(*args)
    for k, v in adressbook.items():
        if lst[0] == k:
            return f'{lst[0]}: {v.phones}'
    return f'Not contacts {lst[0]}'

@input_error
def change_contact(*args):
    lst = list_of_params(*args)
    if len(lst) == 2:
        for k, v in adressbook.items():
            if k == lst[0]:
                contact = Record(Name[k], Phone(int(lst[1])))
                adressbook.update({contact.name.value: contact})
        return f'Contact {lst[0]} changed'
    else:
        raise IndexError

def remove_contact(self, name):
    self.data.pop(name)

COMMANDS = {help: 'help',
            add: 'add',
            exit: 'exit',
            show_all: 'show_all',
            get_number: 'phone',
            change_contact: 'change_contact',
            remove_contact: 'remove',
            hello: 'hello'}


def command_handler(text: str):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None

def main():
    while True:

        user_input = input('>>> ')
        if user_input in ('good bye', 'close', 'exit'):
            print(exit())
            break
        command, data = command_handler(user_input)
        print(command(data))

if __name__ == '__main__':

    main()