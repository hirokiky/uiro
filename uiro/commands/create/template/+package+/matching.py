from matcha import Matching as m

from .views import TopController

matching = m('/', TopController(), name='top')
