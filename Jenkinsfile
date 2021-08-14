pipeline{
    agent any
    stages{
        stage('Testing app'){
            steps{
                sh "bash scripts/tests.sh"
            }
        }
        stage('Install dependencies'){
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