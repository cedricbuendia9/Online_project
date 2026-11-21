pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Codigo obtenido desde GitHub'
            }
        }

        stage('Verify Files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

    }
}