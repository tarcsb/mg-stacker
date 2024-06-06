import unittest
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
