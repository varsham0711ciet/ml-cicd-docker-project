# ML Iris Prediction - GitHub + CodePipeline + CodeDeploy + Docker

This project is a small machine-learning web application that predicts the Iris flower class from four measurements.

Pipeline:
GitHub -> CodePipeline -> CodeDeploy -> EC2 -> Docker -> Flask ML application

The EC2 instance builds the Docker image and runs the container during the CodeDeploy deployment.
