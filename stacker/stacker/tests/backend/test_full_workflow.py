import unittest
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
