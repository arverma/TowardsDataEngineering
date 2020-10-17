# Linux

## Table of contents

1) [Run a job in background on Linux](#runAJobInBack)
2) [tar](#tar)
3) [gunzip](#gunzip)
4) [Add extension to a file](#addExtensionToAFile)
5) [Find a file in linux](#findAFile)
6) [Check IP to whitelist](#checkIpToWhitelist)
7) [Outputs Geographical Information, regarding an ip_address](#outputGeographicalInfo)
9) [Show the available space on the mounted filesystems](#showFilesystemSpace)
10) [Show the size of a file or a folder](#showSizeOfFile)
11) [List the conents of a file in a numbered fashion](#listContentsOfAFile)
12) [Search Bash history](#searchBashHistory)
13) [Moves the cursor to the beginning of the line](#moveCursorToTheBeginning)
14) [Moves the cursor to the end of the line](#moveCursorToTheEndOfLine)
15) [Run previous ran command](#runPreviousCommand)
16) [Find word in a file](#findWordInAFile)
16) [Search For apt package](#searchAptPackage)

#### <a name="runAJobInBack"></a> Run a job in background on Linux

```bash
$ nohup command > my.log 2>&1 &`
```

#### <a name="tar"></a> tar

* Create a tar archive
    ```bash
    tar -cvf <file_name.tar> <file1> <file2>
    ```
    * -c - create
    * -v - verbose
    * -f - the filename of the tar archive

* Extract tar archives
    ```bash
    tar -xvf <file_name.tar>
    ```
    * -x - extract
    * -v - verbose
    * -f - the filename of tar archive to extract

* Create archives and compress with tar
    ```bash
    tar -czvf <file_name.tar.gz> <file1> <file2>`
    ```
    * -c - create
    * -z - zip
    * -v - verbose
    * -f - the filename of the compressed file

*  Uncompress using tar
    ```bash
    tar -xzvf <file_name.tar.gz>
    ```

    * -xz - uncompress and extract
    * -v - verbose
    * -f - the filename of the compressed file
#### <a name="gunzip"></a> gunzip

* Compress a file with gzip
    ```bash
    gzip <file_name>
    ```

* Extract .gz file
    ```bash
    gunzip <file_name.gz>
    ```

#### <a name="addExtensionToAFile"></a> Add extension to file
```bash
$ for f in *; do mv "$f" "$f.gz"; done
```

#### <a name="findAFile"></a> Find a file in Linux
```bash
$ sudo find . -name <file_name>
```

#### <a name="checkIpToWhitelist"></a> Check IP to whitelist
```bash
$ curl ifconfig.me ; echo
```

#### <a name="outputGeographicalInfo"></a> Outputs Geographical Information, regarding an ip_address
For current system's ip address:

```bash
$ curl ipinfo.io
```

For any specific ip address:

```bash
$ curl ipinfo.io/<ip_address>
```

#### <a name="showFilesystemSpace"></a> Show the available space on the mounted filesystems
```bash
$ df -h
```

#### <a name="showSizeOfFile"></a> Show the size of a file or a folder
```bash
$ du -sh <file/folder_name>
```

#### <a name="listContentsOfAFile"></a> List the conents of a file in a numbered fashion
```bash
$ nl <file_name>
```

#### <a name="searchBashHistory"></a> Search Bash history
```bash
Ctrl+r
```

#### <a name="moveCursorToTheBeginning"></a> Moves the cursor to the beginning of the line
```bash
Ctrl+a
```

#### <a name="moveCursorToTheEndOfLine"></a> Moves the cursor to the end of the line
```bash
Ctrl+e
```

#### <a name="runPreviousCommand"></a> Runs previous ran command
```bash
$ !!
```

#### <a name="findWordInAFile"></a> Find word in a file
```bash
$ grep <wordYouWantToFind> <fileName.txt>
```

#### <a name="searchAptPackage"></a> Search any apt package
```bash
$ apt-cache search <keyword>
```