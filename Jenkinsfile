pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
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