pipeline {
  agent {
    docker {
      image 'python:3.9.5'
    }

  }
  stages {
    stage('Test') {
      agent {
        docker {
          label 'docker'
          image 'python:3.9.5'
        }

      }
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python manage.py collectstatic --no-input'
      }
    }

  }
}