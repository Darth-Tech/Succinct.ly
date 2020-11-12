pipeline {
    environment {
        DOCKER_IMAGE = "devagastya0/text_summary"
        DOCKER_DEV_TAG = "latest"
        DOCKER_MASTER_TAG = "stable"
        
    }

    agent {
        node {
            label 'jenkins-slave'
        }
    }

    options {
        buildDiscarder logRotator( 
                    daysToKeepStr: '16', 
                    numToKeepStr: '10'
            )
    }

    stages {
        
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh """
                echo "Cleaned Up Workspace For Project"
                """
            }
        }

        stage('Code Checkout') {
            steps {
                checkout([
        		$class: 'GitSCM', 
        		branches: [[name: '*/jenkins']], 
        		userRemoteConfigs: [[credentialsId: "Dev's Darth Tech Creds", url: 'https://github.com/Darth-Tech/Succinct.ly.git']]
					   ])
            }
        }

        //stage(' Unit Testing') {
        //    steps {
        //        sh """
        //        echo "Running Unit Tests"
        //        """
        //    }
        //}

        //stage('Code Analysis') {
        //    steps {
        //        sh """
        //        echo "Running Code Analysis"
        //        """
        //    }
        //}
        
        stage('Building Development release') {
                when {
                    branch 'dev'
                }
                
                steps{
                    script {
                    
                        echo "Building development docker image..."
                    
                        dockerImage= docker.build(DOCKER_IMAGE + ":$DOCKER_DEV_TAG")
                    }
                    }
                }
        stage('Building stable release') {
                when {
                    branch 'master'
                }
                
                steps{
                    script {
                            echo "Building stable docker image..."
                            dockerImage= docker.build(DOCKER_IMAGE + ":$DOCKER_STABLE_TAG")
                        }
                
                    }
                }

    
        stage('Push development build image') {
            when {
                    branch 'dev'
                }
            steps{
                script {
                    sh"""
                    echo "Pushing development build into docker hub..."
                            docker push $DOCKER_IMAGE:$DOCKER_DEV_TAG
                    """
                        
                }
            }
        }
        stage('Push stable image') {
            when {
                    branch 'master'
                }
            steps{
                script {
                    sh"""
                    echo "Pushing stable build into docker hub..."
                            docker push $DOCKER_IMAGE:$DOCKER_MASTER_TAG
                    """
                        
                }
            }
        }

    }
}
               
