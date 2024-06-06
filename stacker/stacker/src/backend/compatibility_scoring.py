COMPATIBILITY_SCORES = {
    "C++": 90,
    "Rust": 85,
    "Go": 80,
    "React.js": 95,
    "Angular": 85,
    "Vue.js": 80,
    "MySQL": 90,
    "PostgreSQL": 95,
    "MongoDB": 85,
    "Python (Django HIPAA)": 95,
    "Java (Spring Boot)": 90,
    "Node.js (Express)": 85,
    "LDAP": 80,
    "OAuth": 85,
    "Docker": 95,
    "Docker Compose": 90,
    "Prometheus": 85,
    "Grafana": 90,
    "OpenTelemetry": 85
}

def calculate_match_score(stack, category, team_skills):
    team_skill_scores = {
        "C++": 75 if "C++" in team_skills else 50,
        "Rust": 70 if "Rust" in team_skills else 50,
        "Go": 65 if "Go" in team_skills else 50,
        "React.js": 80 if "React.js" in team_skills else 50,
        "Angular": 75 if "Angular" in team_skills else 50,
        "Vue.js": 70 if "Vue.js" in team_skills else 50,
        "MySQL": 85 if "MySQL" in team_skills else 50,
        "PostgreSQL": 90 if "PostgreSQL" in team_skills else 50,
        "MongoDB": 80 if "MongoDB" in team_skills else 50,
        "Python (Django HIPAA)": 95 if "Python" in team_skills else 50,
        "Java (Spring Boot)": 90 if "Java" in team_skills else 50,
        "Node.js (Express)": 85 if "Node.js" in team_skills else 50,
        "LDAP": 75 if "LDAP" in team_skills else 50,
        "OAuth": 75 if "OAuth" in team_skills else 50,
        "Docker": 90 if "Docker" in team_skills else 50,
        "Docker Compose": 85 if "Docker Compose" in team_skills else 50,
        "Prometheus": 80 if "Prometheus" in team_skills else 50,
        "Grafana": 85 if "Grafana" in team_skills else 50,
        "OpenTelemetry": 80 if "OpenTelemetry" in team_skills else 50
    }
    return 0.5 * COMPATIBILITY_SCORES[stack] + 0.5 * team_skill_scores[stack]
