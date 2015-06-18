import re, copy, csv, os, io


class Transformer:
    def __init__(self, name="temp"):
        self.name = name
        self.fp = io.open(name+".temp", 'w', buffering=4096)

        self.row_count = 0
        self.max_values = [0, 0, 0, 0, 0]
        self.fail_times = [0, 0, 0, 0, 0]

    def report(self):
        print "Total rows: {0}\n".format(self.row_count)
        
        print "Attribute convert fail times"
        print "============================"
        attributes = ["Subject", "To", "Time", "Link", "Longtitude"]
        for i in range(len(attributes)):
            print "{0}: {1}".format(attributes[i], self.fail_times[i])

        print "============================"
 
    # Add more than one obj at once 
    def extend(self, objs):
        print "Current rows: {0}".format(self.row_count)
        for obj in objs:
            self.add(obj)
        
    # Convert the obj to attribute vector and add to self.rows
    def add(self, obj):
        vector = list()
    
        # Count the special symbol in subject
        vector.append(self.get_subject(obj))
        # Mail To amount
        vector.append(self.get_to(obj))
        # Time of deliver(a day)
        vector.append(self.get_time(obj))
        # "http://" in the content
        vector.append(self.get_link(obj))
        # Whether has geography information
        vector.append(self.get_longitude(obj))
    
        self.row_count += 1
        vector = (str(e) for e in vector)
        #self.csv_writer.writerow(vector)
        self.fp.write(unicode(" ".join(vector)+'\n'))

    # Normal each axis value to same scale
    def normalize(self):
        # Close the writer
        self.fp.close()

        old_name = self.fp.name
        records = [list() for i in range(5)]
        # Load all valid values of each feature
        with io.open(old_name, 'r') as fp:
            csv_reader = csv.reader(fp, delimiter=' ')
            # All values list
            for row in csv_reader:
                for i in range(5):
                    if row[i] >= 0.0: records[i].append(row[i])

        # Get the median, max value of each feature
        medians = list()
        maxs = list()
        for i in range(5):
            reocrds[i] = sorted(reocrds[i])
            medians.append(records[i][len(records[i])/2])
            maxs.append(reocrds[i][-1])
            print "{0} => Median: {1}, Max: {2}".format(i, medians[i], maxs[i])

        del reocrds

        # Write out the final result
        with io.open(self.name+".csv", 'w') as self.fp:
            with io.open(old_name, 'r') as fp:
                csv_reader = csv.reader(fp, delimiter=' ')
                for row in csv_reader:
                    for i in range(len(row)):
                        if row[i] >= 0:
                            # Normalized value
                            row[i] = str(float(row[i]) / maxs[i])
                        else:
                            # Normalized median value for missing value
                            row[i] = str(medians[i]/maxs[i])

                    self.fp.write(unicode(" ".join(row)+'\n'))
        os.system("rm {0}".format(old_name))
   
    def get_subject(self, obj):
        if obj.has_key("Subject"):
            return len(re.findall("[^a-zA-z0-9]", obj["Subject"]))
    
        else:
            self.fail_times[0] += 1
            return -1
    
    def get_to(self, obj):
        times = 0
        to = 0

        if obj.has_key("To"):
            times += 1
            to += len(obj["To"])
        if obj.has_key("CC"):
            times += 1
            to += len(obj["CC"])
        if obj.has_key("BCC"):
            times += 1
            to += len(obj["BCC"])
    
        if times < 3: self.fail_times[1] += 1
        if times == 0: return -1.0

        return to
    
    def get_time(self, obj):
        if obj.has_key("Date"):
            flags = obj["Date"].split(' ')
            hour, minute = flags[3].split(':')[:2]
            return (60*int(hour) + int(minute))
    
        else:
            self.fail_times[2] += 1
            return -1.0
    
    def get_link(self, obj):
        if obj.has_key("link_count"):
            return len(obj["link_count"])
    
        else:
            self.fail_times[3] += 1
            return -1.0
    
    def get_longitude(self, obj):
        if obj.has_key("geoip"):
            # Range 360 ~ 0
            return obj["geoip"]["longitude"] + 180.0
    
        else: 
            self.fail_times[4] += 1
            return -1.0
