pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'docker ps'
            }
        }
        stage('Execute PlayBook') {
            steps {
                sh 'ansible-playbook ansible-playbook.yml'
            }
        }
        stage('Check docker conatiner') {
            steps {
                sh 'docker ps'
            }
        }
    }
}