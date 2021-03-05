# pytest_demo
This is a minimal develop and test enviromento using Python 3.8+ and Pytest ( and VS Code).
<br>
Please use for study, education, or as template.
<br><br>
Python + Pytestのシンプルな動作環境です。<br>
Pytestの勉強用や動作確認用に。<br>
日本語での説明は私のブログに記載しています。<br>
https://waterfalls.hatenablog.com/entry/2021/03/05/171342

# Requirements
It needs 'pytest' library.
<br>
```pip install pytest ```

# usage
for windows, open command prompt.<br><br>
cd pytest_demo root.<br>
press 'pytest'.
```
cd c:\workspace\python\pytest_demo
pytest
```

# Supplementary explanation
## ./pytest.ini
```python
addopts = -v --capture=no
```
-v => show detail test results.
--capture=no => show standard output( ``` print('hoge') ``` ) in console with test results.

## ./tests/__init.py
When it executes pytest, must need it.

## ./.vscode/launch.json
```
"cwd": "${workspaceFolder}",
"env": {"PYTHONPATH": "${cwd}"}
```
It needs when execute direcutory **.py.
If there is not, we write below import statement every test_**.py.
```python
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))[1]))
from src.calc import Calc
```
insted of
```python
from src.calc import Calc
```
