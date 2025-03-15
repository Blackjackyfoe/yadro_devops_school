node {
    env.DOCKER_IMAGE = "penteka/currency_app"
    env.DOCKER_TAG = "${env.BUILD_NUMBER}" ?: "latest"
    env.DOCKER_CREDENTIALS = "docker-hub"

    //I don't want pipeline exited if stage failed
    stage('Clean Up Old Docker Images') {
        try {
            docker_clean_images()
        } catch (Exception e) {
            echo "Something went wrong with preparing a node for a work:"
            echo "${e.message}"
        }
    }

    //If scm is unavailable - pipeline failed
    try {
        stage('Checkout') {
            checkout scm
        }
    } catch (Exception e) {
        echo "Something went wrong with SCM. Check your creds."
        echo "${e.message}"
    }

    //I don't want pipeline exited if stage failed
    stage('Checking Dockerfile with Hadolint') {
        try {
            docker_hadolint_linter()
        } catch (Exception e) {
            currentBuild.result = 'UNSTABLE'
        }
    }

    try {
        stage('Build Docker Image') {
            docker_build("${env.DOCKER_IMAGE}", "${env.DOCKER_TAG}")
        }
    } catch (Exception e) {
        echo "Something went wrong with building a docker image:"
        echo "${e.message}"
    }

    stage('Scan Image with Trivy') {
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            docker_trivy_scan("${env.DOCKER_IMAGE}", "${env.DOCKER_TAG}")
        }
    }

    try {
        stage('Push Docker Image') {
            docker_push("${env.DOCKER_CREDENTIALS}", "${env.DOCKER_IMAGE}", "${env.DOCKER_TAG}")
        }
    } catch (Exception e) {
        echo "Something went wrong while pushing image to dockerhub:"
        echo "${e.message}"
    }
}
