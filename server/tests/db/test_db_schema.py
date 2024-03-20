import unittest
from tests.test_utils import *


class TestDBSchema(unittest.TestCase):
    def test_rebuild_tables(self):
        """Rebuild the tables"""
        post_rest_call(self, "http://localhost:8080/manage/init")
        event = get_rest_call(self, "http://localhost:8080/events")
        self.assertEqual(len(event), 0)

    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        post_rest_call(self, "http://localhost:8080/manage/init")
        post_rest_call(self, "http://localhost:8080/manage/init")
        event = get_rest_call(self, "http://localhost:8080/events")
        self.assertEqual(len(event), 0)