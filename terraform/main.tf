provider "aws" {
  region  = "eu-west-1"
  shared_credentials_file = "~/.aws/credentials"
  version = "3.8.0"
}

#contains vpc IG and subnets
module "vpc" {
    source = "./VPC"
}

module "sg" {
  source = "./SG"
  vpc_id = module.vpc.vpc_id
}

module "ec2" {
  source = "./EC2"
  vpc_security_groups_ids = module.sg.sg_id
  public_subnet_ids = module.vpc.public_subnets_id
  # public_subnets = slice(var.private_subnet_cidr_blocks, 0, each.value.private_subnet_count)
}
