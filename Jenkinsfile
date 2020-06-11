pipeline{
    agent any
    stages{
        stage("Make scripts executable"){
            steps{
                sh 'chmod +x ./scripts/*'
            }
        }
        stage("Setup enviroment"){
            steps{
                sh './scripts/before_installation.sh'
            }
        }
        stage("Ansible Setup"){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage("Deploy Docker Swarm Stack"){
            steps{
                sh './scripts/docker.sh'
            }
        }
    }
}