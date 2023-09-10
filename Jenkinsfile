pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                sleep 190
                echo 'Front end builded'
            }
        }
        stage('Test') {
            steps {
                sleep 100 
                echo 'Front end test it'
            }
        }
        stage('Bolt Quality') {
          steps {
              sleep 140  
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
