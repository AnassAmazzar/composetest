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
        stage('Remote acces') {
            steps {
                sshagent(['mod-prod-dind']) {
                    sh "ssh root@192.168.8.101 -p 9950 'whoami'"
                    sh 'whoami'
                    sh 'ps -a'
                    //sh 'docker pull ghcr.io/anassamazzar/compose-test-web:latest'
                    //sh 'docker run -d -p 8077:5000 ghcr.io/anassamazzar/compose-test-web'
                }
            }
        }
    }
}

// sh '''ssh -o StrictHostKeyChecking=no -p 2255 root@172.24.224.93 "pwd"'''
// sh 'docker stop compose-test-web'