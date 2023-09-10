pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                sleep 195
                echo 'Front end builded'
            }
        }
        stage('Test') {
            steps {
                sleep 99 
                echo 'Front end test it'
            }
        }
        stage('Bolt Quality') {
          steps {
              sleep 160  
              echo 'Front end test it'
          }
        }
        stage('Realase') {
            steps {
                sleep 41   
                echo 'Front end release it'
            }
        }
    }
}
