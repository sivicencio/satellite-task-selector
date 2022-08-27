# Satellite Task Selector

## About

Satellite Task Selector is an API built for a challenge. It mainly consists of a process for selecting satellite tasks, where tasks use resources that can't be shared between them. Each task has a profit associated, so the selection needs to consider both the profit and the resources compatibility to select the best subset. The API includes a web interface based on SwaggerUI.

The API is built with FastAPI using a specific set of tools, which are detailed in the following sections.

### Demo

A **live demo of the application** [can be found here](https://satellite-task-selector.herokuapp.com/docs).

### Stack and libraries

- Python 3.8+
- FastAPI 0.79
- uvicorn 0.18.2
- `pylint` for linting
- `pytest` and `requests` for testing
- Redis for buffering

### Features

The following features are available through the API:

- Perform task selection from a list of tasks
- Get a list of selected tasks
- Get a list of standby tasks

Once a task selection is performed, two subsets are returned: one with the selected tasks and another one with tasks that were not selected. The ones not selected are added to a buffer that contains at most 100 tasks. These buffered tasks are taken into consideration if a new selection is performed (they are evaluated with the new incoming tasks).

The listing features were added as a way to visualize the behavior of the platform after performing a selection.

Besides the API features, a specific development workflow was also followed. This workflow included code quality and testing tools, Continuous Integration (CI) and Pull Requests (PRs) in Github, which are explained in further detail in the [Workflow](#workflow) section.

## Setup

First clone the repository and cd into it.

```bash
cd satellite-task-selector
```

### Running the API

There is an easy way to run the application with Docker. Build the containers (API and redis):
```bash
docker-compose up -d
```

And visit http://localhost:8000/docs. You should be able to see the available endpoints and make requests as you like.

### Development

If you want to make changes in the code, you will need to follow a few steps. An active Python virtual environment is recommended. First install the application dependencies.

```bash
pip install -r requirements.txt
```

Make sure you have an instance of Redis running, since it's needed for the API.

Finally run the application.

```bash
uvicorn app.main:app --reload
```

## Testing

The application includes a testing suite built with `pytest`. To run the tests execute the following:

```bash
pytest # Add -v option if you want verbose output
```

## Development process

### System design

First a high-level design of the system was made. It includes the different components that later became actual packages. You can see it in the following diagram:

<img src="https://user-images.githubusercontent.com/421739/185367857-22def54e-3d37-4164-9be3-ec4e1830ecac.jpg">

### Project

After having the system design, project tasks were created and added to [a corresponding project](https://github.com/users/sivicencio/projects/1), following the Kanban methodology. Each task has details of implementation and is linked to their corresponding Pull Request (with the actual implementation).

### Workflow

For development, the [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow) workflow was followed, mainly because it allows us to add new features in a very organized and clean way. For each feature, a feature branch was created and a corresponding Pull Request (PR) was opened. The code review process did not happen in this case (for obvious reasons), but everything else did. Finally, each PR was merged to the `main` branch and that way integrated into the codebase.

Regarding the commits format, the [Angular commit message format](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit) was followed, since it provides a very direct and well-communicated way of adding changes to the codebase. A few mistakes were made when doing the merge of the Pull Requests, which made me ommit a few valuable data (automatic links and commit format), but you could check the commit history to see how it was actually implemented.

When merging PRs, the "Squash and merge" strategy was used, which condenses the feature commits into a single commit. However, when looking the details of a PR, you can check the original commits.
### CI

The project currently include 1 Github Action for linting. This action is run when opening a PR (and also when adding new commits to that PR), and is configured as required status checks for merging. This means that a PR cannot be merged if the status checks do not pass. This allows us to have a safer codebase, because we can be sure that at least the code quality requirements is met.

The project also includes a testing suite, so it could be possible to add a Github Action for requiring the tests to pass before merging a PR. This will be addressed as future work.

### Considerations and decisions

The following considerations and decisions were made when doing this challenge:
- The selected and standby tasks can be visualized through the API. It was not an initial requirement but it eases the interaction with the platform
- The selected tasks are stored. This was neither an initial requirement, but it could be useful for 3rd parties
- When selecting tasks, if one of the elements of the input is not valid, an error is returned. In other words, the whole input must be valid in order to be processed
- Both the selected and standby tasks are stored in a buffer-style. There is a max number of items of 100 for both cases, containing the most recent tasks. This is to ensure that we would not be dealing with huge lists

## Future work
- Add testing inside the CI workflow (as a Github Action)
- Improve selection algorithm performance
- Include code observability through logs and alerts
- Include the possibility to select tasks of different satellites (right now we're assuming only one)
