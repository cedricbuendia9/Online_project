pipeline {
    agent any

    stages {

        stage('Docker Version') {
            steps {
                sh 'docker version'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t diabetes-fastapi:latest -f Dockerfile .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop diabetes-fastapi-app || true
                docker rm diabetes-fastapi-app || true

                docker run -d \
                  --name diabetes-fastapi-app \
                  -p 8000:8000 \
                  diabetes-fastapi:latest
                '''
            }
        }

        stage('Verify') {
            steps {
                sh 'docker ps'
            }
        }
    }
}