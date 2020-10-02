### JupyterHub
```
helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo update
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm upgrade --install <release_name> jupyterhub/jupyterhub --namespace <name_space> --version=0.9.0 --values config.yaml
helm uninstall <relase-name> -n <name-space>
```