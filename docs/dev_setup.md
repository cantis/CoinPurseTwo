# Instructions for Developer setup

1. Clone repository from git hub
   - `PS git clone https://github.com/cantis/CoinPurseTwo.git `
2. Poetry Settings
- *I recomend you set the following poetry settings* (needs to only be done once per machine)
    - `PS poetry config virtualenvs.in-project true` *This will create the virtual environment in the project directory*
    - `PS poetry config virtualenvs.path .venv` *This will set the virtual environment directory to .venv*
3. run `poetry install` to install dependencies and create virtual environment
4. run `poetry shell` to activate virtual environment
