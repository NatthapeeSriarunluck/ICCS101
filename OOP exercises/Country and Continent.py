class Country:
    def __init__(self, name: str, population: int, area: int):
        self._name = name
        self._population = population
        self._area = area

    def is_larger(self, other):
        return self._area > other._area

    def population_density(self):
        return self._population / self._area

    def __str__(self):
        return f'{self._name} has a population of {self._population} and is {self._area} square km.'

    def __repr__(self):
        return f"Country('{self._name}',{self._population},{self._area}"


class Continent:
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        total = 0
        for country in self.countries:
            total += country.population
        return total

    def __str__(self):
        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)
        return res


canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
mexico = Country('Mexico', 112336538, 1943950)

countries = [canada, usa, mexico]
north_america = Continent('North America', countries)

print(north_america)