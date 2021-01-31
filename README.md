# kaizen-async

In a world where we are always striving to do better, and to *continously improve*, this server provides you with current metrics.

> Now with added async!

This project supersedes the Django implementation.

## Todos

```
    [x] Asynchronous SJD scraper with secret mgmt
    [x] Serve existing Kaizen metrics
    [x] Set up Pytest and write simple test
    [ ] Moar tests with mocks
    [ ] Data layer - models dir/persist to DB
    [ ] Dockerize
    [ ] Deploy to linode with nginx
    [ ] Authentication
    [ ] Deploy w/Github Actions
    [ ] Simple React client on homepage using Jinja template
    [ ] write + serve American Express statement from inbox metric
    [ ] write + serve savings metric
    [ ] Simple Caching
    [ ] Stash results to NoSQL
    [ ] Hourly cron invocation
    [ ] Analytics w/Streamlit
    [ ] Investigate serverless invocation
    [x] Add precommit
```

## Routes

## Live Docs

## Quick start
0. Create `settings.json` file from `settings_template.json` and populate with credentials.

1. In the project root directory, Run the server

        (venv) $ uvicorn app.main:api --reload

2. Hit the Kaizen endpoint

        curl http://127.0.0.1:8000/api/kaizen

# Run tests

```
        pytest tests
```

## License
MIT

### Resources

- https://training.talkpython.fm/courses/details/getting-started-with-fastapi

- https://www.banjocode.com/scrape-authenticated/

- https://testdriven.io/blog/fastapi-jwt-auth/

- Python Testing with pytest
  - https://learning.oreilly.com/library/view/python-testing-with/9781680502848/

- FastAPI Dev/Test from testdrivenio article repo
  - https://github.com/testdrivenio/fastapi-crud-async

- App structure / separation of concerns
    - https://camillovisini.com/article/abstracting-fastapi-services/
