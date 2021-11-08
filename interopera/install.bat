echo off
cls
chcp 65001
echo Interopera:  instalando dependências
IF not EXIST %PYTHONPATH% (
  echo definindo PYTHONPATH
  set PYTHONPATH=C:\Users\AP\AppData\Local\Programs\Python\Python310\
)
pip install deepmatcher==0.1.2
pip install textdistance==4.2.1
pip install nltk==3.6.2
pip install python-dotenv==0.19.0
pip install google-cloud-translate==3.4.0
pip install pandas==1.3.3
pip install PyQt5==5.15.5
pip install py-entitymatching==0.4.0
pip install tk==0.1.0
pip install numpy==1.13.0
pip install pandasql==0.7.3
echo Finalizado