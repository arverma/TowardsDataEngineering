# PySpark
### Drop Columns from Spark DataFrame

`df = df.drop("query_type").drop("_c0").drop("_c01")`

### Write data to S3

`df.write.mode("overwrite").format("csv").option("compression", ".gzip").save(output_s3_path_in_string, header=True)`

### Validation Steps
`df_new = spark.read.csv("s3://leadid-sandbox/aranjan/mysql_leads_new")`

`df_old = spark.read.option("delimiter", "\x01").csv("s3://..")`

`df_new.count()`

`df_intersect = df_old.intersect(df_new)`

`df_subtract = df_old.subtract(df_intersect)`

`df_new.filter(df_new._c0 == "").filter(df_new._c1 == "").head()`

### Select records with specific string in columns

`df.filter(lower(col("_c0")).contains('%string_to_find%')).head()`

### Get max/min/mean value for a column

`max_value = df.agg({"_c0": “max”}).collect()[0]`

# Linux
### Run a job in background on Linux

`nohup command > my.log 2>&1 &`

### extract .gz file

`gunzip *`

### Add extension to file
`for f in *; do mv "$f" "$f.gz"; done`

### Find a file in Linux
`$ sudo find . -name <file_name>`

### Check IP to whitelist
`curl ifconfig.me ; echo`

# AWS

## S3
### Rename files in S3

`for f in $(aws s3api list-objects --bucket bucket_name --prefix "key/" --delimiter "/" | grep 097 | cut -d : -f 2 | cut -d \" -f 2);  do aws s3 mv s3://bucket_name/$f s3://bucket_name/${f/%/.csv.gz}; done `

### Sync files at two S3 locations

`aws s3 sync s3_source s3_target --recursive`

### Download bucket object from s3
`aws s3 cp s3://.. . --recursive`

## EMR
### Connect to EMR Cluster from CLI

`ssh -i file.pem hadoop@ip.ip.ip.ip`

### Screen

* Create a new screen: `screen -S aranjan`
* Go into specific screen: `screen -rd aranjan`
* Nested screen: `screen -t aman`

### Secure copy a file from local to hadoop

`scp -i file.pem file_path hadoop@ip.ip.ip.ip:/home/hadoop/`

## EKS
### Delete multiple pods
`kubectl get pods -n default | grep Running | cut -d' ' -f 1 | xargs kubectl delete pod -n default`

### See which pod is running on which node
`kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name -n stage`

### Adding WebIdentity role to a ServiceAccount
`kubectl annotate serviceaccount -n <SERVICE_ACCOUNT_NAMESPACE> <SERVICE_ACCOUNT_NAME> \
eks.amazonaws.com/role-arn=arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_ROLE_NAME`

### Get SparkUI for a Spark Pod
`kubectl port-forward <driver-pod-name> 4040:4040 --namespace <name_space>`

### Set default namespace for kubectl commands
```
kubectl config set-context --current --namespace=<insert-namespace-name-here>
# Validate it
kubectl config view --minify | grep namespace:
```

### Configure EKS
`aws eks update-kubeconfig --name <cluster_name> --region us-east-1`

### JupyterHub
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo update
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm upgrade --install <release_name> jupyterhub/jupyterhub --namespace <name_space> --version=0.9.0 --values config.yaml
helm uninstall <relase-name> -n <name-space>
```
### Get all pods in an EKS cluster
`kubectl get pods --all-namespaces`

### Get airflow UI for airflow pod
`kubectl port-forward <airflow-pod-name> 8080:8080`

# Python

### Run Python unittest
`python -m unittest discover -s /path/to/unittest/lambdas`

### Install Python Libraries
`python3 -m pip install --user --upgrade "<library_name>"`

