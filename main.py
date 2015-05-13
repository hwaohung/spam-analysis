import csv, json, time

from utility.transform import *
from utility.request import *


output_filename = "features"


def main():
    doc_type = "logs"
    fp = open(output_filename+".csv", 'w')
    csv_writer = csv.writer(fp, delimiter=',')

    cost = time.time()
    transformer = Transformer()
    for index in get_all_indexes():
        for rows in get_all_rows(index, doc_type):
            transformer.extend(rows)
            #print json.dumps(row, indent=1)
            #print "============================================="
            #print "============================================="
            

    transformer.normalize()
    csv_writer.writerows(transformer.get_all_rows())

    print "Attribute matrix complete!"
    print "Cost: {0}".format(time.time()-cost)

    fp.close()
    

if __name__ == "__main__":
    main()
