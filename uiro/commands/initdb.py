from uiro.commands import LoadAppCommand
from uiro.db import Session, Base


class InitDBCommand(LoadAppCommand):
    """ Creating database tables.
    """
    def take_action(self, parsed_args):
        self.loadapp(parsed_args)
        Base.metadata.create_all(Session.bind)
