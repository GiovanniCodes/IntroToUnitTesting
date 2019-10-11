pipeline {
    agent {docker {image 'python:3.7.2'} }

    stages {
        stage('Build') {
            steps {
                echo 'Hello testing world'
            }
        }
        stage('Test') {
            steps {
                sh 'python Assignment2_test.py'
            }
        }
    }
}
