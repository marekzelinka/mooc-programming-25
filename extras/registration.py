import string


class Registration:
    def __init__(self, owner: str, make: str, year: str, license_plate: str) -> None:
        self.__owner: str = owner
        self.__make: str = make
        self.__year: str = year
        self.license_plate = license_plate

    @property
    def license_plate(self) -> str:
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, plate: str) -> None:
        self.__license_plate = plate

    @classmethod
    def license_plate_valid(cls, plate: str) -> bool:
        if len(plate) < 3 or "-" not in plate:
            return False

        # Chcek the beginning and end sections of the plate separately
        letters, numbers = plate.split("-")

        # hte beginning section can have only letters
        for char in letters:
            if char.lower() not in string.ascii_lowercase + "åäö":
                return False

        # the end section can have only numbers
        for char in numbers:
            if char not in string.digits:
                return False

        return True


if __name__ == "__main__":
    registration = Registration("Mary Motorist", "Volvo", "1992", "abc-123")

    if Registration.license_plate_valid("xyz-789"):
        print("This is a valid license plate!")
