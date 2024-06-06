import unittest
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
