variable "ami" {
    description = "AMI ID for ubuntu 18.04 LTS EC2 in Ireland"
    default = "ami-0823c236601fef765"
}

variable "type" {
    default = "t2.micro"
}

variable "key_name" {
    default = "ubuntu_ec2_key"
}

variable "public_subnet_ids" {
    default = "default value"
}

variable "vpc_security_groups_ids" {
    default = "default value"
}