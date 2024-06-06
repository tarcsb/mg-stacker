import os

configs = {
    "Jenkinsfile": """pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        sh 'pip install -r requirements.txt'
                    }
                    if (fileExists('src/frontend/package.json')) {
                        sh 'cd src/frontend && npm install'
                    }
                }
            }
        }
        stage('Lint Backend') {
            steps {
                sh 'flake8 src/backend'
            }
        }
        stage('Lint Frontend') {
            steps {
                sh 'cd src/frontend && npm run lint'
            }
        }
        stage('Unit Tests Backend') {
            steps {
                sh 'pytest --cov=src/backend tests/backend'
            }
            post {
                always {
                    junit 'tests/backend/junit.xml'
                    publishHTML(target: [
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        stage('Unit Tests Frontend') {
            steps {
                sh 'cd src/frontend && npm test -- --coverage'
            }
            post {
                always {
                    junit 'src/frontend/junit.xml'
                    publishHTML(target: [
                        reportDir: 'src/frontend/coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/coverage/**', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
""",

    ".github/workflows/ci.yml": """name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install Node.js dependencies
      run: |
        cd src/frontend
        npm install

    - name: Lint Python code
      run: |
        pip install flake8
        flake8 src/backend

    - name: Lint JavaScript code
      run: |
        cd src/frontend
        npm run lint

    - name: Test Python code
      run: |
        pip install pytest pytest-cov
        pytest --cov=src/backend tests/backend

    - name: Test JavaScript code
      run: |
        cd src/frontend
        npm test -- --coverage

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v2
      with:
        files: |
          coverage.xml
          src/frontend/coverage/lcov.info
        flags: unittests
        name: codecov-umbrella
        fail_ci_if_error: true

    - name: Upload Artifacts
      uses: actions/upload-artifact@v2
      with:
        name: coverage-reports
        path: |
          coverage.xml
          src/frontend/coverage/lcov.info
""",

    ".flake8": """[flake8]
max-line-length = 88
extend-ignore = E203
""",

    "src/frontend/.eslintrc.json": """{
    "env": {
        "browser": true,
        "es2021": true,
        "node": true
    },
    "extends": [
        "eslint:recommended",
        "plugin:react/recommended",
        "plugin:@typescript-eslint/recommended"
    ],
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "ecmaFeatures": {
            "jsx": true
        },
        "ecmaVersion": 12,
        "sourceType": "module"
    },
    "plugins": [
        "react",
        "@typescript-eslint"
    ],
    "rules": {
        "semi": ["error", "always"],
        "quotes": ["error", "single"]
    }
}
""",

    "src/frontend/package.json": """{
  "scripts": {
    "lint": "eslint 'src/**/*.{js,jsx,ts,tsx}'",
    "lint:fix": "eslint 'src/**/*.{js,jsx,ts,tsx}' --fix"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "src/**/*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "git add"
    ],
    "src/**/*.py": [
      "flake8",
      "git add"
    ]
  }
}
""",

    "build_info.sh": """#!/bin/bash

echo "Build Date: $(date)" > build_info.txt
echo "Commit: $(git rev-parse HEAD)" >> build_info.txt
echo "Branch: $(git rev-parse --abbrev-ref HEAD)" >> build_info.txt
""",

    "Dockerfile": """# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "src/backend/app.py"]
""",

    "src/frontend/Dockerfile": """# Use the official Node.js image from the Docker Hub
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files into the container at /app
COPY package*.json ./

# Install the Node.js dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Build the application
RUN npm run build

# Run the application
CMD ["npm", "start"]
""",

    "docker-compose.yml": """version: '3.7'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: development

  frontend:
    build:
      context: ./src/frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: development
    depends_on:
      - backend
""",

    "k8s/deployment.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: stacker
spec:
  replicas: 2
  selector:
    matchLabels:
      app: stacker
  template:
    metadata:
      labels:
        app: stacker
    spec:
      containers:
      - name: backend
        image: stacker-backend:latest
        ports:
        - containerPort: 5000
        env:
        - name: FLASK_ENV
          value: development
      - name: frontend
        image: stacker-frontend:latest
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: development
""",

    "k8s/service.yaml": """apiVersion: v1
kind: Service
metadata:
  name: stacker
spec:
  selector:
    app: stacker
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: LoadBalancer
"""
}

def create_project_structure():
    for file_path, content in configs.items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully.")
