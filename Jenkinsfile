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

        
        stage('Print Build Info') {
            steps {
                echo "Build Number: ${env.BUILD_NUMBER}"
                echo "Build Date: ${env.BUILD_DATE}"
                echo "Jenkins URL: ${env.JENKINS_URL}"
                echo "Build URL: ${env.BUILD_URL}"
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
