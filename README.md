# tailscale-ci-test

This repository is a proof-of-concept that connects a simple web server and a client running in a GitLab CI pipeline using [Tailscale](https://tailscale.com/).

## Run the example

Set up the web server on your machine:

1. create a Tailscale auth key (enable ephemeral, multiple uses and optionally set tags)
2. install docker
3. in `server/sample.env`, update the `TS_AUTHKEY` variable and save the file as `server/.env`
4. run: `cd server; docker compose up --build`

Run the client in GitLab:

1. create an empty repository in GitLab
2. create a new ci variable `TS_AUTHKEY` and fill it with the same key (Settings > CI/CD > Variables)
3. push the code (it should instantly work)

The `.gitlab-ci.yml` is inspired by this code [GitLab](https://gitlab.com/tailscale-dev/gitlab-ci-cd).
