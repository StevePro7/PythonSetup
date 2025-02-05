Yield in Python and Similar Concepts
05-fEB-2025

https://python.plainenglish.io/yield-in-python-and-similar-concepts-885f0afa7bf3

python -m venv .venv
.\.venv\Scripts\activate
OR
source .venv/bin/activate

Yield
enables programmers to create memory-efficient, responsive applications
that generate items one by one instead of loading everything into memory
at once

Yield
case where you don't want to store all the results in memory at once
but instead produce them one at a time
e.g.
huge web server log
01.py


Yield
calling it doesn't execute the entire function immediately
instead it returns a generator object which can be iterated
over

NB: each time you request the next item from the generator
the function continues from where it left off w/ next value
e.g.
<generator object countdown at 0x0000024F00EA9E40>
02.py


Example     API pagination
03.py


yield vs. return
04.py


Example:    streaming data
05.py