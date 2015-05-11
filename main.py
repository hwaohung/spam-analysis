import csv

from transfrom import *
from request import *


output_filename = "features"


def main():
    doc_type = "logs"
    fp = open(output_filename, 'w')
    csv_writer = csv.writer(fp, delimiter=',')

    for index in get_all_indexes():
        for row in get_all_rows(index, doc_type):
            csv_writer.writerow(row)

    fp.close()
    

if __name__ == "__main__":
    main()
