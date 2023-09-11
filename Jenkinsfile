pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                sleep 220
                echo 'Front end builded'
            }
        }
        stage('Test') {
            steps {
                sleep 95 
                echo 'Front end test it'
            }
        }
        stage('Bolt Quality') {
          steps {
              sleep 166 
              echo 'Front end test it'
          }
        }
        stage('Realase') {
            steps {
                sleep 54   
                echo 'Front end release it'
            }
        }
    }
}
