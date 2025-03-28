pipeline {
    agent any

    environment {
        SSH_PASSWORD = credentials('my-secret-password')
        SSH_USER = 'root'
        SSH_HOST = '192.168.8.101'
        SSH_PORT = '9950'
    }

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
                    sh """
                    ssh -i jenkins/.ssh/id_rsa root@192.168.8.101 -p 9950
                    whoami
                    pwd
                    exit
                    """
                    // sh 'whoami'
                    // sh 'ps -a'
                    // sh "ssh -vvv root@192.168.8.101 -p 9950 'whoami'"
                    //sh 'docker pull ghcr.io/anassamazzar/compose-test-web:latest'
                    //sh 'docker run -d -p 8077:5000 ghcr.io/anassamazzar/compose-test-web'
                    // sh """
                    // sshpass -p '${SSH_PASSWORD}' ssh -o StrictHostKeyChecking=no -p ${SSH_PORT} ${SSH_USER}@${SSH_HOST} 'whoami'
                    // """
                }
            }
        }
    }
}

// sh '''ssh -o StrictHostKeyChecking=no -p 2255 root@172.24.224.93 "pwd"'''
// sh 'docker stop compose-test-web'