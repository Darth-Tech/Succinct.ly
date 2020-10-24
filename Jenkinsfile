pipeline {
    environment {
        DOCKER_IMAGE = "devagastya0/text_summary"
        registryCredential = 'Docker Hub Dev'
        DOCKER_DEV_TAG = "latest"
	DOCKER_MASTER_TAG = "stable"
	DOCKER_FEATURE_TAG = "feature"
	FEATURE_BUILD = false
	DEV_BUILD = false
	STABLE_BUILD = false
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
		environment {
		    FEATURE_BUILD = false
		}
            steps{
                script {
		    sh"""
		    echo "Building docker image..."
		    cd text_summarizer
                    docker build -t $DOCKER_IMAGE:$DOCKER_FEATURE_TAG -f ./Dockerfile .
		    """
                    }
		withEnv(["FEATURE_BUILD=true"])
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
		withEnv(["DEV_BUILD=true"])
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
		withEnv(["STABLE_BUILD=true"])
                }
        }

        stage('Push builded image') {
		
            steps{
    		script {
			
			if (env.FEATURE_BUILD.toBoolean()==true) {
		    sh"""
		    echo "Pushing feature build into docker hub..."
                    docker push $DOCKER_IMAGE:$DOCKER_FEATURE_TAG
		    """
			}
			
			if (env.DEV_BUILD.toBoolean()==true) {
		    sh"""
		    echo "Pushing development build into docker hub..."
                    docker push $DOCKER_IMAGE:$DOCKER_DEV_TAG
		    """
			}
			
			if (env.STABLE_BUILD.toBoolean()==true) {
		    sh"""
		    echo "Pushing stable build into docker hub..."
                    docker push $DOCKER_IMAGE:$DOCKER_STABLE_TAG
		    """
				
			}
			
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
