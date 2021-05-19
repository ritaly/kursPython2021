import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.jon = Student('Jon', 'Snow', 4.5, None)
        self.anna = Student('Anna', 'Smith', 4.7, None)

    def test_email_when_name_changed(self):

        self.assertEqual(self.jon.email, 'jon.snow@university.com')

        self.jon.name = 'John'
        self.assertEqual(self.jon.email, 'john.snow@university.com')

    def test_fullname_value(self):
        self.assertEqual(self.jon.fullname, 'Jon Snow')

    def test_full_when_lastname_changed(self):
        self.assertEqual(self.anna.fullname, 'Anna Smith')

        self.anna.last = 'Villa'
        self.assertEqual(self.anna.fullname, 'Anna Villa')

    def test_grand_scholarship(self):
        self.assertEqual(self.anna.scholarship, None)
        self.anna.grant_scholarship()
        self.assertEqual(self.anna.scholarship, True)

    def test_not_grand_scholarship(self):
        self.assertEqual(self.jon.scholarship, None)
        self.jon.grant_scholarship()
        self.assertEqual(self.jon.scholarship, False)


    def tearDown(self):
        del self.anna
        del self.jon

if __name__ == '__main__':
    unittest.main()