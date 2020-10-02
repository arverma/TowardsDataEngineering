
### Terraform
```
terraform init -var-file="terraform.tfvars" "-lock=false"

terraform plan -var-file="terraform.tfvars" "-lock=false"

terraform apply -var-file="terraform.tfvars" "-lock=false"

terraform destroy -var-file="terraform.tfvars" "-lock=false"
```

```
terragrunt init

terragrunt plan

terragrunt apply
```