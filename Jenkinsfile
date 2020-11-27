pipeline {
  agent any
  stages {
    stage('Build'){
      steps{
        python init.py
      }
    }
    stage('Test'){
      steps{
        pyhton test.py
      }
    }
    stage('Deploy'){
      steps{
        python deploy.py
      }
    }
  }
}
