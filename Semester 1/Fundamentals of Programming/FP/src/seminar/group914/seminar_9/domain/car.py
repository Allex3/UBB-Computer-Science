class Car(object):
    # class names should start with uppercase letter
    def __init__(self, car_id: int, license_plate: str, model: str):
        self.__id = car_id
        self.__license_plate = license_plate
        self.__model = model

    # let's use properties as setters/getters
    # suppose we want to read the id but we don't want to change it
    #  => in this case we make a read-only property

    @property
    def id(self):
        return self.__id

    @property
    def license(self):
        return self.__license_plate

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value: str):
        self.__model = new_value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id} - {self.license} - {self.model}"


def test_car():
    new_car = Car(100, "CJ 01 ABC", "Dacia Sandero")
    assert new_car.id == "CJ 01 ABC"
    assert new_car.model == "Dacia Sandero"


if __name__ == "__main__":
    cary = Car(100, "CJ 99 ABC", "Toyota Supra")
    print(cary)
