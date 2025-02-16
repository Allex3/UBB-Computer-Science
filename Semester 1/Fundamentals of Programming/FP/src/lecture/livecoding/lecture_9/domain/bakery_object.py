class BakeryObject(object):  # a class is by default derived from Python's object class
    def __init__(self, object_id: int, name: str):
        self.__id = object_id
        self._name = name

    # id is a read-only property (it has no setter)
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value: str):
        # NOTE We can add proper validation here
        self._name = new_value

    def __str__(self):
        # super() - goes to the base class of this
        # return super().__str__() + "abcd"
        return f"Bakery object id={self.id} is {self.name}"
