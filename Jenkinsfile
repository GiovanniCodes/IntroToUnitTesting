pipeline {
    agent {docker {image 'python:3.7.2'} }

    stages {
        stage('Build') {
            steps {
                echo 'Hello testing world'
            }
        }
        stage('Test 1') {
            steps {
                sh 'python test_assignment.py'
            }
        }
        
        stage('Test 2') {
           steps {
               sh 'python test_assignment.py'
           }
       }
    }
}
