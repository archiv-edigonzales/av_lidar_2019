# av_lidar_2019

```
gdaltindex lidar2019.shp /lidar2019/02_DTM_25cm_TIFF/*.tif
```
Und nach `/lidar2019/99_Derivate/`

## DTM Processing
Komprimieren und Overviews mittels `scripts/dtm.py`.

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dtm/
gdalbuildvrt -addalpha dtm.vrt *.tif
```

Einzelnes BigTIFF erstellen:
```

```

## DOM Processing
Komprimieren und Overviews mittels `scripts/dom.py`.

VRT erstellen:
```
cd /Samsung_T5/99_Derivate/dom/
gdalbuildvrt -addalpha dom.vrt *.tif
```


## DTM Hillshading

