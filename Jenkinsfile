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
        stage('Check Compose file') {
            steps {
                sh 'ls -l docker-compose.yml'
            }
        }
        stage('Check docker conatiner') {
            steps {
                sh 'docker ps'
            }
        }
    }
}