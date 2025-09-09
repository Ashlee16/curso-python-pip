import csv


def read_csv(path):  # PATH => Ubicación del archivo
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            # Unirá los 2 elementos en un array de tuplas: Header - row
            iterable = zip(header, row)
            territory_dict = {key: value for key, value in iterable}
            data.append(territory_dict)
        return data


if __name__ == "__main__":
    data = read_csv('./App/data.csv')
    print(data[2])
