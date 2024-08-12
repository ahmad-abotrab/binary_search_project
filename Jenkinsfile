pipeline {
    agent {
        docker {
            image 'python:3.11' // Using Python 3.11 Docker image
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout code from the repository
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt' // Install dependencies (if any)
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests' // Run all tests in the 'tests' directory
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
