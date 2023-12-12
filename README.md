<div align="center">
<pre>
  _   _   _____   _   _           _                     
 | \ | | |_   _| | | | |  _   _  | |__    _ __    _   _ 
 |  \| |   | |   | |_| | | | | | | '_ \  | '_ \  | | | |
 | |\  |   | |   |  _  | | |_| | | |_) | | |_) | | |_| |
 |_| \_|   |_|   |_| |_|  \__,_| |_.__/  | .__/   \__, |
                                         |_|      |___/ 
--------------------------------------------------------------
A simple CLI app to interact with Notion API and view tasks.
</pre>
</div>

Recently i discovered the [P.A.R.A Method](https://www.buildingasecondbrain.com/) a system to created to organize
digital life. I decided to build my second brain in Notion, and sometimes i don't have the Web/App opened.

So i decided to create a CLI app to interact with Notion API and my P.A.R.A Method, and i can easily view my tasks, projects
and more in my terminal.

## Installation
---

This project uses [poetry](https://python-poetry.org) to manage dependencies.

Install the dependencies:

```bash
poetry install
```

Build the wheel package:

```bash
poetry build
```

Install the wheel package:

```bash
pip install --user /your/path/to/nthub/dist/*.whl
```

## Configuration
---

To configure properly the cli, you need to set all variables in `settings.yaml` file.

```yaml
notion_api:
  api_key: SECRET_KEY 
  api_version: 2022-06-28
  databases:
    tasks:
      id: <your-database-id>
      title: <your-database-title>
      fields: <your-database-fields>
    projects:
      id: <your-database-id>
      title: <your-database-title>
      fields: <your-database-fields>
    birthdays:
      id: <your-database-id>
      title: <your-database-title>
      fields: <your-database-fields>
```

After setting the variables, you can move it to your `$HOME/.config/nthub` folder.

```bash
mkdir -p $HOME/.config/nthub
cp settings.yaml $HOME/.config/nthub/settings.yaml
```

## Features
---

#### Tasks
- [x] View daily tasks
- [x] View weekly tasks
- [x] View all tasks
- [x] Add new task
- [ ] Edit task
- [ ] Delete task

#### Projects
- [x] View all projects

#### Others
- [x] View all birthdays

## Usage Examples
---

#### Tasks

List all tasks:
```bash
nthub tasks list
```

List tasks daily:
```bash
nthub tasks list --daily
```

List tasks weekly:
```bash
nthub tasks list --weekly
```

Create new task:
```bash
nthub tasks create --title "My new task"
```

#### Projects

List all projects:
```bash
nthub projects list
```

#### Birthdays

List all birthdays:
```bash
nthub birthday list
```

## Meta 
---

According to my personal usage of this cli tool, i'll continue to add more features and improvements.
Feel free to contact me if you have any questions or suggestions. Any feedback is appreciated.

Feel free to modify this project in any way you want, and use the way you want. See `LICENSE` for more information.

