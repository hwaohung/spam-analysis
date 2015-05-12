import csv, json, time

from utility.transform import *
from utility.request import *


output_filename = "features"


def main():
    doc_type = "logs"
    fp = open(output_filename+".csv", 'w')
    csv_writer = csv.writer(fp, delimiter=',')

    cost = time.time()
    for index in get_all_indexes():
        for row in get_all_rows(index, doc_type):
            #print json.dumps(row, indent=1)
            #print "============================================="
            #print "============================================="
            csv_writer.writerow(transform(row))

    print "Attribute matrix complete!"
    print "Cost: {0}".format(time.time()-cost)

    fp.close()
    

if __name__ == "__main__":
    main()
