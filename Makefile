
# Environment
CONFIGPATH=.
SPHINXBUILD= sphinx-build
SOURCEDOC=sourcedoc
PYTHONPATH=./src
DOC = doc
RM = /bin/rm
PYTHON = python3

.PHONY: doc

doc:
	$(SPHINXBUILD) -c $(CONFIGPATH) -b html $(SOURCEDOC) $(DOC)

clean:
	$(RM) -f *~ */*~
	$(RM) -rf __pycache__ src/__pycache__ tests/__pycache__
	$(RM) -rf $(DOC)
	# remove index files
	$(RM) -rf data/*.index
