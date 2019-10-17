import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A new thrilling Python Series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

    def test__init__(self):
        '''
        Test case that confirms that the object is instantiated correctly
        '''
        self.assertEqual(self.new_movie.id, 1234)
        self.assertEqual(self.new_movie.title, 'Python Must Be Crazy')
        self.assertEqual(self.new_movie.overview, 'A new thrilling Python Series')
        self.assertEqual(self.new_movie.poster, 'https://image.tmdb.org/t/p/w500/khsjha27hbs')
        self.assertEqual(self.new_movie.vote_average, 8.5)
        self.assertEqual(self.new_movie.vote_count, 129993)