
# Environment
CONFIGPATH  = .
SPHINXBUILD = sphinx-build
SOURCEDOC   = sourcedoc
PYTHONPATH  = ./data_prc
DOC         = doc
RM          = /bin/rm
PYTHON      = python3


.PHONY: doc

doc:
	$(SPHINXBUILD) -c $(CONFIGPATH) -b html $(SOURCEDOC) $(DOC)

test:
	$(PYTHON) -m unittest tests/test.py

clean:
	$(RM) -f *~ */*~
	$(RM) -rf __pycache__ data_prc/__pycache__ tests/__pycache__
	$(RM) -rf $(DOC)
	# remove index files
	$(RM) -rf data/*.index
