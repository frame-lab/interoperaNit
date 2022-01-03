echo off
cls
chcp 65001
echo Interopera:  instalando dependências
IF not EXIST %PYTHONPATH% (
  echo definindo PYTHONPATH
  set PYTHONPATH=C:\Users\AP\AppData\Local\Programs\Python\Python310\
)
mkdir approximate
mkdir queries
mkdir split
mkdir unique
pip install deepmatcher
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
echo Finalizado