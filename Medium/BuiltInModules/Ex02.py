import os

path: str = '.'

print(os.getcwd())
print(os.listdir(path))
print(os.path.exists(path))
print(os.stat(path))
#os.mkdir('bob')
#os.rename('old', 'new)
#os.remove('new')
#os.chdir('bob')