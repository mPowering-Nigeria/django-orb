# -*- coding: utf-8 -*-

"""
Tests for orb.review managers and querysets
"""

from datetime import date, timedelta

from freezegun import freeze_time

from orb.models import Resource
from orb.resources.tests.factory import resource_factory
from orb.review.models import ContentReview
from orb.review.tests.base import ReviewTestCase


class ReviewQuerysetTests(ReviewTestCase):
    """

    There are three resources, two roles, and two users.

    medical::reviewer
    technical::staff_user


    - the first resource has two reviews, one accepted and one rejected
    - the second resource has two reviews, one accepted and one pending
    - the third reosurce has one pending review that is overdue

    """

    @classmethod
    def setUpClass(cls):
        super(ReviewQuerysetTests, cls).setUpClass()
        cls.resource_two = resource_factory(
            user=cls.nonreviewer,
            title=u"Second review",
            description=u"Básica salud del recién nacido",
        )
        cls.resource_three = resource_factory(
            user=cls.nonreviewer,
            title=u"Third réview",
            description=u"Básica salud del recién nacido",
        )

        ContentReview.objects.create(
            role=cls.medical_role,
            reviewer=cls.staff_user,
            resource=cls.resource,
            status=Resource.APPROVED,
        )
        ContentReview.objects.create(
            role=cls.technical_role,
            reviewer=cls.reviewer,
            resource=cls.resource,
            status=Resource.REJECTED,
        )

        ContentReview.objects.create(
            role=cls.medical_role,
            reviewer=cls.staff_user,
            resource=cls.resource_two,
            status=Resource.APPROVED,
        )
        ContentReview.objects.create(
            role=cls.technical_role,
            reviewer=cls.reviewer,
            resource=cls.resource_two,
            status=Resource.PENDING,
        )

        with freeze_time(date.today() - timedelta(days=15)):
            cls.overdue = ContentReview.objects.create(
                role=cls.technical_role,
                reviewer=cls.reviewer,
                resource=cls.resource_three,
                status=Resource.PENDING,
            )

    def test_pending_qs(self):
        """Returns only reviews that are pending"""
        self.assertEqual(
            ContentReview.reviews.pending().count(),
            2,
        )

    def test_complete_qs(self):
        """Returns only reviews that are approved or rejected"""
        self.assertEqual(
            ContentReview.reviews.complete().count(),
            3,
        )

    def test_overdue_qs(self):
        """Returns only reviews not updated in set time"""
        self.assertEqual(
            ContentReview.reviews.overdue().count(),
            1,
        )

    def test_for_user_qs(self):
        """Returns any reviews for user"""
