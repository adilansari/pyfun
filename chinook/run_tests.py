import unittest
import os

if __name__ == "__main__":
    os.environ['app_env'] = 'test'
    suite = unittest.TestLoader().discover('.', pattern="*_test.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
    os.environ.pop('app_env')