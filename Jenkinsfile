pipeline {
    agent any  // This means the pipeline can run on any available agent

    environment {
        SONARQUBE_SERVER = 'Sonarscanner'  // Name of your SonarQube server configuration in Jenkins
        SONAR_TOKEN = credentials('SonarQube-Token-1')  // Use Jenkins credentials for SonarQube token
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                git url: 'https://github.com/riti-1904/CoverageUnitTesting.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                bat """
                    mvn clean package ^
                    -Dsonar.projectKey=Unittestpipeline ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000 ^
                    -Dsonar.token=$SONAR_TOKEN
                """
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat 'mvn test'  // Runs the unit tests on Windows
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    echo 'Starting SonarQube analysis...'
                    withSonarQubeEnv(SONARQUBE_SERVER) {  // Use the configured SonarQube server
                        bat 'mvn sonar:sonar -Dsonar.login=$SONAR_TOKEN'  // Run SonarQube analysis on Windows
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            junit '**/target/surefire-reports/*.xml'  // Archive test results
        }
    }
}

