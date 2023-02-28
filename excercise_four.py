class Country:
    def __init__(self, country_name: str, population: int, sq_km: int) -> "Country":
        self.country_name = country_name
        self.population = population
        self.sq_km = sq_km

    def is_big(self) -> bool:
        if self.population > 20000000 and self.sq_km > 3000000:
            status = True
        else:
            status = False
        return status
    
    def compare_pd(self, second: "Country") -> None:
        if (self.population / self.sq_km) < (second.population /second.sq_km):
            print(f"{self.country_name} has larger population density than {second.country_name}")
        else:
            print(f"{second.country_name} has larger population density than {self.country_name}")
    

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)


andorra.compare_pd(australia)