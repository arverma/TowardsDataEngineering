## EMR
### Connect to EMR Cluster from CLI

`ssh -i file.pem hadoop@ip.ip.ip.ip`

### Screen

* Create a new screen: `screen -S aranjan`
* Go into specific screen: `screen -rd aranjan`
* Nested screen: `screen -t aman`

### Secure copy a file from local to hadoop

`scp -i file.pem file_path hadoop@ip.ip.ip.ip:/home/hadoop/`