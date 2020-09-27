
resource "aws_instance" "example" {
  provider = "aws.aws-uk"
  ami           = var.ami
  instance_type = var.type
}