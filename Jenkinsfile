pipeline {
    agent any

    stages {
        stage("Init") {
            steps {
                sh '''
                echo "GIT_URL=https://github.com/BluDive-Technology-Limited/FlaskApp3.git" > context_env
                echo "GIT_BRANCH=origin/main" >> context_env
                '''
            }
        }
        stage('Trigger Base Pipeline') {
            steps {
                script {
                    def childBuild = build job: 'default_pipeline1', 
                        parameters: [
                            string(name: 'GIT_URL', value: 'https://github.com/BluDive-Technology-Limited/FlaskApp3.git'),
                            string(name: 'GIT_BRANCH', value: 'main')
                        ],
                        wait: true, // wait for child to complete
                        propagate: true // fail this build if child fails

                    // Store child build number
                    env.CHILD_BUILD_NUMBER = "${childBuild.number}"
                    echo "Triggered child build #${env.CHILD_BUILD_NUMBER}"
                }
            }
        }

        stage('Continue') {
            steps {
                echo 'Base pipeline has completed.'
            }
        }
    }
}
