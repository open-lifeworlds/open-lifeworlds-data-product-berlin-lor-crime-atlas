[![Issues](https://img.shields.io/github/issues/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-crime-atlas)](https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-crime-atlas/issues)

<br />
<p align="center">
  <a href="https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-crime-atlas">
    <img src="logo-with-text.png" alt="Logo" style="height: 80px; ">
  </a>

  <h1 align="center">Berlin LOR crime atlas</h1>

  <p align="center">
    Data product combining Berlin LOR crime atlas data and geodata</a>
  </p>
</p>

## About The Project

See [data product canvas](./docs/data-product-canvas.md) and [ODPS canvas](./docs/odps-canvas.md).

### Built With

* [Python](https://www.python.org/)
* [uv](https://docs.astral.sh/uv/)
* [ruff](https://docs.astral.sh/ruff/)

## Installation

Install uv, see https://github.com/astral-sh/uv?tab=readme-ov-file#installation.

```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Usage

Run this command to generate and activate a virtual environment.

```shell
uv venv
source .venv/bin/activate
```

Run this command to re-install the Open Data Product Python library.

```shell
uv pip install --no-cache-dir git+https://github.com/open-lifeworlds/open-lifeworlds-python-lib.git
```

Run this command to start the main script.

```shell
python3 main.py [OPTION]...

  -h, --help                           show this help
  -c, --clean                          clean intermediate results before start
  -q, --quiet                          do not log outputs

Examples:
  python3 main.py -c
```

## Roadmap

See the [open issues](https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-crime-atlas/issues) for a list of proposed features (and known issues).

## License

Source data distributed under [Creative Commons Namensnennung 3.0 Deutschland Lizenz](https://creativecommons.org/licenses/by/3.0/de/) by [Polizei Berlin](https://www.berlin.de/polizei/).

Data product distributed under the [CC-BY 4.0 License](https://creativecommons.org/licenses/by/4.0/). See [LICENSE.md](./LICENSE.md) for more information.

## Contact

openlifeworlds@gmail.com
