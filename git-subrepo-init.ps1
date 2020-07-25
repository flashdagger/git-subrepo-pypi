<#
.Synopsis
Create, populate and start Python venv.

.Description
This is the `git-subrepo` powershell initialization script.
This script turns on the `git-subrepo` Git subcommand for Windows PowerShell
Just execute inside cmd.exe or another batch file:

   git-subrepo-init.ps1
#>

$Errors = @()

$module_path = $(python -c 'import subrepo; print(subrepo.__file__)')
$subrepo_dir = Join-Path (Get-Item $module_path).Directory 'subrepo'

$Env:GIT_SUBREPO_ROOT = $subrepo_dir
$Env:Path += ";$(Join-Path $subrepo_dir 'lib')"
$version = $(git subrepo --version)
Write-Host "using version $version in $subrepo_dir"
