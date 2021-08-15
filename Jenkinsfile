pipeline{
    agent any
    environment{
        DOCKERHUB_LOGIN=credentials('DOCKERHUB_LOGIN')
        DATABASE_URI=credentials('DATABASE_URI')
    }
    stages{
        stage('Testing app'){
            steps{
                sh "bash scripts/tests.sh"
            }
        }
        stage('Installing dependencies'){
            steps{
                sh "bash scripts/dependencies.sh"
            }
        }
        stage('Building containers'){
            steps{
                sh "docker login -u ${DOCKERHUB_LOGIN_USR} -p ${DOCKERHUB_LOGIN_PSW}"
                sh "bash scripts/containers.sh"
            }
        }
        stage('Running ansible tasks'){
            steps{
                sh "bash scripts/ansible.sh"
            }
        }
        stage('Deploying'){
            steps{
                sh "bash scripts/deploy.sh"
            }
        }
    }
}