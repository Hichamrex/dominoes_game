pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                sleep 201
                echo 'Front end builded'
            }
        }
        stage('Test') {
            steps {
                sleep 91 
                echo 'Front end test it'
            }
        }
        stage('Bolt Quality') {
          steps {
              sleep 180 
              echo 'Front end test it'
          }
        }
        stage('Realase') {
            steps {
                sleep 49   
                echo 'Front end release it'
            }
        }
    }
}
