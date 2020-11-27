pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "/usr/bin/python3.8 init.py"
            }
        }
        stage('Test') {
            steps {
                sh "/usr/bin/python3.8 test.py"
            }
        }
        stage('Deploy') {
            steps {
                sh "/usr/bin/python3.8 deploy.py"
            }
        }
     }
}
