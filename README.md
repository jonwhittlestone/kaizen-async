# kaizen-async

In a world where we are always striving to do better, and to *continously improve*, this server provides you with current metrics.

> Now with added async!

This project supersedes the Django implementation.

## Todos

```
    [x] Asynchronous SJD scraper with secret mgmt
    [x] Serve existing Kaizen metrics
    [ ] Set up Pytest and write tests with mocks
    [ ] Refactor - models dir
    [ ] Deploy to linode with nginx
    [ ] Dockerize
    [ ] Authentication
    [ ] Deploy w/Github Actions
    [ ] Simple React client on homepage using Jinja template
    [ ] Gmail Inbox count/scraper
    [ ] Test for Async Gmail Inbox counter
    [ ] serve American Express statement from inbox metric
    [ ] Simple Caching
    [x] Add precommit
```

## Routes

## Live Docs

## Quick start
0. Create `settings.json` file from `settings_template.json` and populate with credentials.

1. Run the server

        (venv) $ python main.py

2. Hit the Kaizen endpoint

        curl http://127.0.0.1:8000/api/kaizen

## License
MIT

### Resources

- https://training.talkpython.fm/courses/details/getting-started-with-fastapi
- https://www.banjocode.com/scrape-authenticated/
- https://testdriven.io/blog/fastapi-jwt-auth/
