import os

import requests

from mvtToPng import converter

DOWNLOAD_LOCATION = f"{os.getcwd()}/downloads"

r = requests.get("https://basemaps.arcgis.com/arcgis/rest/services/World_Basemap_v2/VectorTileServer/tile/3/3/1.pbf")
vector_data = r.content


def test_bytes_to_png():
    result = converter.Converter(
        vector_tile_in_bytes=vector_data,
        z=3,
        y=2,
        x=3,
        download_path=DOWNLOAD_LOCATION,
        file_name="World_Basemap_v2"
    ).convert()
    assert result is True
