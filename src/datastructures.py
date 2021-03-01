from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky numbers" : [7,13,22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
             "age": 35,
            "lucky numbers" : [10,14,3]   
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
             "age": 5,
            "lucky numbers" : [1]   
        }]

    def _generateId(self):
        return randint(0, 99999999)

    def add_members(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        eliminado = False
        for member in self._members:
            if member["id"]== id:
                self._members.remove(member)
                eliminado = True
        return eliminado

    def update_member(self, id, member):
        modificado = False
        for x in self._members:
            if  x["id"] == id:
                x.update(member)
                modificado = True
        return modificado

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    
    def get_all_members(self):
        return self._members
