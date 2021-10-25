from flask import Blueprint, request, abort

from .models import Task
from ..utils.binary_search import binary_search

bp = Blueprint('task', __name__)

@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        data = request.get_json(force=True)
        new_task = Task(**data)
        return new_task.to_json()
    return Task.list_to_json()

@bp.route('/<int:task_id>')
def task_detail(task_id):
    array = [task_id.id for task_id in Task.objects]
    if task_id <= array[-1]:
        return Task.objects[(binary_search(array, task_id) - 1)].to_json()
    else:
        abort(404)
    # array = Task.objects
    # if low is None and high is None:
    #     low = 0
    #     high = len(array) - 1
    #
    # if high >= low:
    #     mid = (high + low) // 2
    #     # return {task_id: f'{type(task_id)}'}
    #     # return f'{array[mid].id}'
    #     if array[mid].id == task_id:
    #         return array[mid].to_json()
    #     elif array[mid].id > task_id:
    #         return task_detail(task_id, low, mid - 1,)
    #     else:
    #         return task_detail(task_id, mid + 1, high)
    # else:
    #     abort(404)