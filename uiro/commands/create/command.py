import re

from gearbox.command import TemplateCommand


class CreateCommand(TemplateCommand):
    CLEAN_PACKAGE_NAME_RE = re.compile('[^a-zA-Z0-9_]')

    def get_description(self):
        return 'Creates a basic one-app Uiro project'

    def get_parser(self, prog_name):
        parser = super(CreateCommand, self).get_parser(prog_name)

        parser.add_argument('-n', '--name', dest='package',
                            metavar='NAME', required=True,
                            help="Package Name")

        parser.add_argument('-o', '--output-dir', dest='output_dir',
                            metavar='OUTPUT_DIR',
                            help="Destination directory (by default the package name)")

        return parser

    def take_action(self, opts):
        if opts.output_dir is None:
            opts.output_dir = opts.package

        self.run_template(opts.output_dir, opts)
