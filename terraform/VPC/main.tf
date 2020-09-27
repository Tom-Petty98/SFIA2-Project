resource "aws_vpc" "sfia2_vpc" {
  cidr_block       = var.vpc_cidr
  instance_tenancy = "default"

  tags = {
    Name = "sfia2_vpc"
  }
}

resource "aws_subnet" "public_sfia2" {
  count = length(var.subnet_cidrs_public)

  vpc_id = aws_vpc.sfia2_vpc.id
  cidr_block = var.subnet_cidrs_public[count.index]
  availability_zone = var.availability_zones[count.index]
}

resource "aws_internet_gateway" "sfia2_igw" {
  vpc_id = aws_vpc.sfia2_vpc.id
}

resource "aws_route_table" "public_sfia2" {
  vpc_id = aws_vpc.sfia2_vpc.id

  tags = {
    Name = "public_sfia2"
  }
}

resource "aws_route_table_association" "a" {
  count = length(var.subnet_cidrs_public)

  subnet_id      = element(aws_subnet.public_sfia2.*.id, count.index)
  route_table_id = aws_route_table.public_sfia2.id
}

resource "aws_route_table_association" "b" {
  gateway_id     = aws_internet_gateway.sfia2_igw.id
  route_table_id = aws_route_table.public_sfia2.id
}