# birthday-demo

Simple HTTP API application with Cloud deploy playbook

# In Scope

- Simple Hello World style Python Flask application with unit and functional tests.
- [System diagram of production AWS Infrastructure.](https://docs.google.com/drawings/d/17UIdFCO2ffNFYe2A_618zLZojwjKfZyZf7514GZK_jM/edit?usp=sharing)
- Cloud build and deploy script.

# Out of Scope

- Productionisation of application
  - Dockerise localdev and split requirements.txt to reduce docker image size.
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
  - Enable branch projection rules on `main` branch.
  - Codebuild for PRs that runs `pre-commit run --all-files` and tests with coverage.
  - CodePipeline triggered on merge to `main` branch.
  - Post `staging` deploy smoke tests followed auto deploy to prod if in release window.
  - Centralised channel reporting deployments of all applications.

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
  - Other solutions are available and appropriate.

- Disaster Recovery
  - Copy nightly RDS snapshots to another AWS region

## Architectural design choices

There are many ways to skin a cat but generally:

- Avoid vendor lock-in.
  - For instance we could use AWS API Gateway but Django Rest Framework is an excellent open source option.
- Maintainability over raw performance.
  - NodeJs can be more performant than Python but in a Python shop it will induce more developer overhead.

## Code implementation choices

- My first choice would be Django Rest Framework but this is hardly a 'simple' solution.
- Considered using python http.server as the simplest possible python implementation but it doesn't support PUT http method.
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

- Run tests.
```
pytest
```

## Deployment

- Run deploy playbook
```
cd devops/ansible
./birthday_demo_deploy.yml -e env=<staging|prod>
```
