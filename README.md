The machine learning technology that used in CI/CD model:

-   **Flask**: A micro web framework written in Python.
-   **Docker**: Used to package the application and its dependencies into isolated containers.
-   **Github**: A popular platform for version control and hosting the application's source code.
-   **Google Cloud Build**: A CI/CD management service provided by Google Cloud Platform.
-   **Google Cloud Run**: A serverless computing service used to deploy and run applications in containers.

## Technology Used

There are five technologies we use in the **SoulSync** Machine Learning Operations Deployment with CI/CD: Flask, Docker, Github, Google Cloud Build, Google Cloud Run.

### Flask

<img src="https://flask.palletsprojects.com/en/stable/_images/flask-horizontal.png" width="300" height="75"/>

Flask can be used to deploy a machine learning model:
- *Model Training*: Train your machine learning model using libraries like TensorFlow. This involves feeding the model with relevant data and optimizing it to make accurate predictions.
- *Flask Integration*: Integrate the trained model into a Flask application. Define API endpoints that will receive input data and return model predictions.
- *Request Handling*: Define request handling functions in Flask that will receive incoming requests containing input data. These functions will preprocess the input, pass it to the trained model for prediction, and return the model's response.
- *API Documentation*: Flask automatically generates documentation for your API based on type annotations and function descriptions. This documentation provides details on the API endpoints, expected input formats, and response structures.
- *Deployment*: Deploy the Flask application to a hosting platform or server. Platforms like Google Cloud Run or Heroku make it easy to deploy and manage Flask applications.
- *Testing and Monitoring*: Test the deployed API to ensure it's functioning as expected. Monitor the API's performance, track usage metrics, and log any errors or issues for debugging and improvement.

My endpoint:

```YAML
GET /: This is the root endpoint that returns a default response when accessed with a GET request. It can be used for testing or to provide general information about the API. Ex "Welcome to the SoulSync API".

POST /prediction/: This endpoint is used for making predictions. It expects a JSON payload containing the input data for the model. The input data is then processed and passed to the trained model for prediction. The prediction result is returned as a JSON response.
```

Docs: [Flask-docs](https://flask.palletsprojects.com/en/stable/)

### Docker 

<img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" width="100"/>

The provided code is a Dockerfile, which is used to build a Docker image for the deployment of a machine learning model using Flask. Here's a brief explanation of the different sections in the Dockerfile:

```YAML
FROM python:3.9-slim : This line specifies the base image for the Docker container. In this case, it's Python 3.9 with a slim version, which is a small and lightweight image.
WORKDIR /app : This line sets the working directory inside the container to /app. This is where the application code will be copied.
COPY . /app : This line copies the contents of the current directory into the /app directory inside the container. This includes the Dockerfile, requirements.txt, and the main.py file.
RUN pip install --no-cache-dir -U pip : This line installs the pip package manager inside the container. It's used to ensure that the latest version of pip is installed.
RUN pip install -r requirements.txt : This line installs the dependencies listed in the requirements.txt file using the pip package manager inside the container.
EXPOSE 8080 : This line exposes port 8080 on the container. This is the port that the Flask application will listen on.
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080"] : This line specifies the command to run when the container is started. It starts the Flask application using the gunicorn web server, listening on port 8080.
```

The Dockerfile sets up a Python environment, installs the required dependencies specified in the requirements.txt file, and copies the application code into the Docker image. When the Docker container is run, it will execute the main.py file, which is assumed to contain the Flask application code for serving the machine learning model.

Docs:
[docker-docs](https://docs.docker.com/)

### Github

<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="100"/>

GitHub is utilized to create triggers in Google Cloud Build for deploying a machine learning model using CI/CD on Cloud Run. The repository at  **`https://github.com/Soul-Sync/soul-sync-model-endpoint`** contains the necessary code and configuration files for the deployment process. With the triggers set up, any changes or updates made to the repository will automatically trigger the CI/CD pipeline in Google Cloud Build, which will build and deploy the model to Cloud Run based on the defined configuration. This integration allows for streamlined development, version control, and automated deployment of the machine learning model using the power of GitHub and Google Cloud technologies.

Docs: [github-docs](https://docs.github.com/en)

### Google Cloud Build 

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSs3WdMUSzoZGaJjfWjioiK8oQSNFuNUdlty1ocOgsceQ&s" width="100"/>

Google Cloud Build is a CI/CD management service provided by Google Cloud Platform. It is used to automate the process of building, testing, and deploying applications. In the given steps, Cloud Build is utilized to automate the deployment of a machine learning model to Google Cloud Run.

The provided steps outline the CI/CD pipeline for deploying the model:

1. Step 1: Building the container image - The Docker image is built using the specified Dockerfile, and the resulting image is tagged with the project ID and image name.
2. Step 2: Pushing the container image to Container Registry - The built container image is pushed to the Container Registry, making it accessible for deployment.
3. Step 3: Deploying the container to Cloud Run - The container image is deployed to Cloud Run, specifying the image location, region, platform, and authentication settings.
   
To create a trigger for this CI/CD pipeline, the trigger name would be **`soulsync-model-endpoint`** . This trigger can be set up in Google Cloud Build to monitor changes in the repository or other specified conditions. Once the trigger is activated, it will initiate the defined CI/CD pipeline, automatically building and deploying the model to Cloud Run.

Google Cloud Build is used to automate the deployment process, from building the container image to deploying it to Cloud Run, enabling efficient and streamlined CI/CD for the machine learning model.

Docs: [cloud-build-docs](https://cloud.google.com/build/docs)

### Google Cloud Run

<img src="https://static-00.iconduck.com/assets.00/google-cloud-run-icon-512x460-knkc4eyx.png" width="100"/>

Google Cloud Run is a serverless compute service used to run containerized applications. In this implementation, Cloud Run is used to run a container that contains a machine learning model and an API endpoint. This allows for easy and scalable exposure of the model through an HTTP API.

The service or endpoint name in this case is "soulsync-model-endpoint". This is the name given to the deployed service on Cloud Run. It will expose the machine learning model and API through an HTTP endpoint, allowing external clients to make predictions or interact with the model.

Docs: [cloud-run-docs](https://cloud.google.com/run/docs)

# How to use
You can try
```YAML
https://soulsync-model-endpoint-451042832834.asia-southeast2.run.app/
```