__name__ = 'web_app'

from matcha import Matching
from uiro.controller import BaseController
from uiro.view import view_config


class Controller(BaseController):
    @view_config(method='get')
    def get_view(self, request, context):
        return 'No more {}'.format(request.matched_dict['thing'])


matching = Matching('/{thing}', Controller())
