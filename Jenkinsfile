pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Exemple') {
            steps {
                withGroovy {
                    sh 'groovy --version'
                }
            }
        }
    }
}