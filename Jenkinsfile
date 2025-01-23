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


        //stage('Push to Docker Hub') {
          //  steps {
              // withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
//sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                //    sh 'docker push your-dockerhub-username/house-price-api'
              //  }
           // }
        //}

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
