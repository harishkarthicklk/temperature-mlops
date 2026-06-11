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

    }
}