def transform(obj):
    vector = list()

    # Count the special symbol in subject
    vector.append(len(re.findall("[^a-zA-z0-9]", obj["Subject"])))
    # Mail To amount
    vector.append(len(obj["To"]))
    # Time of deliver(a day)
    vector.append(obj["Date"].hour*60+obj["Date"].minute)
    # "http://" in the content
    vector.append(obj["Content"].count("http://"))
    # Whether has geography information
    vector.append(obj["geoip"]["longitude"])
