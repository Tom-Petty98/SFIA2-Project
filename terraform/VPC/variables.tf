variable "availability_zones" {
  description = "AZs in this region to use"
  default = ["eu-west-1a", "eu-west-1c"]
  type = "list"
}

# these values are placholders and get overwritten by .tfvars
variable "vpc_cidr" {}

variable "subnet_cidrs_public" {
  description = "Subnet CIDRs for public subnets (length must match configured availability_zones)"
}