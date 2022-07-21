APIDOC_TITLE = "Base aligner"
APIDOC_DESCRIPTION = "Documentation of the aligner"
APIDOC_VERSION = "1.0"

.PHONY: clean help uninstall install_programs install_sigma install install_python install_java install_node
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

define UNINSTALL_PYSCRIPT
import os

req = 'requirements.txt'
for package in [x.split('==')[0] for x in open(req).read().split('\n')]:
	if package.strip():
		os.system('pip uninstall --yes %s' % package)

endef
export UNINSTALL_PYSCRIPT

define INSTALL_PYSCRIPT
import os

req = 'requirements.txt'
for package in [x.split('==')[0] for x in open(req).read().split('\n')]:
	if package.strip():
		os.system('pip install %s' % package)
endef
export INSTALL_PYSCRIPT

clean: ## Remove all residual Python files
	find . -name '*.pyc' -exec rm -f {} +

help: ## Show all commands
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

uninstall: ## Remove all project dependencies
	cd interopera;	\
	python -c "$$UNINSTALL_PYSCRIPT"

install_programs: ## Install all programs dependencies
	sudo apt-get update
	sudo apt-get install unzip
	sudo apt-get install git
	sudo apt-get install gcc
	sudo apt-get install graphviz
	sudo apt-get install ant
	sudo apt-get install pip

install_sigma: ## Instala as dependências do sigma Install all Sigma dependencies
	cd ~;	\
	touch .bashrc;	\
	echo "alias dir='ls --color=auto --format=vertical -la'" >> .bashrc;	\
	echo "export HISTSIZE=10000 HISTFILESIZE=100000" >> .bashrc;	\
	source .bashrc;	\
	mkdir workspace;	\
	mkdir programs;	\
	cd programs;	\
	wget 'https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.23/bin/apache-tomcat-8.5.23.zip';	\
	wget 'http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz';	\
	wget 'http://wwwlehre.dhbw-stuttgart.de/~sschulz/WORK/E_DOWNLOAD/V_2.0/E.tgz';	\
	tar -xvzf E.tgz;	\
	unzip apache-tomcat-8.5.23.zip;	\
	rm apache-tomcat-8.5.23.zip;	\
	cd ~/programs/apache-tomcat-8.5.23/bin;	\
	chmod 777 *;	\
	cd ../webapps;	\
	chmod 777 *;	\
	cd ~/workspace/;	\
	git clone https://github.com/ontologyportal/sigmakee;	\
	git clone https://github.com/ontologyportal/sumo;	\
	git clone https://github.com/ontologyportal/TPTP-ANTLR;	\
	git clone https://github.com/ontologyportal/SigmaUtils;	\
	cd ~;	\
	mkdir .sigmakee;	\
	cd .sigmakee;	\
	mkdir KBs;	\
	cp -R ~/workspace/sumo/* KBs;	\
	me="$(whoami)";	\
	cp ~/workspace/sigmakee/config.xml ~/.sigmakee/KBs;	\
	sed -i "s/theuser/$me/g" KBs/config.xml;	\
	cd ~/programs;	\
	gunzip WordNet-3.0.tar.gz;	\
	tar -xvf WordNet-3.0.tar;	\
	cp WordNet-3.0/dict/* ~/.sigmakee/KBs/WordNetMappings/;	\
	cd ~;	\
	echo "export SIGMA_HOME=~/.sigmakee" >> .bashrc;	\
	echo "export SIGMA_SRC=~/workspace/sigmakee" >> .bashrc;	\
	echo "export ONTOLOGYPORTAL_GIT=~/workspace" >> .bashrc;	\
	echo "export CATALINA_OPTS=\"$CATALINA_OPTS -Xmx10g\"" >> .bashrc;	\
	echo "export CATALINA_HOME=~/programs/apache-tomcat-8.5.23" >> .bashrc;	\
	echo $ONTOLOGYPORTAL_GIT
	source .bashrc;	\
	cd ~/programs/E;	\
	./configure;	\
	make;	\
	make install;	\
	cd ~/workspace/sigmakee;	\
	ant

install: clean uninstall ## Install all dependencies of the project
	cd interopera;	\
	touch approximate;	\
	touch queries;	\
	touch split;	\
	touch unique;	\
	mkdir -p csv;	\
	mkdir -p results;	\
	mkdir -p samples;	\
	python -c "$$INSTALL_PYSCRIPT"

install_python: ## Install python and set its path
	sudo apt-get install python3
	sudo apt-get install python-is-python3

install_java: ## Install java and set its path
	sudo apt-get install openjdk-18-jre-headless
	cd ~;	\
	echo "export JAVA_HOME=/usr/lib/jvm/java-1.18.0-openjdk-amd64" >> .bashrc;	\
	source .bashrc

install_node: ## Install node
	sudo apt-get install nodejs
	sudo apt-get install npm 