pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t diabetes-fastapi:v2 .'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker images'
            }
        }

    }
}