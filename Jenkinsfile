pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh '''apt-get install python3-dev python3 -y && \\
python3 install -r requirements.txt && \\
python manage.py collectstatic --no-input'''
      }
    }

  }
}