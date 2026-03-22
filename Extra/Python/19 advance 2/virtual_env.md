```cmd
pip install virtualenv
```

> this command to install virtual environment inside your system so next we can create virtual environment.

```cmd
virtualenv myProject # we can give any name
```

> using this command we can create virtual environment.

```cmd
.\myProject\Scripts\activate.ps1
```

> to active your virtual environment

# BUT IF WE HAVE Python 3.3+ don't need virtualenv package

```cmd
python -m venv myProject
```

> to create virtual environment

```cmd
.\myProject\Scripts\activate.ps1 # this for PowerShell
```

```cmd
.\myProject\Scripts\activate.bat # this for cmd
```

```cmd
source myProject/Scripts/activate # git bash/linux and mac
```

> above all command to activate environment

```cmd
deactivate
```

> to de activate environment
