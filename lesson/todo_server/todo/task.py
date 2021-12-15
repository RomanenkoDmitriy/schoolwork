from copy import deepcopy

from flask import Blueprint, request, abort, render_template

from .models import Task
from ..utils.binary_search import binary_search
from ..utils.bubble_sort import bubble_sort
from ..utils.insertion_sort import *

bp = Blueprint('task', __name__)


@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form['title']
        priority = int(request.form['priority'])
        new_task = Task(title=title, priority=priority)
    else:
        order = request.args.get(
            'order', default='', type=str)
        tasks = deepcopy(Task.objects)
        if order:
            bubble_sort(tasks, order)
        else:
            insertion_sort(tasks)
    return render_template('task_list.html', tasks=Task.objects)


@bp.route('/<int:task_id>')
def task_detail(task_id):
    array = [task_id.id for task_id in Task.objects]
    task = binary_search(array, task_id)

    if task:
        return Task.objects[(task - 1)].to_json()
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
