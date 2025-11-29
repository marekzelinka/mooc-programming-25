import string


class PhoneNumber:
    country_codes: dict[str, str] = {
        "Denmark": "+45",
        "Sweden": "+46",
        "Norway": "+47",
        "Finland": "+358",
    }

    def __init__(
        self, name: str, phone_number: str, country_code: str | None = None
    ) -> None:
        self.name: str = name

        # The following two calls are to @property.setter
        self.phone_number = phone_number
        self.country_code = country_code

    @property
    def phone_number(self) -> str:
        """
        When the country code prefix is added
        the initial zero is removed from the phone number
        """

        if not self.country_code:
            return self.__phone_number

        return (
            f"{PhoneNumber.country_codes[self.country_code]} {self.__phone_number[1:]}"
        )

    @phone_number.setter
    def phone_number(self, number: str) -> None:
        for char in number:
            if char not in string.digits + " ":
                raise ValueError("Phone number can only contain numbers and spaces")

        self.__phone_number = number

    @property
    def local_number(self) -> str:
        return self.__phone_number

    @property
    def country_code(self) -> str | None:
        return self.__country_code

    @country_code.setter
    def country_code(self, country_code: str | None) -> None:
        if not country_code:
            self.__country_code = None
            return

        if country_code not in PhoneNumber.country_codes:
            raise ValueError(
                f"Country code is not on the list. Available options are: {', '.join(PhoneNumber.country_codes.keys())}"
            )

        self.__country_code = country_code

    def __str__(self) -> str:
        return f"{self.phone_number} ({self.name})"


if __name__ == "__main__":
    firend = PhoneNumber("Peter Pythons", "040 111 1111", "Sweden")
    print(firend)  # +46 40 111 1111 (Peter Pythons)
    print(firend.phone_number)  # +46 40 111 1111
    print(firend.local_number)  # 040 111 1111
    print()
    best_firend = PhoneNumber("Jonas Javos", "050 1234 567")
    print(best_firend)  # 050 1234 567 (Peter Pythons)
    print(best_firend.phone_number)  # 050 1234 567
    print(best_firend.local_number)  # 050 1234 567
