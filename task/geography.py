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
                if 'geography' in item.keys():
                    publication = item['publication']
                    geography = item['geography']
                    task = item['task']
                    url = item['data-url']
                    key = item['key']

                    if (task in ['geojson']):
                        yield GeoJSON(publication, geography, url, key)


class GeoJSON(luigi.Task):
    publication = luigi.Parameter()
    geography = luigi.Parameter()
    url = luigi.Parameter()
    key = luigi.Parameter()

    def run(self):
        print("+ fetching", self.url)
        r = requests.get(self.url, allow_redirects=True)
        g = geojson.c14n(r.json(), self.geography, self.key)

        with self.output().open("w") as output:
            geojson.dump(g, output)

    def output(self):
        return luigi.LocalTarget("data/area/{0}.geojson".format(self.publication))
