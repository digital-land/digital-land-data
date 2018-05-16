import os
import luigi
import requests
import frontmatter
import geojson
import csv


class Geography(luigi.WrapperTask):
    def requires(self):
        for row in csv.DictReader(open('data/publication/index.tsv'), delimiter='\t'):
            path = os.path.join('data/publication', row['path'])
            if path.endswith('.md'):
                item = frontmatter.load(path)
                task = item['task']
                if (task in ['geojson']):
                    publication = item['publication']
                    prefix = item['prefix']
                    url = item['data-url']
                    key = item['key']

                    yield GeoJSON(publication, prefix, url, key)


class GeoJSON(luigi.Task):
    publication = luigi.Parameter()
    prefix = luigi.Parameter()
    url = luigi.Parameter()
    key = luigi.Parameter()

    def run(self):
        print("+ fetching", self.url)
        r = requests.get(self.url, allow_redirects=True)
        g = geojson.c14n(r.json(), self.prefix, self.key)

        with self.output().open("w") as output:
            geojson.dump(g, output)

    def output(self):
        return luigi.LocalTarget("data/area/{0}.geojson".format(self.publication))
