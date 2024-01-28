Hello World
28-Jan-2024

Reference;
https://github.com/datawire/hello-world-python

Load into VS Code
docker build --pull --rm -f "Dockerfile" -t helloworldpython:latest "."
docker run --rm -d -p 8080:8080/tcp helloworldpython:latest 


Launch PyCharm
New project
hello-world-python
/home/stevepro/GitHub/StevePro9/PythonSetup/ThirdParty


Rename main.py to app.py
touch Dockerfile
touch requirements.txt
prompted to install requirements.txt


Update app.py
curl localhost:8080
curl: (7) Failed to connect to localhost port 8080: Connection refused

Run project
curl localhost:8080
Hello World (Python)! (up 0:00:32)

Update Dockerfile
docker build --pull --rm -f "Dockerfile" -t helloworldpython:latest "." 
