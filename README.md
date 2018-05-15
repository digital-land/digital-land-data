# Digital land data

A collection of geographical [data](data) published by government which may be useful for people building houses.

# Building

These datasets have been collected and transformed by hand using [GDAL](http://www.gdal.org/) and other conversion scripts in the [bin](bin) and [lib](lib) directories.

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init

The process of refreshing the data is being automated as a pipeline of [luigi](https://github.com/spotify/luigi) tasks:

    $ make

# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific copyright and licensing, otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
