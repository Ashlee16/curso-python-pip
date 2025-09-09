def get_population(territory_dict):
    population_dict = {
        '2022': int(territory_dict['2022 Population']),
        '2020': int(territory_dict['2020 Population']),
        '2015': int(territory_dict['2015 Population']),
        '2010': int(territory_dict['2010 Population']),
        '2000': int(territory_dict['2000 Population']),
        '1990': int(territory_dict['1990 Population']),
        '1980': int(territory_dict['1980 Population']),
        '1970': int(territory_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_territory(data, territory):
    resultado = list(
        filter(lambda item: item['Territory'] == territory, data))
    return resultado
