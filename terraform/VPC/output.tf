output "vpc_id" {
    value = aws_vpc.sfia2_vpc.id
}

output "public_subnets_id" {
    value = aws_subnet.public_sfia2.*.id
}