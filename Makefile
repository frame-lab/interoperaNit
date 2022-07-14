APIDOC_TITLE = "Base aligner"
APIDOC_DESCRIPTION = "Documentation of the aligner"
APIDOC_VERSION = "1.0"

.PHONY: clean help uninstall
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

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

install_sigma:
	interopera=$(pwd)
	sudo apt-get install unzip
	sudo apt-get update
	cd ~;	\
	touch .bashrc;	\
	echo "alias dir='ls --color=auto --format=vertical -la'" >> .bashrc;	\
	echo "export HISTSIZE=10000 HISTFILESIZE=100000" >> .bashrc;	\
	source .bashrc;	\
	echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bashrc;	\
	source .bashrc;	\
	mkdir programs;	\
	cd programs;	\
	wget 'https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.23/bin/apache-tomcat-8.5.23.zip';	\
	wget 'http://wwwlehre.dhbw-stuttgart.de/~sschulz/WORK/E_DOWNLOAD/V_2.0/E.tgz';	\
	tar -xvzf E.tgz;	\
	unzip apache-tomcat-8.5.23.zip;	\
	rm apache-tomcat-8.5.23.zip;	\
	cd apache-tomcat-8.5.23/bin;	\
	chmod 777 *;	\
	cd ../webapps;	\
	chmod 777 *;	\
	mkdir .sigmakee
	cd .sigmakee
	mkdir KBs
	cp -R ~/workspace/sumo/* KBs
	me="$(whoami)"
	cp $interopera/workspace/sigmakee/config.xml ~/.sigmakee/KBs
	sed -i "s/theuser/$me/g" KBs/config.xml
	cd ~/Programs
	gunzip WordNet-3.0.tar.gz
	tar -xvf WordNet-3.0.tar
	cp WordNet-3.0/dict/* ~/.sigmakee/KBs/WordNetMappings/
	cd ~/programs/E
	sudo apt-get install gcc
	./configure
	make
	make install
	cd ~
	sudo apt-get install graphviz
	echo "export SIGMA_HOME=$interopera/interopera/.sigmakee" >> .bashrc
	echo "export SIGMA_SRC=$interopera/interopera/workspace/sigmakee" >> .bashrc
	echo "export ONTOLOGYPORTAL_GIT=$interopera/interopera/workspace" >> .bashrc
	echo "export CATALINA_OPTS="$CATALINA_OPTS -Xmx10g"" >> .bashrc
	echo "export CATALINA_HOME=~/programs/apache-tomcat-8.5.23" >> .bashrc
	source .bashrc
	cd $interopera/interopera/workspace/sigmakee
	sudo apt-get update
	sudo apt-get install ant
	ant

uninstall:
	cd interopera;	\
	python -c "$$UNINSTALL_PYSCRIPT"

clean:
	find . -name '*.pyc' -exec rm -f {} +

install: clean uninstall ## instala as dependências do projeto
	cd interopera;	\
	touch approximate;	\
	touch queries;	\
	touch split;	\
	touch unique;	\
	mkdir -p csv;	\
	mkdir -p results;	\
	mkdir -p samples;	\
	python -c "$$INSTALL_PYSCRIPT"