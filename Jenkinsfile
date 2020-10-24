pipeline {
    environment {
        DOCKER_IMAGE_TAG = "devagastya0/text_summary:latest"
        registryCredential = 'Docker Hub Dev'
        dockerImage = ''
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

        stage('Code Analysis') {
            steps {
                sh """
                echo "Running Code Analysis"
                """
            }
        }
        stage('Building image') {
            when {
                branch 'jenkins'
            }
            
            steps{
                script {
		    sh"""
		    echo "Building docker image..."
                    docker build -t devagastya0/text_summary:latest -f ./text_summarizer/Dockerfile .
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
