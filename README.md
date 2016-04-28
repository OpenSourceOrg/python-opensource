python-opensource
=================

Example:

```python
from opensource import licenses

for license in licenses.tagged("copyleft"):
    print(license.name)
```
