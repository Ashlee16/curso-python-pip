import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('data.csv')
    data = list(
    filter(lambda item: item['Continent'] == 'South America', data))

    territories = list(map(lambda x: x['Territory'], data))
    percentages = list(map(lambda x: float(x['World Population Percentage']), data))
    charts.generate_pie_chart(territories, percentages)


    territory = input("Elija el país => ")
    print(territory)

    result = utils.population_by_territory(data, territory)

    if len(result) > 0:
        territory = result[0]
        print(territory)
        labels, values = utils.get_population(territory)
        charts.generate_bar_chart(territory['Territory'], labels, values)
        


if __name__ == "__main__":
    run()
