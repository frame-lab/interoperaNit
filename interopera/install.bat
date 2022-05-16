echo off
cls
chcp 65001
echo Interopera:  instalando dependências
IF "%PYTHONPATH%"=="" (
  echo definindo PYTHONPATH
  set PYTHONPATH=C:\Users\AP\AppData\Local\Programs\Python\Python39\
)
mkdir csv
mkdir results
mkdir samples
type NUL > approximate
type NUL > queries
type NUL > split
type NUL > unique
pip install deepmatcher
pip install torchtext==0.9.0
pip install torch
pip install textdistance
pip install nltk
pip install python-dotenv
pip install google-cloud-translate
pip install pandas
pip install PyQt5
pip install py-entitymatching
pip install tk
pip install numpy
pip install pandasql
pip install tqdm
pip install py4j
echo Finalizado