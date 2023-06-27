## How to to change html files to php?
from pathlib from Path

p = Path('/home/ravini/template')
for i in p.iterdir():
   if i.suffix == '.html':
       i.rename(i.with_suffix('.php'))

