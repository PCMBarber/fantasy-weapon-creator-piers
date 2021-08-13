pipeline{
    agent any
    stages{
        stage{
            steps{
                sh "bash scripts/dependencies.sh"
            }
        }
        stage('Setup nginx proxy'){
            steps{
                sh "bash scripts/ansible.sh"
            }
        }
    }
}