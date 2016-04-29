# {{{ Copyright (c) Paul R. Tagliamonte <paultag@opensource.org>, 2015-2016
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. }}}

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

# vim: foldmethod=marker
