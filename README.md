# Todo App CLI
This is a command-line todo list application.

## Installation
- Clone the repository.
- Move inside the folder and run `pip install -e .`
- From now on you run the application using the command `todo`

## Usage
- Use `todo --help` to print the help
```
Usage: todo [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add      Create and add a task to your list
  display  Output all registered tasks by default.
  purge    Suppress all done tasks
```

- use `todo <cmd> --help` to print the help for a specific command
```
Usage: todo add [OPTIONS]

  Create and add a task to your list

Options:
  --title TEXT     Title of your task  [required]
  --priority TEXT  Set the priority of your task, Normal by default
  --help           Show this message and exit.
```

## Developers
Run `pytest -v` test to execute the test suite.
