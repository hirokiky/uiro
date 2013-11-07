Using mako templates
====================

Uiro depends on mako_ template, and provide some shortcuts to use templates
for applications.
Templates for an application should store in `yourpackage/templates` directory.
Uiro will collect templates and correlate the app and templates.

You learn how to use shortcuts here, but not about mako_ template
usage. you should see mako_ documentation and learn about it.

Easiest way, by view
--------------------
Most easiest way to get and render a template is specifying
it by `view_config`, like this.

.. code-block:: python

    @view_config(method='get',
                 template_name='blog:entry.mako')
    def get_view(self, request, context):
        entry = context['blog_entry']
        return {'entry': entry}

If views return a dictionary, `view_config` will handle
it as context dictionary for a template specified by `template_name`.
`view_config` will render it and use it as Response body.

You can specify a template by passing a template name
that is string splittable by a colon.
The left value is package name,
and the right value is template name, like 'blog:entry.mako'.

The template used in above example must be here::

    blog/templates/entry.mako

It was collected automatically, so you can use it only specifying
the signature.

Simplest way
------------

You can get template by a getter function
`uiro.template.get_template`.
It simply returns mako_ template object, so you can
render it by `.render` method.

.. code-block:: python

    from uiro.template import get_template
    get_template('blog:entry.mako').render(entry='blog entry')

.. _mako: http://www.makotemplates.org/
