from collections import UserDict


class Core:
    
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

class Name(Core):
    pass

class Phone(Core):
    pass

class Record:
    
    def __init__(self, name:Name, phone:Phone):
        self.name = name
        self.phone = phone
      
    def change_phone(self, new_phone):
        old_phone = self.phone
        self.phone = new_phone
        return f"Change {old_phone} to {new_phone}"
        
class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record


if __name__ == '__main__':
    
    addressbook = AddressBook()
    
    name = Name("Alex")
    phone = Phone("9999999999")
    
    record1 = Record(name, phone)
    
    print(f"{record1.name} - {record1.phone}")
     
    record2 = Record(Name('Igor'), Phone("9999999990"))
    
    addressbook.add_record(record1)
    addressbook.add_record(record2)
 
    record3 = addressbook.get('Alex')

    if record3:
        record3.change_phone(Phone('9999999900'))
    
    for record in addressbook.values():
        print(f"{record.name} {record.phone}")
    