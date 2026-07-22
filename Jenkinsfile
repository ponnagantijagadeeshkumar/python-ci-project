pipeline {
    agenet any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code"
            }
        }

        stage("Install Dependencies") {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run application') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest'
            }
        }

        post {
            success {
                echo "pipeline completed successfully"
            }
        }

        failure {
            echo "pipeline failed"
        }

        always {
            echo "Build finished"
        }
    }
}