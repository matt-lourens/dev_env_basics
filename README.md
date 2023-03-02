# Work Environment
<!-- https://github.com/matt-lourens/dev_env_basics -->
## VS Code

A code editor. It's free, open source, and runs everywhere (even your Ipad).

[Install](https://code.visualstudio.com/)

[Source code](https://github.com/microsoft/vscode)

- Really good IntelliSense
- Debugging
- Integrated version control (Git)
- Highly customizable

### Overview

#### Useful Commands

- ctrl+shift+p -> Most useful, opens the command palette
- ctrl+k, ctrl+s -> Keyboard shortcuts, away with the mouse!
- ctrl+b -> Toggle Explorer
- ctrl+` -> Toggle Terminal

## Github Copilot

ChatGPT in your editor

## Use cases

### Coding

#### [Virtual environments](https://realpython.com/python-virtual-environments-a-primer/)

Isolate workspaces on a per-project basis

**Template Project Structure:**

- project_name
  - .venv
  - .vscode
  - .gitignore
  - project_name
    - \_\_init\_\_.py
    - main.py
  - requirements.txt

**Steps**

1. `ctrl+shift+p` -> Python: Create Environment

2. ctrl+shift+\` to open new terminal in .venv
3. `pip install -r requirements.txt`
4. Create repo [online](https://github.com/) and initialize it locally

    ```bash
    echo "# project_name" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin git@github.com:username/project_name.git
    git push -u origin master
    ```

For management of different python environments use [pyenv](https://github.com/pyenv/pyenv)

#### [Python](https://www.python.org/) Development

Extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Remote development:

- [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
- [WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

Capabilities:

CoPilot Example:

Code Generation:Function that gets the ground state of a given Hamiltonian H

- Code generation
      Function that gets the ground state of a given Hamiltonian
      $H=\begin{bmatrix}
        0 & 1 & 1 & 0\\
        1 & 0 & 0 & -1\\
        1 & 0 & 0 & -1\\
        0 & -1 & -1 & 0
        \end{bmatrix}$

    Use Scipy sparse matrix instead and return smallest eigenvalue based on real part
- Code explanation
  Factorial Docstring
  Binomial: The latex for this function is
- Relative Imports
- Debugging

### Writing

Prompts

The derivative of the function $f(x)$ is the limit:
The fundamental theorem of calculus connects derivatives and integrals

% 3 by 3 Matrix with alphabetic entries

% Hamiltonian from cong et al:

The parameters for our model significantly influence the performance and jsutifies the usefulness of the framework

Scroll bar
Git track changes

Extension:

- Latex Workshop

### Note taking

Markdown is powerful

Extensions:

- Code Spell Checker
- Markdown+Math
- markdownlint

<!-- Iframe for this gif https://en.wikipedia.org/wiki/File:Fundamental_theorem_of_calculus_(animation_).gif -->

Visualise vector addition:
<!-- <iframe scrolling="no" title="3D Vector addition, triangle, pyramid" src="https://www.geogebra.org/material/iframe/id/yragvt6s/width/1280/height/537/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/true/ld/true/sdz/true/ctl/false" width="1280px" height="537px" style="border:0px;"> </iframe> -->

Visualise projection:
<!-- <iframe scrolling="no" title="Projection+Orthornormal basis" src="https://www.geogebra.org/material/iframe/id/tjhd7ege/width/1920/height/916/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1920px" height="916px" style="border:0px;"> </iframe> -->

### Pair programming

ctrl+shift+p -> Live Share: Start Collaboration Session
