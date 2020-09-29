resource "aws_db_subnet_group" "storysite-subnet-group" {
  name       = "storysite_db"
  subnet_ids = var.subnet_ids
}


resource "aws_db_instance" "default" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  name                 = "storysite"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.mysql5.7"
  db_subnet_group_name = "storysite_db"
  skip_final_snapshot = true
}