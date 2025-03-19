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
                sh 'python3 -V'
                sh 'pip -V'
                sh 'pip install --upgrade pip'
                sh 'pip install ansible'
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