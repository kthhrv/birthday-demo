# Birthday-demo

Simple HTTP API application with two endpoints

## Localdev

requirements; docker and pyenv locally installed

- Install python packages required for dev
```
pip install requirements-dev.txt
```

- Start up localdev constainers
```
invoke run
```

## Testing

- All usecases should have tests
- Test are run during PR and Merge to `main` builds.

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
