pipeline {

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
        		doGenerateSubmoduleConfigurations: false, 
        		extensions: [[$class: 'CleanCheckout']],
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

        stage('Build Deploy Code') {
            when {
                branch '*/jenkins'
            }
            steps {
                sh """
		docker login --username devagastya0 --password 70ef5182-a60a-4de4-b449-73353e329dc6; 
                docker build ./text_summarizer/ -t devagastya0/text_summary;
		docker push devagastya0/text_summary; 
		echo "Built deploy code..."
                """
            }
        }

    }   
}
