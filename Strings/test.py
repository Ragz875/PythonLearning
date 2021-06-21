from fuzzywuzzy import fuzz
string = "geeks for, geeks geeks geeks geeks"
new_string=''
for word in string.split():
    new_string+=' ' + word
print('Original:\n',string)
print('new String: \n',new_string.lstrip())
print(fuzz.ratio('Mapbox Inc', 'Mapbox'))
print(fuzz.partial_ratio('Mapbox Inc', 'Mapbox'))
print(fuzz.partial_ratio('San Francisco, CA 94404', 'San Francisco, CA'))

