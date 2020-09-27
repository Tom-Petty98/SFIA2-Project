
resource "aws_instance" "sfia2" {
  
  ami           = var.ami
  instance_type = var.type
  key_name = var.key_name
  vpc_security_group_ids = [var.vpc_security_groups_ids]
  associate_public_ip_address = true
  subnet_id = var.public_subnet_ids[0]

  # count = length(var.public_subnet_ids)
  # subnet_id              = var.public_subnet_ids[count.index]

  tags = {
    Name = "sfia2"
  }
}