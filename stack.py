# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 Kenji Saito

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask, request, abort, jsonify

stack = Flask(__name__)

stacks = {}


def abort_by_missing_param(param):
    abort(400, {
        'code': 'Bad Request',
        'message': '{0} is missing'.format(param)
    })


def abort_by_not_found(param, value):
    abort(404, {
        'code': 'Not Found',
        'message': '{0} {1} is not found'.format(param, value)
    })


@stack.route('/')
def index():
    return jsonify({})


@stack.route('/calc/<string:name>', methods=['POST'])
def calc(name):
    if name not in stacks:
        abort_by_not_found('name', name)

    if len(stacks[name]) <= 0:
        abort_by_missing_param('operator')

    op = stacks[name].pop()

    if op == 'ADD':
        if len(stacks[name]) < 2:
            abort_by_missing_param('operand')

        arg2 = int(stacks[name].pop())
        arg1 = int(stacks[name].pop())

        value = str(arg1 + arg2)

    elif op == 'SUB':
        if len(stacks[name]) < 2:
            abort_by_missing_param('operand')

        arg2 = int(stacks[name].pop())
        arg1 = int(stacks[name].pop())

        value = str(arg1 - arg2)
        
    elif op == 'MUL':
        if len(stacks[name]) < 2:
            abort_by_missing_param('operand')

        arg2 = int(stacks[name].pop())
        arg1 = int(stacks[name].pop())

        value = str(arg1 * arg2)

    elif op == 'DIV':
        if len(stacks[name]) < 2:
            abort_by_missing_param('operand')

        arg2 = int(stacks[name].pop())
        arg1 = int(stacks[name].pop())

        value = str(arg1 // arg2)

    else:
        stacks[name].append(op)
        abort_by_missing_param('operator')

    stacks[name].append(value)

    return jsonify({
        'result': value
    })


@stack.route('/clear/<string:name>', methods=['POST'])
def clear(name):
    if name not in stacks:
        abort_by_not_found('name', name)

    stacks[name] = []

    return jsonify({
        'stack': stacks[name]
    })


@stack.route('/create', methods=['POST'])
def create_stack():
    name = request.json.get('name')

    if name is None:
        abort_by_missing_param('name')

    stacks[name] = []

    return jsonify({
        'name': name
    })


@stack.route('/list', methods=['GET'])
def list_stacks():
    return jsonify({
        'stacks': list(stacks.keys())
    })


@stack.route('/peek/<string:name>', methods=['GET'])
def peek(name):
    if name not in stacks:
        abort_by_not_found('name', name)

    return jsonify({
        'stack': stacks[name]
    })


@stack.route('/pop/<string:name>', methods=['POST'])
def pop(name):
    if name not in stacks:
        abort_by_not_found('name', name)

    if len(stacks[name]) <= 0:
        abort(400, {
            'code': 'Bad Request',
            'message': 'stack is empty'
        })

    value = stacks[name].pop()

    return jsonify({
        'popped': value
    })


@stack.route('/push/<string:name>', methods=['POST'])
def push(name):
    if name not in stacks:
        abort_by_not_found('name', name)

    value = request.json.get('value')

    if value is None:
        abort_by_missing_param('value')

    stacks[name].append(value)

    return jsonify({
        'pushed': value
    })


@stack.route('/run/<string:name>', methods=['POST'])
def run(name):
    if name not in stacks:
        abort_by_not_found('name', name)

    if len(stacks[name]) <= 0:
        abort(400, {
            'code': 'Bad Request',
            'message': 'stack is empty'
        })

    if type(stacks[name][-1]) is not list:
        abort_by_missing_param('program')

    program = stacks[name].pop()

    for code in program:
        stacks[name].append(code)

        if stacks[name][-1].isalpha():
            calc(name)

    return jsonify({
        'result': stacks[name][-1]
    })


if __name__ == '__main__':
    stack.run()


# end of stack.py
