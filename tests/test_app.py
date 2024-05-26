import unittest
from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Run YouTube Transcript', response.data)

    def test_transcribe(self):
        response = self.client.post('/api/transcribe', json={'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
