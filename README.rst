django-startproject-templates
=============================

Easy to use templates for use with |djangos-startproject|_.

.. |djangos-startproject| replace:: Django's ``startproject --template``
.. _djangos-startproject: https://docs.djangoproject.com/en/stable/ref/django-admin/#startproject

Use with e.g.

.. code-block:: console

    $ django-admin startproject example . --template ~/Documents/Projects/django-startproject-templates/simple

The ``.`` puts the ``manage.py`` in the current directory.

Templates
---------

``simple``
~~~~~~~~~~

A single project that is its own app.

``simple-core``
~~~~~~~~~~~~~~~

A single project with a nested empty core app.

``single-file``
~~~~~~~~~~~~~~~

My single file project taken from `my single file blog post <https://adamj.eu/tech/2019/04/03/django-versus-flask-with-single-file-applications/>`__.
