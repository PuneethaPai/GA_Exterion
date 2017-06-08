import unittest

from bucket import Bucket
from score_card import ScoreCard


class BucketTest(unittest.TestCase):
    def test_bucket_equality_for_change_in_order(self):
        bucket1 = Bucket([ScoreCard(index=1, score=10), ScoreCard(index=2, score=20)])
        bucket2 = Bucket([ScoreCard(index=2, score=20), ScoreCard(index=1, score=10)])
        self.assertEquals(bucket1, bucket2)

    def test_bucket_inequality(self):
        bucket1 = Bucket([ScoreCard(index=1, score=10), ScoreCard(index=2, score=20)])
        bucket2 = Bucket([ScoreCard(index=3, score=30), ScoreCard(index=4, score=40)])
        self.assertNotEqual(bucket1, bucket2)
        self.assertNotEqual(bucket1.__hash__(), bucket2.__hash__())
