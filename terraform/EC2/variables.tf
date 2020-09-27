variable "ami" {
    description = "AMI ID for EC2 in Ireland"
    default = "t2.micro"
}

variable "type" {
    default = "t2.micro"
}

variable "key_name" {
    default = "ubuntu_ec2_key"
}

variable "public_subnet_id" {
    default = "default value"
}

variable "vpc_security_groups_ids" {
    default = "default value"
}