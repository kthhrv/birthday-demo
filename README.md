# birthday-demo

Simple HTTP API application with two endpoints

## Architectural design choices

There are many ways to skin a cat but 

- Avoid vendor lock-in.
- Maintainablity over raw performance.

For instance we could use AWS API Gateway but Django Rest Framework is an excellent open source option.
NodeJs is more performant that Python but in a Python shop it will induce more developer overhead.

## Localdev

requirements; docker and pyenv locally installed

- Install python packages required for dev
```
pip install requirements-dev.txt
```

- Start up localdev containers
```
invoke run
```

## Testing

- All usecases should have tests please
- `coverage` is required to meet agreed limit.
- Test are automatically run during PR and Merge to `main` builds.

- To run tests locally
```
invoke tests
```

## Deployment

Merge to `main` triggers an AWS CodePipeline that:
- Runs linting and unittests.
- Builds a docker container and publishes it to ECR.
- Deploys the container to a pre-production `staging` environment.
- Runs `smoketests` against `staging`.
- If linting, unittests and smoketests pass and we're inside the agreed release window the container is deployed to `prod` otherwise waits for manual approval.
- If CodePipeline stages fail the team specified in `devops/owner.json` is notified by slack and/or email.


## Prodction monitoring and alerting

- AWS CloudWatch Dashboard at: https://
- Application is configured with Sentry enabled.


## Disaster Recovery

- Database is snapshoted nightly and those snapshots are copied to 2 other AWS regions
- Application can be deployed to a different AWS region with its Database restored from the latest copied snapshot.
