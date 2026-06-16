README 02
24-May-2026

Font manager and text rendering
render everything to self.writer in virtual coordinates
always blit self.screen at (0, 0)
treat screen as a “presentation surface”, not a game world


30-May-2026
Here is the source code for C#/XNA
https://github.com/SteveProXNA/SimpsonsTrivia/tree/master/SimpsonsTrivia.XNA 
In Python - how should I best architect the code? I use UV so I would have Simpsons project root and beneath 
a README file and pyproject.toml file 
From there I believe to have the main entry point "program.py" at the root level with 2x top level folders "src" and "tests"
or should I rename src to app? 
Finally where should be Content directory live i.e. on what level ? top or beneath src and should I name the content folder 
Content or Assets?