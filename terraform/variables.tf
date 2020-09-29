variable "vpc_cidr" {}

variable "subnet_cidrs_public" {
  description = "Subnet CIDRs for public subnets (length must match configured availability_zones)"
}
variable "db_username" {}
variable "db_password" {}