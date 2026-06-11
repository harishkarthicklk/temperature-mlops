pipeline {

    agent any

    stages {

        stage('Debug') {
            steps {
                bat 'where python'
                bat 'python --version'
                bat 'python -m pip list'
            }
        }

    }
}