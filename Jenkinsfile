Pipeline {
	agent {
		label 'TestAgent'} {
		stages {
			stage ('intimation on push in test branch') {
				step { echo "push hogaya hai bhai test mai" }
				}
			stage ( 'store git file in Jenkins' ) {
				step { checkout scm }
				}
			stage ('copy to test server') {
				step { sh 'cp -r ${WORKSPACE} /opt/test-server/}
				}
		}
	}
}
