from collections import UserDict


class Field:
    
    def __init__(self, value=None):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value
    
    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a interger')
        self.value = value

class Record(Field):
    
    def __init__(self, name, phone):
        self.name = name
        self.phones = [phone] if phone else []
      
    def change_phone(self, old_phone, new_phone):
        for np, op in enumerate(self.phones):
            if op.value == old_phone.value:
                self.phones[np] = new_phone
        return f"Change {old_phone} to {new_phone}"
    
    def add_phone(self, phone):
        self.phones.append(phone)

    def del_phone(self, phone):
        self.phones.remove(phone)
        
class AdressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record


if __name__ == '__main__':
    
    addressbook = AdressBook()
    
    name = Name('Alex')
    phone = Phone(9999999999)
    
    record1 = Record(name, phone)
    record1.add_phone(Phone(123456))
    print(f"{record1.name} - {record1.phones}")
     
    record2 = Record(Name('Igor'), Phone(9999999990))
    
    addressbook.add_record(record1)
    addressbook.add_record(record2)
 
    record3 = addressbook.get('Alex')

    if record3:
        record3.change_phone(Phone(9999999999), Phone(9999999900))
    
    for record in addressbook.values():
        print(f"{record.name} {record.phones}")

    
    