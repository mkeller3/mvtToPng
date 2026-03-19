# -*- coding: utf-8 -*-
"""
Module for converting a vector tile to a png.
.. module:: mvtToPng.downloader
   :platform: Unix, Windows
   :synopsis: Module for converting a vector tile to a png.
"""

import logging
import sys
import os
import json

import geopandas as gpd
import matplotlib.pyplot as plt
from vt2geojson.tools import vt_bytes_to_geojson

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


class mvtToPngException(Exception):
    """ my custom exception class """


class Converter():
    """
    This class provides you the ability to convert a vector tile to a png.
    """

    def __init__(
        self,
        vector_tile_in_bytes: bytes,
        z: int,
        x: int,
        y: int,
        download_path: str,
        file_name: str,
        color: str = "#000000"
    ):
        """
        Init method

        :param vector_tile_in_bytes: The vector tile in bytes.
        :param z: The z location of the tile.
        :param x: The x location of the tile.
        :param y: The y location of the tile.
        :param download_path: The path to download the png to.
        :param file_name: The name of the png file.
        :param color: The color of the features on the map.

        """

        self.vector_tile_in_bytes = vector_tile_in_bytes
        self.z = z
        self.x = x
        self.y = y
        self.download_path = download_path
        self.file_name = file_name
        self.color = color

    def convert(self) -> bool:
        """
        Convert the vector tile to a png.

        """

        features = vt_bytes_to_geojson(
            b_content=self.vector_tile_in_bytes,
            x=self.x,
            y=self.y,
            z=self.z
        )

        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

        df_places = gpd.read_file(json.dumps(features), driver='GeoJSON')

        df_places.plot(color=self.color, aspect=1)

        plt.axis('off')

        plt.savefig(
            fname=f"{self.download_path}/{self.file_name}.png",
            bbox_inches="tight",
            pad_inches=0
        )

        return True
