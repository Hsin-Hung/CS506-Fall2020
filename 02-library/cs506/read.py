
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    ret = []
    with open(csv_file_path, 'r') as file:
        
        lines = file.read().splitlines()

        for row in lines:

            lst = []

            for i in row.split(","):

                try:
                    f = float(i)
                    if f.is_integer():
                        f = int(i)
                    lst.append(f)

                except ValueError:
                    try: 
                        lst.append(i[1:-1])
                    except ValueError:
                        print("ValueError")


            ret.append(lst)
            


    return ret
