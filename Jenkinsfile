pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout code from the repository
            }
        }

        stage('Build and Test in Docker') {
            steps {
                script {
                    sh '''
                    docker run --rm -v $PWD:/workspace -w /workspace python:3.11 \
                    sh -c "pip3 install -r requirements.txt && python3 -m unittest discover -s tests"
                    '''
                }
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
