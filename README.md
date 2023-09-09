# Birthday-demo

Simple HTTP API application with two endpoints

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
- `coverage` is required to met agreed limit.
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
- If in agreed release window deploys the container to `prod` otherwise waits for manual approval.


## Prodction monitoring and alerting

- AWS CloudWatch Dashboard at: https://
- Application is configured with Sentry enabled.


## Disaster Recovery

- Database is snapshoted nightly and those snapshots are copied to 2 other AWS regions
- Application can be deployed to a different AWS region with its Database restored from the latest copied snapshot.
