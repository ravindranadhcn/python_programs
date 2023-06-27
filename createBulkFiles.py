## How to create Bulk Files at a Time ??

## mkdir test-dir && cd $_ && touch {1.10}.txt

from pathlib import Path

p = '/home/ravini/test-dir/'
for i in range(1,11):
   Path(p+str(i)+'.txt').touch()
