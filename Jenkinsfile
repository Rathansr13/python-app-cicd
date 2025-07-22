pipeline {
    agent any

    environment {
        BUILD_DATE = "${new Date().format('yyyy-MM-dd')}"
        DOCKER_USERNAME = "rathan13"
        REPO_NAME = "myapp"                         // Name of your repo on Docker Hub
        BUILD_NUMBER = "6166122"
        DOCKER_IMAGE = "${DOCKER_USERNAME}/${REPO_NAME}" // Full Docker image name
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
                    sh "docker build -t  myapp:latest ."
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
               withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                 sh '''echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'''
                 sh 'docker image tag myapp:latest rathan13/myapp:latest'
                 sh 'docker push rathan13/myapp:latest'
                 sh 'docker logout'}

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
