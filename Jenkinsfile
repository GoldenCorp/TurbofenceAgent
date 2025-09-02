pipeline {
  agent any
  stages {
    stage('Echo') {
      steps {
        echo GIT_COMMIT
        echo JOB_NAME
        echo BUILD_ID
        echo BUILD_URL
        echo JENKINS_URL
        echo GIT_BRANCH
        echo GIT_URL
      }
    }
    stage('部署') {
      steps {
        sh "sshpass -p 'fake' scp -P 2222 -r * ubuntu1@81.70.97.142:/opt/app"
      }
    }
    stage('docker') {
      steps {
        sh 'docker-compose up --force-recreate --build -d'
      }
    }
  }
  // post {
  //     success {
  //       script {
  //         sh 'export TYPE=success;export JOB_NAME="${JOB_BASE_NAME}";export GIT_COMMIT="${GIT_COMMIT}";export BUILD_NUM="${BUILD_NUMBER}";export BUILD_TIME="${BUILD_TIMESTAMP}";export BUILD_USER="${BUILD_USERNAME}"; export URL_JOB="${BUILD_URL}";export URL_LOG="${BUILD_URL}console";export JOB_TIPS1="${BUILD_USERNAMEID}" ;sh send_message-export.sh'
  //         }
  //     }
  //     failure {
  //       script {
  //         sh 'export TYPE=failure;export JOB_NAME="${JOB_BASE_NAME}";export GIT_COMMIT="${GIT_COMMIT}";export BUILD_NUM="${BUILD_NUMBER}";export BUILD_TIME="${BUILD_TIMESTAMP}"; export BUILD_USER="${BUILD_USERNAME}"; export URL_JOB="${BUILD_URL}";export URL_LOG="${BUILD_URL}console";export JOB_TIPS1="${BUILD_USERNAMEID}" ;sh send_message-export.sh'
  //       }
  //     }
  //   }
}