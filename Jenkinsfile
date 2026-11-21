pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "cedricbuendia/diabetes-fastapi"
    }

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest -f Dockerfile .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE:latest'
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
                  $DOCKER_IMAGE:latest
                '''
            }
        }
    }
}