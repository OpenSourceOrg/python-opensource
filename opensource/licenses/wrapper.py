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
    def __init__(self, *args, **kwargs):
        super(License, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @property
    def superseded(self):
        return self.get('superseded_by') is not None

    def __repr__(self):
        return '<License {id} ({name})>'.format(**self)


class OpenSourceAPI(object):
    """
    """

    def __init__(self, url="http://api.opensource.org"):
        """
        """
        self.url = url

    def _get(self, resource, *args):
        """
        """
        response = requests.get(os.path.join(self.url, resource, *args))
        data = response.json()
        if response.status_code != 200:
            raise ValueError(", ".join([x['message'] for x in data['errors']]))
        return data

    def all(self):
        """
        """
        return self._get("licenses")

    def tagged(self, tag):
        """
        """
        return [License(x) for x in self._get("licenses", tag)]

    def get(self, name):
        """
        """
        return [License(x) for x in self._get("license", name)]
