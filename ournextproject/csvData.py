import csv
import json

def to_text(fname1, fname2):
	with open(fname1, newline='') as csvfile1:
		with open(fname2, 'a', newline='') as textfile:
			reader = csv.reader(csvfile1, delimiter=',')
			next(reader, None)
			for id, name, latitude, longitude in reader:
				try:
					s = '{{from:{{name: \'Columbus\', coordinates: [-83.0007065, 39.9622601]}}, to: {{ name: \'{}\', coordinates: [{}, {}]}}'.format(name, longitude, latitude)
					textfile.write(r'{},'.format(s))
				except AttributeError:
					continue
					
def to_geoJSON(infile):
	'''convert csv to geoJSON'''
	features = []
	with open(infile, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for city, state, latitude, longitude in reader:
		    latitude, longitude = map(float, (latitude, longitude))
		    features.append(
		        Feature(
		            geometry = Point((longitude, latitude)),
		            properties = {
		                'city': city,
		                'state': state
		            }
		        )
		    )

	collection = FeatureCollection(features)
	with open("GeoObs.json", "w") as f:
		f.write('%s' % collection)	
		
		
def csvToJSON(infile, outfile):
    with open(infile, newline='') as csvfile:
        with open(outfile, 'a') as jsonfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for lname, fname, city, county, state, country, lat, lon, agent in reader:
                try:
                    s1 = "\"from\": [-83.0007065, 39.9622601]"	
                    s2 = "\"to\":[{}, {}], \"name\": \"{}, {}\"".format(lon, lat, lname, fname)
                    jsonfile.write(r'{{{},{}}},'.format(s1, s2))
                except AttributeError:
                    continue
	
def csvToJSONChart(infile, outfile):
	j = []
	i = 0
	with open(infile, newline='') as csvfile:
		with open(outfile, 'a') as jsonfile:
			reader = csv.reader(csvfile, delimiter=',')
			next(reader, None)
			for cat, freq in reader:
				if(freq == ''):
					continue
				else:
					try:
						s = "{{\"x\":{}, \"y\": \"{}\"}}".format(freq, cat)
						jsonfile.write(r'{},'.format(s))
						i += 1
					except AttributeError:
						continue
			
def csvToIssue(textFile, infile, outfile):
    with open(textFile) as tfile:
        with open(infile, newline='') as csvfile:
            with open(outfile, 'a') as jsonfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader, None)
                date = []
                i = 0
                for line in tfile:
                    date.append(line)
                for city, state, lat, lon, country, fname, lname, agentType in reader:
                    try:
                        s = '{{"lastName":\"{}\", "firstName":\"{}\", "agentType":\"{}\", "city":\"{}\", "state":\"{}\", "country": \"{}\", "lat":{}, "lon":{}, "pubDate":[{}]}}'.format(lname, 
                        fname, agentType, city, state, country, lat, lon, date[i] )
                        jsonfile.write(r'{},'.format(s))
                        i += 1
                    except AttributeError:
                        continue
def subToJSON(infile, outfile):
    with open(infile, newline='') as csvfile:
        with open(outfile, 'a') as jsonfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for fname, lname, cost, pubDate in reader:
                try:
                    s = '{{"lastName":\"{}\", "firstName":\"{}\", "amount":\"{}\", "pubDate":\"{}\"}}'.format(lname, fname, cost, pubDate)	
                    
                    jsonfile.write(r'{},'.format(s))
                except AttributeError:
                    continue
            
def pubToJSON(infile, outfile):
    with open(infile, newline='') as csvfile:
        with open(outfile, 'a') as jsonfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for pub, loc, ethnic, lat, lon in reader:
                try:
                    s = '{{"newspaper":\"{}\", "location":\"{}\", "ethnicPeriodical":\"{}\", "lat":{}, "lon":{}}}'.format(pub, loc, ethnic, lat, lon)	
                    
                    jsonfile.write(r'{},'.format(s))
                except AttributeError:
                    continue

def subToChart(infile, outfile):
    with open(infile, newline='') as csvfile:
        with open(outfile, 'a') as jsonfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)
            for cat, freq in reader:
                try:
                    #name = '{}, {}'.format(lname, fname)
                    s = "{{\"x\":{}, \"y\": \"{}\"}}".format(freq, cat)
                    jsonfile.write(r'{},'.format(s))
                except AttributeError:
                    continue


                    
if __name__=="__main__":

	fname = 'qp_aa.csv'
	textname = 'qp_aa.json'
	pubToJSON(fname, textname)
	
	
	
	
	
	
	
	
	
	
	
