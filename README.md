![Saleor Platform](https://user-images.githubusercontent.com/249912/71523206-4e45f800-28c8-11ea-84ba-345a9bfc998a.png)

<div align="center">
  <h1>Saleor Platform by Peter</h1>
</div>

<div align="center">
  <p>Run backend and dashboard</p>
</div>

<div align="center">
  <a href="https://saleor.io/">🏠 Website</a>
  <span> • </span>
  <a href="https://docs.saleor.io/docs/3.x/">📚 Docs</a>
  <span> • </span>
  <a href="https://saleor.io/blog/">📰 Blog</a>
  <span> • </span>
  <a href="https://twitter.com/getsaleor">🐦 Twitter</a>
</div>

<div align="center">
  <a href="https://githubbox.com/saleor/saleor-platform">🔎 Explore Code</a>
</div>

## About

### What is Saleor Platform?

Saleor Platform is the easiest way to start local development with all the major Saleor services:
- [Core GraphQL API](https://github.com/saleor/saleor)
- [Dashboard](https://github.com/saleor/saleor-dashboard)
- Mailpit (Test email interface)
- Jaeger (APM)
- The necessary databases, cache, etc.

*Keep in mind this repository is for local development only and is not meant to be deployed in any production environment! If you're not a developer and just want to try out Saleor you can check our [live demo](https://demo.saleor.io/).*

## Requirements
1. [Docker](https://docs.docker.com/install/)

## How to clone the repository?

To clone the repository, run the following command

```
git clone https://github.com/PhuongT1/saleor-backend-docker.git
```

## How to run it?
1. Run the application:
```shell
docker compose up
```

## Where is the application running?
- Saleor Core (API) - http://localhost:8000
- Saleor Dashboard - http://localhost:9000
<!-- - Mailpit (Test email interface) - http://localhost:8025 -->

