import csv
def lat_lng(location):
    import csv
    with open("Lat-Long.txt", "r") as csv_file:
        ltlng_data = list(csv.reader(csv_file))
        #City = []
        #State = []
        Location = []
        Latitude = []
        Longitude = []
        for row in ltlng_data[1:]:
            #City.append(row[1])
            #State.append(row[2])
            Location.append(row[1] + ', ' + row[2])
            Latitude.append(row[3])
            Longitude.append(row[4])
        for idx, value in enumerate(Location):
            if value == location:
                lat = Latitude[idx]
                long = Longitude[idx]
                Lat_Long = [lat, long]
                break
            else:
                pass
        return Lat_Long



        
            
            



