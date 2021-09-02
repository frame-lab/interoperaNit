APIDOC_TITLE = "Ontology aligner"
APIDOC_DESCRIPTION = "Documentation of the aligner"
APIDOC_VERSION = "0.1.0"

.PHONY: clean clean-pyc clean-build help uninstall_all
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

define UNINSTALL_ALL_PYSCRIPT
import os
req = 'requirements.txt'
for package in [x.split('==')[0] for x in open(req).read().split('\n')]:
	if package.strip():
		os.system('pip uninstall --yes %s' % package)

endef
export UNINSTALL_ALL_PYSCRIPT

uninstall_all:
	@python -c "$$UNINSTALL_ALL_PYSCRIPT"

clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

install: clean uninstall_all ## instala as dependências do projeto
	pip install --upgrade pip
	pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt