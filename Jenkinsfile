pipeline {
    agent any

    stages {
        stage('Checkout') {
 steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], credentialsId: 'GitHub', url: 'https://github.com/Mahdi-Ghorbel-10/MLops-house-prediction.git']) 
            }        }

     stage('Build') {
    steps {
        sh '''#!/bin/bash
            python3 -m venv .venv
            source .venv/bin/activate && pip install -r requirements.txt && docker build -t ghorbelmahdi/house-price-api .
        '''
                }
            }


                stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                   sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                   docker push ghorbelmahdi/house-price-apilatest
                      '''
}

            }
        }
        stage('Deploy') {
            steps {
                //  Example Kubernetes deployment (adapt as needed)
                //  withCredentials([kubernetes(credentialsId: 'your-kubernetes-credentials', serverUrl: 'your-kubernetes-server-url')]) {
                //     sh 'kubectl apply -f deployment.yaml'
                //  }

                echo "Deployment steps go here. Adapt to your target environment (e.g., Kubernetes, AWS, Azure)."

            }
        }
    }
}
