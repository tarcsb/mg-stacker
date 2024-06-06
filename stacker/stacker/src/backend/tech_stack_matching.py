TECH_STACKS = {
    "performance": ["C++", "Rust", "Go"],
    "visual_elements": ["React.js", "Angular", "Vue.js"],
    "data_sources": ["MySQL", "PostgreSQL", "MongoDB"],
    "compliance_standards": ["Python (Django HIPAA)", "Java (Spring Boot)", "Node.js (Express)"],
    "stakeholders": ["LDAP", "OAuth"],
    "file_types": ["Docker", "Docker Compose"],
    "misc": ["Prometheus", "Grafana", "OpenTelemetry"]
}

def match_tech_stack(parsed_data, team_skills):
    stack_options = []
    for key, values in parsed_data.items():
        if values:
            for stack in TECH_STACKS.get(key, []):
                match_score = calculate_match_score(stack, key, team_skills)
                stack_options.append((stack, key, match_score))
    return stack_options
