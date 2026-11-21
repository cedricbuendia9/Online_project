pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Version') {
            steps {
                sh 'docker version'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t diabetes-fastapi:ci -f Dockerfile .'
            }
        }

        stage('List Images') {
            steps {
                sh 'docker images'
            }
        }

    }
}