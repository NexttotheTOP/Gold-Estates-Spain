import requests
import xml.etree.ElementTree as ET
import json

# Fetch the XML data
url = 'https://gold-estates.com/xml/kyero.php?f=660593ba93d69'
response = requests.get(url)
xml_data = response.content

# Parse the XML data
root = ET.fromstring(xml_data)

# Function to extract text content from an element
def get_text(element, default=''):
    return element.text.strip() if element is not None and element.text else default

# Extract information from the XML
properties = []
for item in root.findall('.//property'):
    property_data = {
        'id': get_text(item.find('id')),
        'date': get_text(item.find('date')),
        'ref': get_text(item.find('ref')),
        'price': get_text(item.find('price')),
        'currency': get_text(item.find('currency')),
        'price_freq': get_text(item.find('price_freq')),
        'new_build': get_text(item.find('new_build')),
        'type': get_text(item.find('type')),
        'town': get_text(item.find('town')),
        'province': get_text(item.find('province')),
        'location_detail': get_text(item.find('location_detail')),
        'beds': get_text(item.find('beds')),
        'baths': get_text(item.find('baths')),
        'pool': get_text(item.find('pool')),
        'location': {
            'latitude': get_text(item.find('location/latitude')),
            'longitude': get_text(item.find('location/longitude'))
        },
        'energy_rating': {
            'consumption': get_text(item.find('energy_rating/consumption')),
            'emissions': get_text(item.find('energy_rating/emissions'))
        },
        'surface_area': {
            'built': get_text(item.find('surface_area/built')),
            'plot': get_text(item.find('surface_area/plot'))
        },
        'url': {
            'en': get_text(item.find('url/en')),
            'es': get_text(item.find('url/es')),
            'de': get_text(item.find('url/de')),
            'nl': get_text(item.find('url/nl')),
            'fr': get_text(item.find('url/fr')),
            'da': get_text(item.find('url/da')),
            'ru': get_text(item.find('url/ru'))
        },
        'desc': {
            'en': get_text(item.find('desc/en')),
            'es': get_text(item.find('desc/es')),
            'de': get_text(item.find('desc/de')),
            'nl': get_text(item.find('desc/nl')),
            'fr': get_text(item.find('desc/fr')),
            'da': get_text(item.find('desc/da')),
            'ru': get_text(item.find('desc/ru'))
        },
        'features': [get_text(f) for f in item.findall('features/feature')],
        'images': [get_text(img.find('url')) for img in item.findall('images/image')]
    }
    properties.append(property_data)

# Convert the properties list to JSON
properties_json = json.dumps(properties, indent=4)

# Save the JSON data to a file
with open('properties.json', 'w') as f:
    f.write(properties_json)

print("JSON data has been saved to properties.json")