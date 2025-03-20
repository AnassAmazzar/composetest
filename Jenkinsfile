pipeline {
    agent any

    stages {
        stage('Check User') {
            steps {
                sh 'whoami'
            }
        }
        stage('check changes') {
            steps {
                sh 'which ansible' 
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -V'
            }
        }
        stage('Execute PlayBook') {
            steps {
                sh 'ansible-playbook ansible-playbook.yml'
            }
        }
        stage('Check docker conatiner') {
            steps {
                sh 'sudo docker ps'
            }
        }
    }
}