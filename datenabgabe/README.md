```
java -jar /Users/stefan/apps/ili2pg-4.3.0/ili2pg-4.3.0.jar \
--dbhost 192.168.50.8 --dbport 5432 --dbdatabase pub --dbusr ddluser --dbpwd ddluser \
--dbschema av_lidar_2019 --models SO_AGI_Lidarprodukte_Publikation_20180202 \
--defaultSrsCode 2056 --createGeomIdx --createFk --createFkIdx --createEnumTabs --beautifyEnumDispName --createMetaInfo --createNumChecks --nameByTopic --strokeArcs --sqlEnableNull \
--schemaimport

java -jar /Users/stefan/apps/ili2pg-4.3.0/ili2pg-4.3.0.jar \
--dbhost 192.168.50.8 --dbport 5432 --dbdatabase pub --dbusr ddluser --dbpwd ddluser \
--dbschema av_lidar_2019 --models SO_AGI_Lidarprodukte_Publikation_20180202 \
--defaultSrsCode 2056 --createGeomIdx --createFk --createFkIdx --createEnumTabs --beautifyEnumDispName --createMetaInfo --createNumChecks --nameByTopic --strokeArcs --sqlEnableNull \
--export fubar1.xtf
```

```
UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.dsm/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bezugsrahmen = 'LV95',
    produkttyp = 'DOM'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.dsm_hillshade/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bezugsrahmen = 'LV95',
    produkttyp = 'DOM_Relief'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.dtm/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bezugsrahmen = 'LV95',
    produkttyp = 'DTM'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.dtm_hillshade/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bezugsrahmen = 'LV95',
    produkttyp = 'DTM_Relief'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.dtm_contour50cm/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'_50cm.zip',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'Shape',
    bezugsrahmen = 'LV95',
    produkttyp = 'Hoehenlinien'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.dtm_slope/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bezugsrahmen = 'LV95',
    produkttyp = 'DTM_Hangneigung'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.laz/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'.laz',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'LAZ',
    bezugsrahmen = 'LV95',
    produkttyp = 'Rohdaten'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.ndsm_buildings/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'_buildings.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bezugsrahmen = 'LV95',
    produkttyp = 'nDOM'
WHERE
    link IS NULL
;

UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.ndsm_buildings/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'_buildings.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bemerkung = 'Gebäude',
    bezugsrahmen = 'LV95',
    produkttyp = 'nDOM'
WHERE
    link IS NULL
   -- produkttyp ='nDOM'
;


UPDATE 
    av_lidar_2019.lidarprodukte_lidarprodukt 
SET
    kachel_hoehe = 2000,
    kachel_breite = 2000,
    pixel_hoehe = 0.25,
    pixel_breite = 0.25,
    flugjahr = 2019,
    flugdatum = '2019-03',
    link = 'https://geo.so.ch/geodata/ch.so.agi.lidar_2019.ndsm_vegetation/'||ST_XMin(geometrie)||'_'||ST_YMin(geometrie)||'_vegetation.tif',
    minimum = 0,
    maximum = 0,
    filegroesse = 0,
    filetyp = 'GeoTIFF',
    bemerkung = 'Vegetation',
    bezugsrahmen = 'LV95',
    produkttyp = 'nDOM'
WHERE
    link IS NULL
;
```
