pipeline {
    agent any
    stages {
        stage("Init") {
            steps {
                sh '''
                echo "GIT_URL=https://github.com/BluDive-Technology-Limited/FlaskApp1.git" > context_env
                echo "GIT_BRANCH=origin/main" >> context_env
                '''
            }
        }
        stage('Trigger Base Pipeline') {
            steps {
                build job: 'default_pipeline1', parameters: [
                    string(name: 'GIT_URL', value: 'https://github.com/BluDive-Technology-Limited/FlaskApp3.git'),
                    string(name: 'GIT_BRANCH', value: 'main')
                ]
            }
        }
        stage('Wait for Base Pipeline') {
            steps {
                waitUntil {
                    def job = Jenkins.instance.getItemByFullName('default_pipeline1')
                    return job.getLastBuild().isBuilding() == false
                }
            }
        }
    }
}
