# Python

**Heads up!** Many \*nix OSes (like many Debian-based Linux distributions) require you to use `python3` instead of `python`!

### Check your Python version
```bash
python -V
```

Remember, if that doesn't work, try this instead!

```bash
python3 -V
```

### Run Python unittest
```bash
python -m unittest discover -s /path/to/unittest/lambdas
```

### Install Python Libraries

```bash
python -m pip install --user --upgrade "<library_name>"
```

### Managing Requirements

**Create a Virtual Environment**

```bash
python -m venv venv
```

**Activate a Virtual Environment** - _Linux_
```bash
source venv/bin/activate
```


**Creating a requirements.txt file**

```bash
python -m pip freeze > requirements.txt
```

**Installing a requirements.txt file**

```bash
python -m pip install -r requirements.txt
```
