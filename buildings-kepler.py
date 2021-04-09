import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
from pyproj import CRS

# read file
buildings = gpd.read_file(r'data/region_buildings.shp')

buildings  = buildings.to_crs(4326)
buildings['dt'] = pd.to_datetime(buildings['date_formt'], format='%Y/%m/%d %H:%M:%S', errors = 'coerce')#.dt.tz_localize(None)
buildings['date_formt'] = [str(build).replace('-', '/') for build in buildings['dt']]

mapbuilding = KeplerGl(height=600)
mapbuilding.add_data(buildings, 'Helsinki buildings')
config={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "Helsinki buildings"
          ],
          "id": "0l8w49xcl",
          "name": [
            "date_formt"
          ],
          "type": "timeRange",
          "value": [
            -4225705724000,
            -3111465320000
          ],
          "enlarged": True,
          "plotType": "histogram",
          "animationWindow": "incremental",
          "yAxis": None
        }
      ],
      "layers": [
        {
          "id": "rdw5hkq",
          "type": "geojson",
          "config": {
            "dataId": "Helsinki buildings",
            "label": "Helsinki buildings",
            "color": [
              241,
              92,
              23
            ],
            "columns": {
              "geojson": "geometry"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                34,
                63,
                154
              ],
              "colorRange": {
                "name": "ColorBrewer YlOrRd-9",
                "type": "sequential",
                "category": "ColorBrewer",
                "colors": [
                  "#ffffcc",
                  "#ffeda0",
                  "#fed976",
                  "#feb24c",
                  "#fd8d3c",
                  "#fc4e2a",
                  "#e31a1c",
                  "#bd0026",
                  "#800026"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "stroked": False,
              "filled": True,
              "enable3d": False,
              "wireframe": False
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "date_formt",
              "type": "timestamp"
            },
            "colorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "heightField": None,
            "heightScale": "linear",
            "radiusField": None,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "Helsinki buildings": [
              {
                "name": "fid",
                "format": None
              },
              {
                "name": "date_formt",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": False,
      "latitude": 60.179179424875194,
      "longitude": 24.988806763710908,
      "pitch": 0,
      "zoom": 9.636543163687318,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
mapbuilding.save_to_html(file_name='root/Helsinki-buildings.html', config=config, read_only=True)