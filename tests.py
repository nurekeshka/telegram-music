from music import clear_downloads
from music import download
from server import send_audio
import unittest, os


base_directory = os.path.dirname(__file__)
temp_directory = os.path.join(base_directory, 'temp')

class TestMusicMethods(unittest.TestCase):
    def test_download(self):
        download('https://youtu.be/nfs8NYg7yQM')
        self.assertTrue(os.path.exists(os.path.join(temp_directory, 'Charlie Puth - Attention [Official Video].webm')))
    
    def test_clear_downloads(self):
        clear_downloads()
        self.assertFalse(os.listdir(temp_directory))


if __name__ == '__main__':
    unittest.main()
