class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int) -> None:
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth


def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    return Pet(name, species, year_of_birth)


if __name__ == "__init__":
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)  # Fluffy
    print(fluffy.species)  # dog
    print(fluffy.year_of_birth)  # 2017
