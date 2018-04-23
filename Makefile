.PHONY: help clean dev docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "  docs	create pydocs for all relveant modules"

clean:
	rm -rf dist/*

docs:
	$(MAKE) -C docs html

package:
	python setup.py sdist
	python setup.py bdist_wheel --universal