TARGETS=\
	data/organisation.tsv

digital-land-data:	clobber
	PYTHONPATH=".:./lib" luigi --module task --local-scheduler DigitalLand --workers 3

init::
	pip3 install -r requirements.txt

clobber::
	rm -f $(TARGETS)

clean::
	rm -rf .cache

prune::	clean
	rm -f .cache.sqlite
