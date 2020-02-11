from base import BaseClient
import json
import logging
logger = logging.getLogger(__name__)


class ContactsClient(BaseClient):
    """Class to work with Contact API in hubspot."""

    def __init__(self, *args, **kwargs):
        """Initialize api base."""
        super(ContactsClient, self).__init__(*args, **kwargs)
        self.options['api_base'] = 'api.hubapi.com'

    def create_update_contacts(self, email_address, api_key, data, **options):
        """Create or Update contacts in hubspot."""
        subpath = '/contacts/v1/contact/createOrUpdate/email/%s/?hapikey=%s' % (
            email_address, api_key)
        return self._call(
            subpath=None,
            url=subpath,
            method='POST',
            data=data,
            **options
        )

    def get_contact_by_email(self, email_address, api_key):
        """Get contact by email_address ."""
        subpath = '/contacts/v1/contact/email/%s/profile?hapikey=%s' % (
            email_address, api_key)

        data = self._call(
            subpath=None,
            url=subpath,
            method='GET',
        )
        if data.body:
            json_data = json.loads(data.body)
            return json_data

    def update_contacts(self, email_address, api_key, data, **options):
        """Update contacts in hubspot."""
        # get vid from hubspot to update contact.
        contact = self.get_contact_by_email(email_address, api_key)
        if contact:
            subpath = '/contacts/v1/contact/vid/%s/profile?hapikey=%s' % (
                contact['vid'], api_key)
            return self._call(
                subpath=None,
                url=subpath,
                method='POST',
                data=data,
                **options
            )

    def delete_contact(self, email_address, api_key):
        """ Delete a contact from hubspot.

            :param string email_address: the email of the user that will be
            deleted.
            :param string api_key: the api key used on Hubspot.
            :raises HapiNotFound: if contact is not found on Hubspot.
        """
        contact = self.get_contact_by_email(email_address, api_key)
        if contact:
            subpath = '/contacts/v1/contact/vid/%s?hapikey=%s' % (
                contact['vid'], api_key
            )
            return self._call(
                subpath=None,
                url=subpath,
                method='DELETE'
            )
