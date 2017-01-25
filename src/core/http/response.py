# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

from .providers import ResponseProvider
from src.core import helper
from .exceptions import ResponseError

class Response(ResponseProvider):
    """Response class"""

    def __init__(self, config, tpl):
        """
        Response instance
        :param src.lib.browser.config.Config config: configurations
        :param src.lib.tpl.tpl.Tpl tpl: templater
        """
        ResponseProvider.__init__(self, config, tpl)

        pass

    def handle(self, resp, request_url, items_size, total_size):
        """
        Handle response
        :param urllib3.response.HTTPResponse response: response object
        :param str request_url: url from request
        :param int items_size: current items sizes
        :param int total_size: response object
        :raise ResponseError
        :return: @TODO
        """
        if hasattr(resp, 'status'):

            if 0 < self._config.debug:
                self._tpl.line_log(key='get_item_lvl1',
                                    percent=self._tpl.line(msg=helper.percent(items_size, total_size),
                                              color='cyan'),
                                    current=items_size,
                                    total=total_size,
                                    item=request_url,
                                    size=self._get_content_size(resp))
            else:
                self._tpl.line_log(key='get_item_lvl0',
                                    percent=self._tpl.line(msg=helper.percent(items_size, total_size),
                                              color='cyan'),
                                    item=request_url)
        else:
            raise ResponseError('Unable to get response from {url}'.format(url=request_url))
        pass