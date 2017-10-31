"""Create routes for accessing pages."""
from chelsea_pyra... import (
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


def append_to_list(val):
    """."""
    longer_list.append(val)
    curr_idx = len(longer_list) - 1
    while longer_list[curr_idx] > longer_list[find_parent(curr_idx)]:
        saved_parent_val = longer_list[find_parent(curr_idx)]
        saved_parent_idx = find_parent(curr_idx)
        longer_list[saved_parent_idx] = val
        longer_list[curr_idx] = saved_parent_val
        curr_idx = saved_parent_idx
    return longer_list


def find_parent(idx):
    """."""
    if idx % 2 == 0:
        parent_idx = idx / 2 - 1
    elif idx % 2 == 1:
        parent_idx = (idx - 1) / 2
    return int(parent_idx)


