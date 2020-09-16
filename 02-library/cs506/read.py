
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    ret = []
    with open(csv_file_path, 'r') as file:
        
        lines = file.read().splitlines()

        for row in lines:
            ret.append([int(i) if i.isnumeric() else i[1:-1] for i in row.split(",")])


    return ret
