# av_lidar_2019

```
gdaltindex lidar2019.shp /lidar2019/02_DTM_25cm_TIFF/*.tif
```
Und nach `/lidar2019/99_Derivate/`

## DTM Processing
Komprimieren und Overviews mittels `./scripts/dtm.py`.

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm/
gdalbuildvrt -addalpha dtm.vrt *.tif
```

Einzelnes BigTIFF erstellen:
```
./scripts/bigtiff_dtm.sh
```

## DOM Processing
Komprimieren und Overviews mittels `./scripts/dom.py`.

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dom/
gdalbuildvrt -addalpha dom.vrt *.tif
```

Einzelnes BigTIFF erstellen:
```
./scripts/bigtiff_dom.sh
```


## DTM Hillshading
Hillshading der einzelnen Kacheln rechnen:
```
./scripts/hillshade_dtm.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm_hillshade/
gdalbuildvrt -addalpha dtm_hillshade.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_dtm_hillshade.py
```

## DTM Slope
Einzelne Kacheln rechnen:
```
./scripts/slope_dtm.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm_slope/
gdalbuildvrt -addalpha dtm_slope.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_dtm_slope.sh
```

## DOM Hillshading
Hillshading der einzelnen Kacheln rechnen:
```
./scripts/hillshade_dom.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dom_hillshade/
gdalbuildvrt -addalpha dom_hillshade.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_dom_hillshade.py
```

## Rasterizing Vegetation
```
./scripts/rasterize_vegetation.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/vegetation/
gdalbuildvrt -addalpha vegetation.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_vegetation.sh
```


## Rasterizing Buildings
```
./scripts/rasterize_buildings.py
```

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/buildings/
gdalbuildvrt -addalpha buildings.vrt *.tif
```

Einzelnes BigTiff erstellen:
```
./scripts/bigtiff_vegetation.sh
```

## LAS to LAZ
```
./scripts/las2laz.py
```

