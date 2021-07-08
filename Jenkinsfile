pipeline {
  agent any
  
  stages {

    stage('Test') {
      agent {
        docker { 
          image 'python:3.9.5' 
        }
      }
      
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python manage.py collectstatic --no-input'
      }
    }

    stage('Build') {
      
      steps {
        echo 'Running build'
      }
    }
  }
}