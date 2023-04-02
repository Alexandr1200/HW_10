from Field1 import AddressBook, Record, Name, Phone


addressbook = AddressBook()


def add_record(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    record = Record(name, phone)
    addressbook.add_record(record)
    return f"Name {name} add successful"


def main():
    while True:
        user_input = input(">>>")
        
        if user_input.startswith("add"):
            name, phone = user_input.replace("add", '').strip().split()
            print(add_record(name, phone))

        elif user_input != "exit":
            print("Unknown command, try again")
            
        if user_input.startswith("exit"):
            print("Bye")
            break
        

if __name__ == '__main__':

    main()
    for record in addressbook.values():
        print(f"{record.name} - {record.phone}")