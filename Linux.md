# Linux

## Table of contents

1) [Run a job in background on Linux](#runAJobInBack)
2) [tar](#tar)
3) [gunzip](#gunzip)
4) [Add extension to a file](#addExtensionToAFile)
5) [Find a file in linux](#findAFile)
6) [Check IP to whitelist](#checkIpToWhitelist)
7) [Outputs Geographical Information, regarding an ip_address](#outputGeographicalInfo)
8) [Compare two text files and show the differences](#compareTwoTextFiles)
9) [Show the available space on the mounted filesystems](#showFilesystemSpace)
10) [Show the size of a file or a folder](#showSizeOfFile)
11) [Kill all the instances of a particular program](#killall)
12) [List the conents of a file in a numbered fashion](#listContentsOfAFile)
13) [Display the word count in a text file](#displayWordCount)
14) [List running processes in a tree like format](#listRunningProcesses)
15) [Display the time and date on the top right corner of the terminal](#displayTimeAndDate)
16) [Search Bash history](#searchBashHistory)
17) [Moves the cursor to the beginning of the line](#moveCursorToTheBeginning)
18) [Moves the cursor to the end of the line](#moveCursorToTheEndOfLine)

### <a name="runAJobInBack"></a> Run a job in background on Linux

`nohup command > my.log 2>&1 &`

### <a name="tar"></a> tar

* #### Create a tar archive
    `tar -cvf <file_name.tar> <file1> <file2>`
    
    * -c - create
    * -v - verbose
    * -f - the filename of the tar archive

* #### Extract tar archives
    `tar -xvf <file_name.tar>`
    
    * -x - extract
    * -v - verbose
    * -f - the filename of tar archive to extract

* #### Create archives and compress with tar
    `tar -czvf <file_name.tar.gz> <file1> <file2>`

    * -c - create
    * -z - zip
    * -v - verbose
    * -f - the filename of the compressed file

* #### Uncompress using tar
    `tar -xzvf <file_name.tar.gz>`

    * -xz - uncompress and extract
    * -v - verbose
    * -f - the filename of the compressed file

### <a name="gunzip"></a> gunzip

* #### Compress a file with gzip
    `gzip <file_name>`

* #### Extract .gz file
    `gunzip <file_name.gz>`

### <a name="addExtensionToAFile"></a> Add extension to file
`for f in *; do mv "$f" "$f.gz"; done`

### <a name="findAFile"></a> Find a file in Linux
`$ sudo find . -name <file_name>`

### <a name="checkIpToWhitelist"></a> Check IP to whitelist
`curl ifconfig.me ; echo`

### <a name="outputGeographicalInfo"></a> Outputs Geographical Information, regarding an ip_address
`curl ipinfo.io ; echo`

### <a name="compareTwoTextFiles"></a> Compare two text files and show the differences
`diff -y -w 50 <file1> <file2> --suppress-common-lines`
    
* -y - shows line difference side by side
* -w - lets us specify the maximum line width to use to avoid wraparound lines
* -suppress-common-lines - suppress the matching lines, letting us to focus on lines which have differences

### <a name="showFilesystemSpace"></a> Show the available space on the mounted filesystems
`df -h`

### <a name="showSizeOfFile"></a> Show the size of a file or a folder
`du -sh <file/folder_name>`

### <a name="killall"></a> Kill all the instances of a particular program
`killall <program_name>`

### <a name="listContentsOfAFile"></a> List the conents of a file in a numbered fashion
`nl <file_name>`

### <a name="displayWordCount"></a> Display the word count in a text file
`wc -l <file_name>`

### <a name="listRunningProcesses"></a> List running processes in a tree like format
`pstree`

### <a name="displayTimeAndDate"></a> Display the time and date on the top right corner of the terminal
`while sleep 1;do tput sc;tput cup 0 $(($(tput cols)-29));date;tput rc;done &`

### <a name="searchBashHistory"></a> Search Bash history
`Ctrl+r`

### <a name="moveCursorToTheBeginning"></a> Moves the cursor to the beginning of the line
`Ctrl+a`

### <a name="moveCursorToTheEndOfLine"></a> Moves the cursor to the end of the line
`Ctrl+e`
