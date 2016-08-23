from base import BaseClient

import logging
logger = logging.getLogger(__name__)


class EventsClient(BaseClient):

    def __init__(self, *args, **kwargs):
        super(EventsClient, self).__init__(*args, **kwargs)
        self.options['api_base'] = 'track.hubspot.com'

    def _get_path(self, subpath):
        return '/v1/%s' % subpath

    def create_event(self, portal_id, event_id, email_address, **options):
        subpath = 'event?_n=%s&_a=%s&email_address=%s' % (event_id, portal_id,
                                                          email_address)
        return self._call(
            subpath=None,
            url=self._get_path(subpath),
            method='GET',
            **options
        )
