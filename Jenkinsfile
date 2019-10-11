pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Hello testing world'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_ppa2.py'
            }
        }
    }
}