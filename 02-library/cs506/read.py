import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    ret = []
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ret.append([int(i) if i.isnumeric() else i for i in row])


    return ret
