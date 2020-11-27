pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "python init.py"
            }
        }
        stage('Test') {
            steps {
                sh "pyhton test.py"
            }
        }
        stage('Deploy') {
            steps {
                sh "python deploy.py"
            }
        }
     }
}
