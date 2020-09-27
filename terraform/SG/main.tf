resource "aws_security_group" "sfia2_sg" {
  name        = "custom ingress"
  description = "Allow custom inbound traffic"
  vpc_id      = var.vpc_id

  dynamic "ingress" {
      for_each = [for i in var.ingress_ports: {
          from_port = i.from_port
          protocol = "tcp"
          to_port = i.to_port
          cidr_blocks = i.cidr
      }]

      content {
          from_port = ingress.value.from_port
          protocol = ingress.value.protocol
          to_port = ingress.value.to_port
          cidr_blocks = ingress.value.cidr_blocks
      }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "sfia2_sg"
  }
}