from test_plus.test import TestCase

from ..factories import EventFactory
from ..serializers import EventSerializer
from ...generic.tests.test_views import GenericViewSetMixin


class EventViewSetTestCase(GenericViewSetMixin, TestCase):
    basename = "event"
    serializer_class = EventSerializer
    factory_class = EventFactory
    queries_less_than_limit = 5

    def validate_item(self, item):
        self.assertEqual(item["name"], self.obj.name)
