import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ogcFeatureApiCollectionDownloader",
    version="0.0.1",
    description="Automatically download a collection from an OGC Feature API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkeller3/ogcFeatureApiCollectionDownloader",
    author="Michael Keller",
    author_email="michaelkeller03@gmail.com",
    license="GNU General Public License v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=required,
    entry_points={
        "console_scripts": [
            "ogcFeatureApiCollectionDownloader=ogcFeatureApiCollectionDownloader.__main__:main",
        ]
    },
)
