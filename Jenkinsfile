pipeline {
    agent any

    environment {
        BUILD_DATE = "${new Date().format('yyyy-MM-dd')}"
        DOCKER_USERNAME = "rathan13"
        REPO_NAME = "myapp"
        BUILD_NUMBER = "6166122"
        DOCKER_IMAGE = "${DOCKER_USERNAME}/${REPO_NAME}"
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
                    sh "docker build -t myapp:latest ."
                }
            }
        }

        stage('Push to Docker Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'''
                    sh 'docker image tag myapp:latest rathan13/myapp:latest'
                    sh 'docker push rathan13/myapp:latest'
                    sh 'docker logout'
                }
            }
        }
            stage('Push to ECR') {
    steps {
        script {
            sh '''
            if ! command -v aws &> /dev/null
            then
                echo "AWS CLI not found! Please install it."
                exit 1
            fi

            aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 906385056045.dkr.ecr.ap-northeast-1.amazonaws.com

            docker build -t python-app .
            docker tag python-app:latest 906385056045.dkr.ecr.ap-northeast-1.amazonaws.com/python-app:latest
            docker push 906385056045.dkr.ecr.ap-northeast-1.amazonaws.com/python-app:latest
            '''
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
