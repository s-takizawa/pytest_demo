# pytest_demo
This is a minimal develop and test enviromento using Python 3.8+ and Pytest ( and VS Code).
<br>
Please use for study, education, or as template.

# Requirements
It needs 'pytest'.
<br>
```pip install pytest ```

# Supplementary explanation
## ./pytest.ini
```python
addopts = -v --capture=no
```
capture=no => show ``` print('hoge') ``` at console when it executes pytest.

## ./tests/__init.py
When it executes pytest, must need it.

## ./.vscode/launch.json
```
"cwd": "${workspaceFolder}",
"env": {"PYTHONPATH": "${cwd}"}
```
It needs when execute direcutory **.py.
If there is not, we write below import statement every test_**.py.
```pyton
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))[1]))
print(sys.path)
from src.calc import Calc
```
insted of
```python
from src.calc import Calc
```
