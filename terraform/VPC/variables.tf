variable "availability_zones" {
  description = "AZs in this region to use"
  default = ["eu-west-1a", "eu-west-1c"]
  type = "list"
}

variable "vpc_cidr" {
  default = "15.0.0.0/16"
}

variable "subnet_cidrs_public" {
  description = "Subnet CIDRs for public subnets (length must match configured availability_zones)"
  default = ["15.0.10.0/24", "15.0.20.0/24"]
  type = "list"
}