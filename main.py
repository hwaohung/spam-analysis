import csv, json, time

from utility.transform import *
from utility.request import *


output_filename = "features"


def main():
    doc_type = "logs"

    cost = time.time()
    transformer = Transformer(output_filename)
    for index in get_all_indexes():
        for rows in get_all_rows(index, doc_type, offset=0, limit=1000):
            transformer.extend(rows)
            #print json.dumps(row, indent=1)
            #print "============================================="
            #print "============================================="
            
    transformer.normalize()

    print "Attribute convert complete!"
    print "Cost: {0}".format(time.time()-cost)
    transformer.report()
    transformer.close()
    

if __name__ == "__main__":
    main()
