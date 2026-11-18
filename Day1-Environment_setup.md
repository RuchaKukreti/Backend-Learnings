## 1. Create a virtual environment

**Command:**
```powershell
python -m venv .venv
```
- Creates an isolated Python environment for the project.
- Prevents dependency and version conflicts between different projects.

## 2. Change PowerShell execution policy

**Command:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- Allows locally created PowerShell scripts to execute.
- Applies the policy change only to the current Windows user.

## 3. Activate virtual environment

**Command:**
```powershell
.\.venv\Scripts\Activate.ps1
```
- Activates the project's virtual environment.
- Uses its Python interpreter and packages in the current terminal.

**Verification:** Terminal displays `(.venv)`.

## 4. Verify pip inside virtual environment

**Command:**
```powershell
python -m pip --version
```
- Checks the installed pip version.
- Confirms pip is running from the project's virtual environment.

## 5. Install FastAPI

**Command:**
```powershell
python -m pip install fastapi
```
- Installs FastAPI and its