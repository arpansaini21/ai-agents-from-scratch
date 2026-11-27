import unittest

from src.ticket_classifier import ClassifyTicket


class TestClassifyTicket(unittest.TestCase):
    def test_assign_team(self):
        cases = [
            ("Customer cannot login", "Identity Team"),
            ("Security alert triggered", "Security Team"),
            ("Payment transaction failed", "Payments Team"),
            ("Network connection unavailable", "Infrastructure Team"),
            ("Database connection timeout", "Database Team"),
            ("Email delivery failed", "Messaging Team"),
            ("Customer cannot LOGIN", "Identity Team"),
            (
                "Customer cannot login after a database failure.",
                "Define and document a routing priority",
            ),
            ("Unable to update profile", "General Support"),
        ]

        for description, expected in cases:
            with self.subTest(description=description):
                self.assertEqual(ClassifyTicket(description).assign_team(), expected)

    def test_rejects_blank_descriptions(self):
        for description in ("", "   "):
            with self.subTest(description=description):
                with self.assertRaisesRegex(ValueError, "^Description cannot be empty$"):
                    ClassifyTicket(description)

    def test_rejects_non_string_description(self):
        with self.assertRaisesRegex(TypeError, "^Description must be a string$"):
            ClassifyTicket(None)
