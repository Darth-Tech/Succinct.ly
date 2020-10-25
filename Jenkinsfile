pipeline {
    environment {
        DOCKER_IMAGE = "devagastya0/text_summary"
        DOCKER_DEV_TAG = "latest"
        DOCKER_MASTER_TAG = "stable"
        DOCKER_FEATURE_TAG = "feature"
        FEATURE_BUILD = false
        DEV_BUILD = false
        STABLE_BUILD = false
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
        stage('Building new feature release') {
            when {
                    branch 'feature'
                }
            
            steps{
                script {
                    sh"""
                    echo "Building feature docker image..."
                    cd text_summarizer
                            docker build -t $DOCKER_IMAGE:$DOCKER_FEATURE_TAG -f ./Dockerfile .
                    """
            
                    }
                    }
            
                }
        stage('Building Development release') {
                when {
                    branch 'dev'
                }
                
                steps{
                    script {
                    sh"""
                    echo "Building development docker image..."
                    cd text_summarizer
                            docker build -t $DOCKER_IMAGE:$DOCKER_DEV_TAG -f ./Dockerfile .
                    """
                
                    }
                    }
                }
        stage('Building stable release') {
                when {
                    branch 'master'
                }
                
                steps{
                    script {
                        sh"""
                        echo "Building stable docker image..."
                        cd text_summarizer
                                docker build -t $DOCKER_IMAGE:$DOCKER_MASTER_TAG -f ./Dockerfile .
                        """
                        }
                
                    }
                }

        stage('Push feature build image') {
        
            steps{
                script {
                    sh"""
                    echo "Pushing feature build into docker hub..."
                            docker push $DOCKER_IMAGE:$DOCKER_FEATURE_TAG
                    """
                        
                }
            }
        }
        stage('Push development build image') {
        
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
               