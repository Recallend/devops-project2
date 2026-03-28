pipeline {
    agent any
    environment {
        APP_NAME = 'document-scanner'
        DOCKER_IMAGE = 'document-scanner:latest'
        HOST_PORT = '5002'  // Port exposed on GCP VM
    }
    stages {
        stage('Checkout Code') {
            steps {
                git(
                    url: 'https://github.com/Recallend/devops-project2.git',
                    branch: 'main',
                    credentialsId: 'github-pat'
                )
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('Stop Old Container') {
            steps {
                sh """
                    docker stop ${APP_NAME} || true
                    docker rm ${APP_NAME} || true
                """
            }
        }
        stage('Run Container') {
            steps {
                sh "docker run -d -p ${HOST_PORT}:5000 --name ${APP_NAME} ${DOCKER_IMAGE}"
            }
        }
    }
    post {
        success {
            echo 'Document Scanner app deployed successfully!'
        }
        failure {
            echo 'Deployment failed. Check logs.'
        }
    }
}
