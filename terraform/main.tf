provider "aws" {
  region  = "eu-west-1"
  shared_credentials_file = "~/.aws/credentials"
  alias   = "aws-uk"
}

module "vpc" {
    source = "./VPC"
    vpc_id = module.vpc.vpc_id
}

module "sg" {
  source = "./SG"
}

module "ec2" {
  source = "./EC2"
  vpc_security_groups_ids = module.sg.sg_id
}