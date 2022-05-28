# Python3

## Table of Contents

1) [Check your Python version](#checkYourPythonVersion)
2) [Run Python unittest](#runPythonUnittest)
3) [Install Python Libraries](#installPythonLibraries)
4) [Managing Requirements](#managingRequirements)
5) [Prettify print yaml files](#PrettifyfyPrintYamlFiles)
6) [Prettify print json files](#PrettifyfyPrintJsonFiles)
7) [Read file from Gitlab private repo](Python%20Script/read_from_gitlab.py)
8) [Read parquet file](Python%20Script/read_parquet_file.py)

### Create a server
```bash
python3 -m http.server 8000
```

### <a name="checkYourPythonVersion"></a> Check your Python version
```bash
$ python3 -V
```

### <a name="runPythonUnittest"></a> Run Python unittest
```bash
$ python3 -m unittest discover -s /path/to/unittest/lambdas
```

### <a name="installPythonLibraries"></a> Install Python Libraries

```bash
$ python3 -m pip install --user --upgrade "<library_name>"
```

### <a name="managingRequirements"></a> Managing Requirements

**Create a Virtual Environment**

```bash
$ python3 -m venv venv
```

**Activate a Virtual Environment** - _Linux_
```bash
$ source venv/bin/activate
```


**Creating a requirements.txt file**

```bash
$ python3 -m pip freeze > requirements.txt
```

**Installing a requirements.txt file**

```bash
$ python3 -m pip install -r requirements.txt
```

### <a name="PrettifyfyPrintYamlFiles"></a> Prettify print yaml files
```bash
$ python3 -c 'import yaml;print(yaml.safe_load(open("<pathToFile.yaml>")))'`
```

### <a name="PrettifyfyPrintJsonFiles"></a> Prettify print json files
```bash
$ python3 -m json.tool <PathToFile.Json>`
```