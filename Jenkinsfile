pipeline {
    environment {
        DOCKER_IMAGE = "devagastya0/text_summary"
        registryCredential = 'Docker Hub Dev'
        DOCKER_DEV_TAG = "latest"
	DOCKER_MASTER_TAG = "stable"
	DOCKER_FEATURE_TAG = "feature"
	
    }

    agent {
        node {
            label 'master'
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
		    echo "Building docker image..."
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
		    echo "Building docker image..."
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
		    echo "Building docker image..."
		    cd text_summarizer
                    docker build -t $DOCKER_IMAGE:$DOCKER_MASTER_TAG -f ./Dockerfile .
		    
		    """
                    }
                }
        }

        stage('Deploy Image') {
		
            steps{
    		script {
                    docker.withRegistry( '', registryCredential ) {
                    
                    docker_image.push()
                    }
                }	
		
                
            }
        }

        //stage('Build Deploy Code') {
        //    when {
        //        branch 'jenkins'
        //    }
        //   steps {
        //        sh """
		//docker login --username devagastya0 --password "70ef5182-a60a-4de4-b449-73353e329dc6"; 
        //        docker build ./text_summarizer/ -t devagastya0/text_summary:latest;
		//docker push devagastya0/text_summary; 
		//echo "Built deploy code..."
        //        """
        //    }
        //}

    }   
}
