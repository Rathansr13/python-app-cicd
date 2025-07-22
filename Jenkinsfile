pipeline {
    agent any

    environment {
        BUILD_DATE = "${new Date().format('yyyy-MM-dd')}"
    }

    stages {

        stage('Checkout from Git') {
            steps {
                git url: 'https://github.com/Rathansr13/python-app-cicd', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                    """
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker logout
                    """
                }
            }
        }

        stage('Print Build Info') {
            steps {
                echo "Docker Image: ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                echo "Build Date: ${BUILD_DATE}"
                echo "Build Number: ${env.BUILD_NUMBER}"
            }
        }
        
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
