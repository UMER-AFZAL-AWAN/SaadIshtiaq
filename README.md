# SaadIshtiaq

Using py 3.12.3 for this project

Why are these three different commands -- TODO 
PS C:\D\Codes\SaadBhaiBackChod\SaadIshtiaq> python --version                                                                                                          
Python 3.10.11                                                                                                                   
PS C:\D\Codes\SaadBhaiBackChod\SaadIshtiaq> python3 --version
Python 3.14.3
PS C:\D\Codes\SaadBhaiBackChod\SaadIshtiaq> py --version
Python 3.12.3
PS C:\D\Codes\SaadBhaiBackChod\SaadIshtiaq> 


FOR UBUNTU:
To activate the virtual env: source .venv/bin/activate

launch.json parameters
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [

    {
      "name": "Python Debugger: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "python": "${workspaceFolder}/.venv/bin/python"
    }
  ]
}

settings.json parameters
{
  "python.terminal.activateEnvironment": true,
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python-envs.pythonProjects": [],
}