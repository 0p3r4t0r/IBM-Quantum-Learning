# Getting Started with Qiskit

https://docs.quantum.ibm.com/guides/install-qiskit

A minimal-working-example for running Qiskit jobs using IBM Quantum Channels
on the [IBM Quantum Platform](https://www.ibm.com/quantum/pricing).

[Poetry](https://python-poetry.org/) is used for dependency management.
It provides much more rigorous constraints for versions and is also much
easier to read than the bare-bones `pip freeze > requirements.txt`.

[python-dotenv](https://pypi.org/project/python-dotenv/) is used to read in
the api token, which is stored in `.env`.


## Pitfalls

- Poetry broken virtual environment

    `rm -rf .venv && poetry env remove --all`

    src: https://github.com/python-poetry/poetry/issues/6841#issuecomment-1284578506