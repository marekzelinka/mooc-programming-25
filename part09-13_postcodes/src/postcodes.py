class City:
    postcodes: dict[str, str] = {
        "Helsinki": "00100",
        "Turku": "20100",
        "Tampere": "33100",
        "Rovaniemi": "96100",
        "Oulu": "90100",
    }

    def __init__(self, name: str, population: int, postcode: str | None = None):
        self.__name = name
        self.__population = population
        self.postcode = postcode

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @property
    def postcode(self) -> str | None:
        return self.__postcode

    @postcode.setter
    def postcode(self, postcode: str | None) -> None:
        if not postcode:
            self.__postcode = None

            return

        postcode = City.postcodes[postcode]

        if not postcode:
            raise ValueError(
                f"Postcode is not on the list, available options are {', '.join(City.postcodes.keys())}"
            )

        self.__postcode = postcode

    def __str__(self):
        return f"{self.__name} ({self.__population} residents.)"
