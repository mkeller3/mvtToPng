import os

from mvtToPng import converter

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = os.path.join(DIR_PATH, "states_3_2_3.pbf")
DOWNLOAD_LOCATION = f"{os.getcwd()}/downloads"

with open(FILE_PATH, 'rb') as file:
    vector_data = file.read()


def test_bytes_to_png():
    result = converter.Converter(
        vector_tile_in_bytes=vector_data,
        z=3,
        y=2,
        x=3,
        download_path=DOWNLOAD_LOCATION,
        file_name="states"
    ).convert()
    assert result is True
