"""Create routes for accessing pages."""


def includeme(config):
    """Define routes for serving pages."""
    config.add_static_view('static', 'chelsea_pyramid_learning_journal:static')
    config.add_route('list_view', '/')
    config.add_route('detail_view', '/journal/{id:\d+}')
    config.add_route('create_view', '/journal/new-entry')
    config.add_route('update_view', '/journal/{id:\d+}/edit-entry')
