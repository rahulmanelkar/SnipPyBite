# SnipPyBite
Snippybyte is a code snippet tool written in Python.

You can use it to manage your code snippets.

It currently uses a CLI for user interaction with a fast API backend

## Installation:

Requirements:
- Python 3.11+
- uv


## Usage

### Get Code

```bash
git clone https://github.com/kishanpatel789/snipster.git
cd snipster
```
### Using the CLI

 uv run snippybite --help                                                                                        2 ↵

 Usage: snippybite [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.       │
│ --help                        Show this message and exit.                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ add                                                                                                                  │
│ list                                                                                                                 │
│ get                                                                                                                  │
│ delete                                                                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


### API with FastAPI

```bash
uv run fastapi dev src/snipster/api.py
```

The API can be reached at `http://127.0.0.1:8000`. Access the Swagger docs at `http://127.0.0.1:8000/docs`


## License

MIT
