pipeline {
  agent {
    node {
      label 'myAgent'
    }

  }
  stages {
    stage('Test') {
      steps {
        sh 'pipenv run python manage.py collectstatic --no-input'
      }
    }

  }
}