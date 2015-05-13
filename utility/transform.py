import re, copy


class Transformer:
    def __init__(self):
        self.rows = list()
        self.max_values = [0, 0, 0, 0, 0]
    

    def extend(self, objs):
        for obj in objs:
            self.add(obj)

    # Convert the obj to attribute vector and add to self.rows
    def add(self, obj):
        vector = list()
    
        # Count the special symbol in subject
        vector.append(get_subject(obj))
        # Mail To amount
        vector.append(get_to(obj))
        # Time of deliver(a day)
        vector.append(get_time(obj))
        # "http://" in the content
        vector.append(get_link(obj))
        # Whether has geography information
        vector.append(get_longitude(obj))
    
        #print vector

        # Keep the max value of each axis
        for i in range(len(vector)):
            if vector[i] > self.max_values[i]:
                self.max_values[i] = vector[i]
        
        self.rows.append(vector)

    # Normal each axis value to same scale
    def normalize(self):
        for row in self.rows:
            for i in range(len(row)):
                row[i] /= self.max_values[i]
   
    # Get all attribute vectors, and also can re-weight some attributes(optional)
    def get_all_rows(self, weights=None):
        rows = copy.deepcopy(self.rows)
        if weights is not None:
            for row in rows:
                for i in range(len(weights)):
                    row[i] *= weights[i]

        return rows


def get_subject(obj):
    if obj.has_key("Subject"):
        return len(re.findall("[^a-zA-z0-9]", obj["Subject"]))

    else: return 0


def get_to(obj):
    if obj.has_key("To"):
        return len(obj["To"])

    else: return 1


def get_time(obj):
    if obj.has_key("Date"):
        flags = obj["Date"].split(' ')
        hour, minute = flags[3].split(':')[:2]
        return (60*int(hour) + int(minute))

    else: return 1200


def get_link(obj):
    if obj.has_key("Content")
        return obj["Content"].count("http://")

    else: return 0


def get_longitude(obj):
    if obj.has_key("geoip"):
        # Range 360 ~ 0
        return obj["geoip"]["longitude"] + 180.0

    else: return 180.0
