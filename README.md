# ogcFeatureApiCollectionDownloader

A python package to automatically download data from an OGC Feature API Collection.

## Install
`pip install ogcFeatureApiCollectionDownloader`

## How to use
```
import os

from ogcFeatureApiCollectionDownloader import downloader

download_location = f"{os.getcwd()}/downloads"

downloader.DownloadCollection(
    url="https://demo.pygeoapi.io/stable/collections/lakes/"
).download(
    download_path=download_location
)


```