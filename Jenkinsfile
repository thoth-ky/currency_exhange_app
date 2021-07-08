pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'pipenv run python manage.py collectstatic --no-input'
      }
    }

  }
}