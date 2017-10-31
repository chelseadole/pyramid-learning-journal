"""Create routes for accessing pages."""

from chelsea_pyramid_learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
    update_view
)


def includeme(config):
    """Define routes for serving pages."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/new-entry')
    config.add_route('update_view', '/journal/{id:\d+}/edit-entry')