import unittest
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
