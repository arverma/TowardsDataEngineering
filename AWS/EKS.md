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

### Find a file in Linux
`$ sudo find . -name <file_name>`

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
`export KUBECONFIG=$KUBECONFIG:~/.kube/config-nonprod`
`aws eks update-kubeconfig --name <cluster_name> --region us-east-1`



### Get all pods in an EKS cluster
`kubectl get pods --all-namespaces`

### Get airflow UI for airflow pod
`kubectl port-forward <airflow-pod-name> 8080:8080`
