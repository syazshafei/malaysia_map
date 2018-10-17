# Add a new Country

1. You need shapefiles why contains data of your map. You can get this file in this site : http://www.diva-gis.org/gdata or https://gadm.org/download_country_v3.html

2. You need to add ISO 3166-2 with column name ISO for all record in your file. It’s important because, it’s a normal for mapping your data with geojson file. Refer to this link : https://en.wikipedia.org/wiki/ISO_3166-2:MY

3. You need to convert shapefile to geojson file. This action can make with ogr2ogr tools : http://www.gdal.org/ogr2ogr.htm
Or use this command : *ogr2ogr -f GeoJSON -t_srs crs:84 [name].geojson [name].shp*

4. Put your geojson file in next folder : */superset/assets/src/visualizations/countries* with the next name : *nameofyourcountries.geojson*

5. You can to reduce size of geojson file on this site : http://mapshaper.org/

6. Go in file *superset/assets/src/explore/controls.jsx*

Add your country in component ‘select_country’ Example : add ‘Malaysia’
```
select_country: {
    type: 'SelectControl',
    label: 'Country Name Type',
    default: 'France',
    choices: [
    'Belgium',
    'Brazil',
    'China',
    'Egypt',
    'France',
    'Germany',
    'Italy',
    'Malaysia',
    'Morocco',
    'Netherlands',
    'Russia',
    'Singapore',
    'Spain',
    'Uk',
    'Usa',
    ].map(s => [s, s]),
    description: 'The name of country that Superset should display',
