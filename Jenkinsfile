pipeline {

    agent any

    stages {

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Compare Models') {
            steps {
                bat 'python model_registry/compare_models.py'
            }
        }

        stage('Build Docker Images') {
            steps {
                bat 'docker compose build'
            }
        }
        stage('Deploy To Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/'
            }
        }

    }
}