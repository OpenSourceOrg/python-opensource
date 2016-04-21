# Copyright (c) 2015, Paul R. Tagliamonte <paultag@opensource.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import requests
import os

class License(dict):
    """
    Dict subclass (you can use me like a dict!) for License information. This
    contains a few helper methods to clean up code using the License
    information API.
    """

    def __init__(self, *args, **kwargs):
        super(License, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @property
    def other_names(self):
        if 'other_names' in self and self['other_names'] != None:
            return self['other_names']
        return []

    @property
    def superseded(self):
        """
        Check to see if a license has been superseded by another license. This
        method returns a boolean. The identifier that this license was
        superseded by, if true, is contained in 'superseded_by'
        """
        return self.get('superseded_by') is not None

    def __repr__(self):
        return '<License {id} ({name})>'.format(**self)


class OpenSourceAPI(object):
    """
    Open Source API Wrapper
    """

    def __init__(self, url="https://api.opensource.org"):
        self.url = url

    def _get(self, resource, *args):
        """
        Internal method to fetch an API endpoint with a bit of sugar to make
        the rest of the code a bit more readable.
        """
        response = requests.get(os.path.join(self.url, resource, *args))
        data = response.json()
        if response.status_code != 200:
            raise ValueError(", ".join([x['message'] for x in data['errors']]))
        return data

    def all(self):
        """
        Return a list of all license identifiers that the server knows about.
        """
        return [License(x) for x in self._get("licenses")]

    def tagged(self, tag):
        """
        Return a list of all License objects that are tagged with a given
        tag.
        """
        return [License(x) for x in self._get("licenses", tag)]

    def get(self, name):
        """
        Return a License object for the given identifier.
        """
        return License(self._get("license", name))
