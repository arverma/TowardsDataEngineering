# Python

## Table of Contents

1) [Check your Python version](#checkYourPythonVersion)
2) [Run Python unittest](#runPythonUnittest)
3) [Install Python Libraries](#installPythonLibraries)
4) [Managing Requirements](#managingRequirements)

**Heads up!** Many \*nix OSes (like many Debian-based Linux distributions) require you to use `python3` instead of `python`!

### <a name="checkYourPythonVersion"></a> Check your Python version
```bash
python -V
```

Remember, if that doesn't work, try this instead!

```bash
python3 -V
```

### <a name="runPythonUnittest"></a> Run Python unittest
```bash
python -m unittest discover -s /path/to/unittest/lambdas
```

### <a name="installPythonLibraries"></a> Install Python Libraries

```bash
python -m pip install --user --upgrade "<library_name>"
```

### <a name="managingRequirements"></a> Managing Requirements

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
