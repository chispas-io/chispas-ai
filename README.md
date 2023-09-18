# ✨ Chispas

[![CI](https://github.com/chispas-io/chispas-ai/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chispas-io/chispas-ai/actions/workflows/ci.yml)

Language learning with an AI tutor.

## Setup

Setup env

```bash
scripts/setup
```

Generate an OpenAI token https://platform.openai.com/account/api-keys and supply it as an environment variable, `OPENAI_API_KEY`. Or copy/edit the example `.env` file.

```bash
cp .env.example .env
vim .env
```

Initialize the db and run the app

```bash
pipenv run cli init-db
pipenv run cli serve
```

Then visit http://localhost:5000/.

## Test

```bash
pipenv run tests
```
