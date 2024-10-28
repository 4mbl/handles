# [handles](https://4mbl.link/gh/handles)

> Command-line tool to check the availability of a username on various platforms.

## Table of Contents

* [Table of Contents](#table-of-contents)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)

### Installation

Use pip to install `handles`.

```bash
python3 -m pip install --upgrade handles
```

## Usage

```python
# check if a username is available on any of the supported platforms
handles --platforms '*' myusername

# check if usernames on a file are available on github
handles --platforms github --file usernames.txt
```

## License

Distributed under the MIT License. See [`LICENSE`](./LICENSE) for more information.
