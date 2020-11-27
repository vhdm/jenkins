pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sudo sh "/usr/bin/python3.8 init.py"
            }
        }
        stage('Test') {
            steps {
                sudo sh "/usr/bin/python3.8 test.py"
            }
        }
        stage('Deploy') {
            steps {
                sudo sh "/usr/bin/python3.8 deploy.py"
            }
        }
     }
}
