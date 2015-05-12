import re


def transform(obj):
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
    return vector


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
    return obj["Content"].count("http://")


def get_longitude(obj):
    if obj.has_key("geoip"):
        return obj["geoip"]["longitude"]

    else: return 0.0
