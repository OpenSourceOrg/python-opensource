<a href="https://opensource.org/licenses"><img align="right" width="150" height="200" src="https://opensource.org/files/OSIApproved.png"></a>
python-opensource
=================

`python-opensource` is an API Wrapper that allows you to query the
Open Source License API with Python.

Example
-------

```python
from opensource import licenses

for license in licenses.tagged("copyleft"):
    print(license.name)
```

Installing
----------

```
pip install opensource
```
