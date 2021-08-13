pipeline{
    agent any
    stages{
        stage('Setup nginx proxy'){
            steps{
                sh "bash scripts/ansible.sh"
            }
        }
    }
}