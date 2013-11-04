
def test_templates():
    from uiro import template as uiro_template
    from .pkgs import template_app

    uiro_template.setup_lookup((template_app,))
    template = uiro_template.get_app_template('template_app:test.mako')
    assert template.render(content='work') == b'No more work'
