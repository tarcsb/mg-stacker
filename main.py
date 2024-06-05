import os
import json
import logging

logging.basicConfig(level=logging.INFO)

class ProjectGenerator:
    def __init__(self):
        self.load_configurations()

    def load_configurations(self):
        with open('stacks/stacks.json', 'r') as f:
            self.stacks = json.load(f)
        with open('requirements/requirements.json', 'r') as f:
            self.requirements = json.load(f)

    def create_file(self, path, content):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            file.write(content)
        logging.info(f"Created file: {path}")

    def create_service(self, service_name, stack_key):
        stack = self.stacks[stack_key]
        logging.info(f"Creating service {service_name} with stack {stack_key}")

        frontend_path = os.path.join(service_name, 'frontend', 'package.json')
        self.create_file(frontend_path, '{}')

        backend_path = os.path.join(service_name, 'backend', 'package.json')
        self.create_file(backend_path, '{}')

        self.create_file(os.path.join(service_name, 'backend', 'server.js'), self.generate_server_js())
        self.create_file(os.path.join(service_name, 'backend', 'server.test.js'), self.generate_server_test_js())
        self.create_file(os.path.join(service_name, 'main.py'), self.generate_main_py())

        for req_file, req_content in self.requirements.items():
            self.create_file(os.path.join(service_name, 'requirements', req_file), '\n'.join(req_content))

        readme_content = self.generate_readme(service_name, stack)
        self.create_file(os.path.join(service_name, 'README.md'), readme_content)

    def generate_server_js(self):
        return """const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const winston = require('winston');
const morgan = require('morgan');
const tracer = require('jaeger-client').initTracer;
const promClient = require('prom-client');
const AWS = require('aws-sdk');
const { AzureKeyVaultSecret } = require('azure-sdk');

const app = express();
app.use(cors());
app.use(express.json());
app.use(morgan('combined'));

mongoose.connect('mongodb://localhost:27017/yourdbname', { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
"""

    def generate_server_test_js(self):
        return """const request = require('supertest');
const app = require('./server'); // Assuming your Express app is exported from server.js

describe('GET /', () => {
  it('should return Hello World', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toEqual(200);
    expect(res.text).toBe('Hello World!');
  });
});
"""

    def generate_main_py(self):
        return """import json
import os

# List of common stacks with optional addons
stacks = {
    'MERN': {
        'frontend': 'React',
        'backend': 'Node.js',
        'database': 'MongoDB',
        'libraries': ['Express.js'],
        'addons': {
            'observability': ['winston', 'morgan'],
            'traceability': ['jaeger-client', 'opentracing'],
            'system_awareness': ['prom-client'],
            'cloud_deployment': ['aws-sdk', 'azure-sdk'],
            'docker': True,
            'jenkins': True,
            'kubernetes': True
        }
    }
}

# Recommendation engine
def recommend_stack(requirements):
    keywords = requirements.lower().split()
    for app_type, stacks_list in stacks.items():
        if any(keyword in app_type for keyword in keywords):
            return stacks_list[0]  # Just picking the first one for simplicity

def main():
    requirements = 'e-commerce'  # Example requirement for stack recommendation
    stack = recommend_stack(requirements)
    print(stack)

if __name__ == "__main__":
    main()
"""

    def generate_readme(self, service_name, stack):
        return f"""
# {service_name.capitalize()} Setup

This project is built using the following stack:

- **Frontend:** {stack['frontend']}
- **Backend:** {stack['backend']}
- **Database:** {stack['database']}
- **Libraries:** {', '.join(stack['libraries'])}

## Getting Started

### Prerequisites

- Node.js (for Node.js backend)
- MongoDB (for MERN stack)
- Java and Maven (for Spring Boot backend)
- Go (for Go backend)
- Qt (for C++ Qt backend)

### Installation

1. Clone the repository:

\`\`\`sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
\`\`\`

2. Install dependencies:

\`\`\`sh
# For React frontend
cd frontend
npm install

# For Node.js backend
cd ../backend
npm install

# For Spring Boot backend
cd ../backend
mvn install

# For Go backend
cd ../backend
go mod init
go mod tidy

# For C++ Qt backend
cd ../backend
# Install necessary Qt libraries
\`\`\`

### Running the application

\`\`\`sh
# Start React frontend
cd frontend
npm start

# Start Node.js backend
cd ../backend
node server.js

# Start Spring Boot backend
cd ../backend
mvn spring-boot:run

# Start Go backend
cd ../backend
go run main.go

# Start C++ Qt application
cd ../backend
./Demo
\`\`\`

### Running tests

\`\`\`sh
# Run React tests
cd frontend
npm test

# Run Node.js tests
cd ../backend
npm test

# Run Spring Boot tests
cd ../backend
mvn test

# Run Go tests
cd ../backend
go test

# Run C++ tests
cd ../backend
./DemoTest
\`\`\`
"""

def main():
    generator = ProjectGenerator()
    services = ["service1", "service2", "service3"]
    for service in services:
        generator.create_service(service, "MERN")

if __name__ == "__main__":
    main()
