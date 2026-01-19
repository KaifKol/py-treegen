# treegen

`treegen` is a simple command-line utility written in Python that generates a visual directory tree, similar to the Unix `tree` command. The output can be saved to a file or printed directly to the console.

---

## Features

* Generate a directory tree structure
* Ignore specific files or folders
* Show **only files** or **only directories**
* Output to a file or directly to stdout
* Works on Windows, macOS, and Linux

---

## Requirements

* Python 3.7+

No external dependencies are required.

---

## Usage

```bash
python treegen.py -p <path> [options]
```

If the script is run **without any arguments**, it will display the help message.

---

## Options

| Option               | Description                                                    |
| -------------------- | -------------------------------------------------------------- |
| `-p`, `--path`       | Target directory (`.` , relative, or full path) **(required)** |
| `-o`, `--out`        | Output file name (default: `tree.txt`)                         |
| `-i`, `--ignore`     | Comma-separated list of files/folders to ignore                |
| `-f`, `--files-only` | Show only files                                                |
| `-d`, `--dirs-only`  | Show only directories                                          |
| `-s`, `--stdout`     | Print output to console instead of writing to a file           |

---

## Examples

### 1. Generate a tree for the current directory

```bash
python treegen.py -p .
```

Creates `tree.txt` inside the target directory.

---

### 2. Ignore folders like `.git` and `node_modules`

```bash
python treegen.py -p . -i .git,node_modules
```

---

### 3. Print the tree directly to the console

```bash
python treegen.py -p . -s
```

---

### 4. Show only files

```bash
python treegen.py -p . -f
```

---

### 5. Show only directories

```bash
python treegen.py -p . -d
```

---

## Example Output

Assume the following directory structure:

```
project/
├── main.py
├── utils.py
├── README.md
└── src/
    ├── core.py
    └── helpers.py
```

Running:

```bash
python treegen.py -p project -s
```

Will output:

```
project/
├── README.md
├── main.py
├── utils.py
└── src
    ├── core.py
    └── helpers.py
```

---

## Notes

* The output uses Unicode box-drawing characters (`├──`, `└──`, `│`)
* Permission errors are safely ignored
* When writing to a file, the file is created inside the target directory

---