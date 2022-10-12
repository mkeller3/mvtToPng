import os

from ogcFeatureApiCollectionDownloader import downloader

download_location = f"{os.getcwd()}/downloads"

downloader.DownloadCollection(
    url="https://demo.pygeoapi.io/stable/collections/lakes/"
).download(
    download_path=download_location
)

# downloader.DownloadCollection(
#     url="https://demo.ldproxy.net/daraa/collections/AgricultureSrf/"
# ).download(
#     download_path=download_location
# )

# downloader.DownloadCollection(
#     url="https://api.qwikgeo.com/api/v1/collections/user_data.vccvnkvhrmzsqqbbcacvjrlspfpdhbcthvjszbnfledgklxnps",
#     headers={
#         'Authorization': 'Bearer xxx',
#         'Content-Type': 'application/json'
#     }
# ).download(
#     download_path=download_location
# )