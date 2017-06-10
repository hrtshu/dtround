# dtround
Python module for rounding datetime/date object

# Installation
```bash
$ pip install dtround
```

# Functions
| Function		| Description												|
|---------------|-----------------------------------------------------------|
| floor			| Round down datetime/date object							|
| ceil			| Round up datetime/date object								|
| round			| Round off datetime/date object							|
| fday_month	| Return the first day of the month of datetime/date object	|
| fday_year		| Return the first day of the year of datetime/date object	|

# Example
```python
import dtround
from datetime import datetime, timedelta

dt = datetime(2048, 4, 16, 8, 32, 2, 65536)
unit = timedelta(minutes=15)

# Simple use
print(dtround.floor(dt, unit)) # 2048-04-16 08:30:00
print(dtround.ceil(dt, unit)) # 2048-04-16 08:45:00

print(dtround.fday_month(dt)) # 2048-04-01 00:00:00
print(dtround.fday_year(dt)) # 2048-01-01 00:00:00

# Combination
unit = timedelta(weeks=1)
base = dtround.fday_month(dt)
print(dtround.ceil(dt, unit, base=base)) # 2048-04-22 00:00:00
```

# Supported Python versions
Python 2.7+ and Python 3.2+

# License
MIT License

See [LICENSE.txt](LICENSE.txt)

# Author
Shuhei Hirata &lt;<sh7916@gmail.com>&gt;
