<H1>lgbsttracker_api</H1>
<p align="center">
<img src="https://img.shields.io/github/last-commit/py4mac/lgbsttracker_api.svg">
<a href="https://github.com/py4mac/" target="_blank">
    <img src="https://github.com/py4mac/lgbsttracker_api/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/py4mac/lgbsttracker_api" target="_blank">
    <img src="https://codecov.io/gh/py4mac/lgbsttracker_api/branch/master/graph/badge.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/lgbsttracker_api" target="_blank">
    <img src="https://badge.fury.io/py/lgbsttracker_api.svg" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://py4mac.github.io/lgbsttracker_api" target="_blank">https://py4mac.github.io/lgbsttracker_api</a>

**Source Code**: <a href="https://github.com/py4mac/lgbsttracker_api" target="_blank">https://github.com/py4mac/lgbsttracker_api</a>

---

## Requirements

Python 3.6+


## Installation

```bash
pip install lgbsttracker_api
```

## Example

### Use it


(Work in progress)

## Environment variables

| Variable Name |  Description | Default value |
| --- | --- | --- |
| EXPERIMENT_STORAGE_URI | DB Experiment Storage URI | Mandatory: to be set by the user before using library |
| SQL_DB_THREAD_POOL_EXECUTOR_SIZE | Thread pool size | 100 |
| MIN_CONNECTION_POOL_SIZE | Minimum pool size connection | 10 |
| MAX_CONNECTION_POOL_SIZE | Maxiumum pool size connection | 20 |
| CONNECTION_POOL_RECYCLE_TIME | Pool connection recycle time | 30 |

## References

* https://github.com/mlflow/mlflow/
* https://github.com/undera/pylgbst
* https://github.com/tiangolo/fastapi
* https://github.com/aalhour/cookiecutter-aiohttp-sqlalchemy/

## License

This project is licensed under the terms of the MIT license.