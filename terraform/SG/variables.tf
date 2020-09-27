variable "vpc_id" {
    default = "default value"
}

variable "ingress_ports" {
    default = [
        {
            from_port = "22"
            to_port = "22"
            cidr = ["0.0.0.0/0"]
        },
        {
            from_port = "80"
            to_port = "80"
            cidr = ["0.0.0.0/0"]
        },
        # required for jenkins webhook to work in this simple setup but is bad practice
        {
            from_port = "8080"
            to_port = "8080"
            cidr = ["0.0.0.0/0"]
        }
    ]
}