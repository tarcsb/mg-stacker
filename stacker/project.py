import os

project_structure = {
    "stacker/src/backend/__init__.py": "# Initialize backend package\n",
    "stacker/src/backend/nlp_parsing.py": """import spacy

def parse_user_input(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    parsed_data = {
        "performance": [],
        "visual_elements": [],
        "data_sources": [],
        "compliance_standards": [],
        "stakeholders": [],
        "file_types": [],
        "misc": []
    }
    for ent in doc.ents:
        if ent.label_ == "PERFORMANCE":
            parsed_data["performance"].append(ent.text)
        elif ent.label_ == "VISUAL":
            parsed_data["visual_elements"].append(ent.text)
        elif ent.label_ == "DATA":
            parsed_data["data_sources"].append(ent.text)
        elif ent.label_ == "COMPLIANCE":
            parsed_data["compliance_standards"].append(ent.text)
        elif ent.label_ == "STAKEHOLDER":
            parsed_data["stakeholders"].append(ent.text)
        elif ent.label_ == "FILE":
            parsed_data["file_types"].append(ent.text)
        else:
            parsed_data["misc"].append(ent.text)
    return parsed_data
""",
    "stacker/src/backend/tech_stack_matching.py": """TECH_STACKS = {
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
""",
    "stacker/src/backend/compatibility_scoring.py": """COMPATIBILITY_SCORES = {
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
""",
    "stacker/src/backend/sorting.py": """def sort_tech_stacks(stack_options, criteria="overall"):
    if criteria == "team_skills":
        sorted_stacks = sorted(stack_options, key=lambda x: x[2], reverse=True)
    elif criteria == "performance":
        sorted_stacks = sorted(stack_options, key=lambda x: x[2], reverse=True)
    else:
        sorted_stacks = sorted(stack_options, key=lambda x: x[2], reverse=True)
    return sorted_stacks
""",
    "stacker/src/frontend/public/index.html": """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Stacker</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
""",
    "stacker/src/frontend/src/components/Stepper.js": """import React from 'react';

const Stepper = () => {
  return (
    <div>
      <h2>Stepper Component</h2>
      {/* Stepper logic goes here */}
    </div>
  );
};

export default Stepper;
""",
    "stacker/src/frontend/src/components/NotificationSettings.js": """import React from 'react';

const NotificationSettings = () => {
  return (
    <div>
      <h2>Notification Settings</h2>
      {/* Notification settings logic goes here */}
    </div>
  );
};

export default NotificationSettings;
""",
    "stacker/src/frontend/src/components/SecuritySettings.js": """import React from 'react';

const SecuritySettings = () => {
  return (
    <div>
      <h2>Security Settings</h2>
      {/* Security settings logic goes here */}
    </div>
  );
};

export default SecuritySettings;
""",
    "stacker/src/frontend/src/context/NotificationContext.js": """import React, { createContext, useState } from 'react';

export const NotificationContext = createContext();

export const NotificationProvider = ({ children }) => {
  const [notifications, setNotifications] = useState([]);

  const addNotification = (notification) => {
    setNotifications([...notifications, notification]);
  };

  const removeNotification = (id) => {
    setNotifications(notifications.filter(notification => notification.id !== id));
  };

  return (
    <NotificationContext.Provider value={{ notifications, addNotification, removeNotification }}>
      {children}
    </NotificationContext.Provider>
  );
};
""",
    "stacker/src/frontend/src/hooks/useShortKeys.js": """import { useEffect } from 'react';

const useShortKeys = (shortKeys) => {
  useEffect(() => {
    const handleKeyDown = (event) => {
      const key = `${event.ctrlKey ? 'Ctrl+' : ''}${event.key}`;
      if (shortKeys[key]) {
        event.preventDefault();
        shortKeys[key]();
      }
    };

    window.addEventListener('keydown', handleKeyDown);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [shortKeys]);
};

export default useShortKeys;
""",
    "stacker/src/frontend/src/pages/HomePage.js": """import React from 'react';

const HomePage = () => {
  return (
    <div>
      <h2>Home Page</h2>
      {/* Home page content goes here */}
    </div>
  );
};

export default HomePage;
""",
    "stacker/src/frontend/src/pages/Dashboard.js": """import React from 'react';

const Dashboard = () => {
  return (
    <div>
      <h2>Dashboard</h2>
      {/* Dashboard content goes here */}
    </div>
  );
};

export default Dashboard;
""",
    "stacker/src/frontend/src/App.js": """import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { NotificationProvider } from './context/NotificationContext';
import Stepper from './components/Stepper';
import NotificationSettings from './components/NotificationSettings';
import SecuritySettings from './components/SecuritySettings';
import HomePage from './pages/HomePage';
import Dashboard from './pages/Dashboard';
import useShortKeys from './hooks/useShortKeys';

function App() {
  const shortKeys = {
    'Ctrl+N': () => alert('New notification shortcut!'),
    'Ctrl+D': () => alert('Dashboard shortcut!'),
  };

  useShortKeys(shortKeys);

  return (
    <NotificationProvider>
      <Router>
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/dashboard" component={Dashboard} />
        </Switch>
        <Stepper />
        <NotificationSettings />
        <SecuritySettings />
      </Router>
    </NotificationProvider>
  );
}

export default App;
""",
    "stacker/src/frontend/src/index.js": """import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
""",
    "stacker/src/frontend/src/router.js": """import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import Dashboard from './pages/Dashboard';

const AppRouter = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/dashboard" component={Dashboard} />
      </Switch>
    </Router>
  );
};

export default AppRouter;
""",
    "stacker/tests/__init__.py": "# Initialize tests package\n",
    "stacker/tests/backend/test_nlp_parsing.py": """import unittest
from src.backend.nlp_parsing import parse_user_input

class TestNLPParsing(unittest.TestCase):
    def test_parse_user_input(self):
        input_text = "I need a HIPAA-compliant health application with authentication, code analysis, and monitoring."
        expected_output = {
            "performance": [],
            "visual_elements": [],
            "data_sources": ["health"],
            "compliance_standards": ["HIPAA"],
            "stakeholders": [],
            "file_types": [],
            "misc": ["authentication", "code analysis", "monitoring"]
        }
        self.assertEqual(parse_user_input(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()
""",
    "stacker/tests/backend/test_tech_stack_matching.py": """import unittest
from src.backend.tech_stack_matching import match_tech_stack

class TestTechStackMatching(unittest.TestCase):
    def test_match_tech_stack(self):
        parsed_data = {
            "compliance_standards": ["HIPAA"],
            "data_sources": ["health"],
            "misc": ["authentication", "code analysis", "monitoring"]
        }
        team_skills = ["Python", "JavaScript", "Docker"]
        stack_options = match_tech_stack(parsed_data, team_skills)
        self.assertTrue(len(stack_options) > 0)
        self.assertIn(("Python (Django HIPAA)", "compliance_standards", 72.5), stack_options)

if __name__ == "__main__":
    unittest.main()
""",
    "stacker/tests/backend/test_sorting.py": """import unittest
from src.backend.sorting import sort_tech_stacks

class TestSortingUtility(unittest.TestCase):
    def test_sort_tech_stacks(self):
        stack_options = [
            ("Python (Django HIPAA)", "compliance_standards", 72.5),
            ("Java (Spring Boot)", "compliance_standards", 70.0),
            ("Node.js (Express)", "compliance_standards", 67.5)
        ]
        sorted_stacks = sort_tech_stacks(stack_options, criteria="overall")
        self.assertEqual(sorted_stacks[0][0], "Python (Django HIPAA)")

if __name__ == "__main__":
    unittest.main()
""",
    "stacker/tests/backend/test_full_workflow.py": """import unittest
from src.backend.nlp_parsing import parse_user_input
from src.backend.tech_stack_matching import match_tech_stack
from src.backend.sorting import sort_tech_stacks

class TestFullWorkflow(unittest.TestCase):
    def test_full_workflow(self):
        input_text = "I need a HIPAA-compliant health application with authentication, code analysis, and monitoring. My team skills are Python, JavaScript, Docker."
        parsed_data = parse_user_input(input_text)
        team_skills = ["Python", "JavaScript", "Docker"]
        stack_options = match_tech_stack(parsed_data, team_skills)
        sorted_stacks = sort_tech_stacks(stack_options, criteria="overall")
        
        expected_top_stack = "Python (Django HIPAA)"
        self.assertEqual(sorted_stacks[0][0], expected_top_stack)

if __name__ == "__main__":
    unittest.main()
""",
    "stacker/tests/frontend/test_ui.js": """import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../../src/App';

test('renders Stepper component', () => {
  render(<App />);
  const element = screen.getByText(/Stepper Component/i);
  expect(element).toBeInTheDocument();
});

test('renders Notification Settings component', () => {
  render(<App />);
  const element = screen.getByText(/Notification Settings/i);
  expect(element).toBeInTheDocument();
});

test('renders Security Settings component', () => {
  render(<App />);
  const element = screen.getByText(/Security Settings/i);
  expect(element).toBeInTheDocument();
});
""",
    "stacker/configs/logging_config.py": """import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

logger = setup_logging()
logger.info("Logging setup complete.")
""",
    "stacker/requirements.txt": """spacy
flask
pytest
react-router-dom
@testing-library/react
@testing-library/jest-dom
""",
    "stacker/setup.py": """from setuptools import setup, find_packages

setup(
    name='stacker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'spacy',
        'flask',
    ],
)
"""
}

def create_project_structure():
    for file_path, content in project_structure.items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully.")
