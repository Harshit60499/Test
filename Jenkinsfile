pipeline {
	agent {
		label 'TestAgent'} 
		stages {
			stage ('intimation on push in test branch') {
				steps { echo "push hogaya hai bhai test mai" }
				}
			stage ('store git file in Jenkins') {
				steps { checkout scm }
				}
			stage ('copy to test server') {
				steps { sh 'cp -r ${WORKSPACE} /opt/test-server/'}
				}
	}
}
