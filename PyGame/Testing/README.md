Testing
16-May-2026

cd D:\GitHub\StevePro9\PythonSetup\PyGame
mkdir Testing

uv init --python 3.11
uv venv --python 3.11

.venv\Scripts\activate


docker build -t simpsons-trivia .
docker run -it simpsons-trivia

docker run -it --entrypoint bash simpsons-trivia


xhost +local:docker

docker run -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  simpsons-trivia:latest