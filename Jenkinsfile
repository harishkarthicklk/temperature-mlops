pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

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

        stage('Wait For Rollout') {
            steps {
                bat 'kubectl rollout status deployment/backend'
            }
        }

        stage('Health Check') {
            steps {
                bat 'kubectl get pods'
            }
        }

    }

    post {

        failure {

            bat 'kubectl rollout undo deployment/backend'

        }

    }

}