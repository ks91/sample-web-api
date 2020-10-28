sample-web-api
==========
This app provides a very simple Web API sample that provides stacks.

It requires Python3 and Flask.

## How to use
To use, first create a stack (this API can handle multiple stacks).
```shell
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"foo"}' http://localhost:5000/create
{"name":"foo"} # returned
```
To push,
```shell
$ curl -X POST -H "Content-Type: application/json" -d '{"value":"5"}' http://localhost:5000/push/foo
{"pushed":"5"} # returned
```
To pop,
```shell
$ curl -X POST http://localhost:5000/pop/foo
{"popped":"5"} # returned
```

## All features
* **/calc/{name}** (POST) to perform stack calculator computation. Supports 'ADD', 'SUB', 'MUL', 'DIV' between two integers.
* **/create** (POST) to create a stack named {name} where data is {"name": name}
* **/list** (GET) to list all stacks.
* **/peek/{name}** (GET) to peek in the whole stack.
* **/pop/{name}** (POST) to pop a value from the stack.
* **/push/{name}** (POST) to push {value} onto the stack where data is {"value": value}
