# -*- coding: utf-8 -*-
"""
Module for downloading a collection from an OGC Feature API
.. module:: ogcFeatureApiCollectionDownloader.downloader
   :platform: Unix, Windows
   :synopsis: Module for downloading a collection from an OGC Feature API
"""

import logging
import os
import json
import sys

import requests

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


class OgcFeatureApiCollectionDownloaderException(Exception):
    """ my custom exception class """


class DownloadCollection():
    """
    This class provides you the ability to download a OGC Feature API Collection.

    """

    def __init__(self, url: str, headers: object = {}):
        """
        Init method

        :param url: The url of the OGC Feature API Collection.

        """

        self.url = url

        self.headers = headers

        logging.info(
            "Validating that an OGC Feature API Collection exists at %s", url)

        response = requests.get(url=url, headers=headers)

        if response.status_code != 200:
            raise OgcFeatureApiCollectionDownloaderException(
                "This url did not return a 200 status code.")

        data = response.json()

        if 'id' not in data:
            raise OgcFeatureApiCollectionDownloaderException(
                "This url does not contain a valid OGC Feature API Collection.")

        if 'itemType' not in data:
            raise OgcFeatureApiCollectionDownloaderException(
                "This url does not contain a valid OGC Feature API Collection.")

        if data['itemType'] != 'feature':
            raise OgcFeatureApiCollectionDownloaderException(
                "This url does not contain a valid OGC Feature API Collection.")

        self.title = data['title']

        for link in data['links']:
            if link['rel'] == 'items' and link['type'] == 'application/geo+json':
                self.collection_url = link['href']

        logging.info(
            "Validated that an OGC Feature API Collection exists at %s", url)

    def download(self, download_path: str):
        """
        Download the OGC Feature API Collection into a geojson file.

        :param download_path: The location to download the data.

        """

        feature_collection = {
            "type": "FeatureCollection",
            "features": []
        }

        logging.info("Downloading OGC Feature Api Collection: %s.", self.title)

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        response = requests.get(url=self.collection_url, headers=self.headers)

        if 'features' not in response.json():
            raise OgcFeatureApiCollectionDownloaderException(
                "This url does not contain a valid Geojson FeatureCollection.")

        feature_collection['features'] += response.json().get('features')

        with open(f'{download_path}/{self.title}.geojson', 'w') as json_file:
            data = json.dumps(feature_collection)
            json_file.write(data[:-2])

        more_data = False

        for link in response.json()['links']:
            if link['rel'] == 'next':
                next_data_url = link['href']
                more_data = True

        while more_data:
            logging.info('Downloading data for %s', next_data_url)

            response = requests.get(url=next_data_url, headers=self.headers)

            if 'features' not in response.json():
                raise OgcFeatureApiCollectionDownloaderException(
                    "This url does not contain a valid Geojson FeatureCollection.")

            feature_collection['features'] += response.json().get('features')

            with open(f'{download_path}/{self.title}.geojson', 'a') as json_file:
                data = json.dumps(feature_collection['features'])
                data = data[:-1]
                data = data[1:]
                json_file.write(",")
                json_file.write(data)

            logging.info('Downloaded data for %s', next_data_url)

            more_new_data = False

            for link in response.json()['links']:
                if link['rel'] == 'next':
                    next_data_url = link['href']
                    more_new_data = True

            if more_new_data is False:
                more_data = False

        with open(f'{download_path}/{self.title}.geojson', 'a') as json_file:
            json_file.write("]}")

        logging.info("Downloaded OGC Feature Api Collection: %s.", self.title)
