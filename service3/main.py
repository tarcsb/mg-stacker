import json
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
