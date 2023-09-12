# birthday-demo

Simple HTTP API application with basic CICD

# In Scope

- Simple Hello World style Python Flask application with unit and functional tests.
- System diagram of production AWS Infrastructure.
- Cloud build and deploy script.

# Out of Scope

- Productionisation of application
  - Dockerise localdev and split requirements.txt 
  - Front with Nginx and WSGI
  - Use an API framework like Django Rest Framework
  - Use Clustered HA DB
  - Log to CloudWatch Logs
  
- Developer quality of life enhancements
  - repo setup script (distributed separately).
    - verify docker and pyenv installed.
    - clone with ticket number included in the folder and branch names.
    - create pyenv and install required python packages.
    - run `pre-commit install`.
  - pyinvoke/make for commonly used developer actions.
 
- CICD: AWS CodePipeline/CodeBuild
  - Codebuild for PRs that runs `pre-commit run --all-files` and tests with coverage.
  - CodePipeline triggered on merge to `main` branch.
  - Post `staging` deploy smoke tests before in release window auto deploy to prod.
  - Centralsed channel reporting deployments of all applications.
  
- Monitoring: AWS CloudWatch Dashboard
  - Load Balancer request and error rates plus application response times
  - AutoscalingGroup CPU load and instance count
  - Per instance CPU, memory and disk usage
  
- Alerting: AWS CloudWatch Alarms
  - Email and or Messaging of owning team for
    - Disk, CPU, memory, error rate or response time out of bounds
    - CICD stage failures
    
- Exception Handling: Sentry
  - Configuration of App to send exceptions to Sentry
  - Configuration of Sentry to notify teams
 
- Secret/Env-variable Management: Envars
  - `pre-commit` checks for unencrypted secrets
  - I've developed a solution that leans towards developer ease of use over centralisation
    - https://github.com/timeoutdigital/envars
  - Other solutions are available and approiate ;-)
 
- Disaster Recovery
  - Copy nightly RDS snapshots to another AWS region

## Architectural design choices

There are many ways to skin a cat but generally:

- Avoid vendor lock-in.
  - For instance we could use AWS API Gateway but Django Rest Framework is an excellent open source option.
- Maintainablity over raw performance.
  - NodeJs can be more performant than Python but in a Python shop it will induce more developer overhead.
 
## Code implimentation choices

- My first choice would be Django Rest Framework but this is hardly a 'simple' solution.
- Considered using python http.server as the simplist possible python implemtation but it doesn't suport PUT http method.
- Python Flask looks like the next simplest option.


## Localdev

- Install required python packages
```
pip install requirements.txt
```

- Run app
```
cd birthday_demo
flask run --debug
```

## Testing

- All usecases should have tests.
- `coverage` is required to meet agreed limit.
- Test are automatically run during PR and Merge to `main` builds.

- To run tests locally
```
pytest
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
