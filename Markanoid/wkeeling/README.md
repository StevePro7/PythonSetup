wkeeling
06-Jan-2024


pip install pygame


https://steveproxna.blogspot.com/2020/07/python-setup-cheat-sheet.html

Terminal
cd ~/GitHub/StevePro9/PythonSetup/Markanoid/wkeeling/arkanoid
pip freeze > requirements.txt
pip install -r requirements.txt

python arkanoid.py


IMPORTANT
could not get the Dockerfile working because 
the references to debian jessie have archived

reference:
https://stackoverflow.com/questions/46406847/docker-how-to-add-backports-to-sources-list-via-dockerfile

Tried different deb-src URI but continued to get the message
you must add deb-src URIs to sources.list