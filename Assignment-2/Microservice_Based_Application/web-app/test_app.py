# test_app.py

import unittest
import app


class RateLimiterTestCase(unittest.TestCase):

    def setUp(self):
        # Setting up the Flask test client
        app.app.testing = True
        self.app = app.app.test_client()

        # Reset Redis database
        app.r.flushdb()

    def test_successful_request(self):
        """Test a successful request."""
        response = self.app.get('/endpoint')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Request processed!", response.data)

    def test_rate_limiting(self):
        """Test that rate limiting works after reaching the limit."""

        # Sending requests up to the limit
        for _ in range(app.LIMIT):
            response = self.app.get('/endpoint')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Request processed!", response.data)

        # The next request should be rate limited
        response = self.app.get('/endpoint')
        self.assertEqual(response.status_code, 429)  # 429 is Too Many Requests
        self.assertIn(b"Too many requests!", response.data)


if __name__ == '__main__':
    unittest.main()
