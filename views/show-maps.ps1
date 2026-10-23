<#
.SYNOPSIS
  Put the semester topic map and Graph View on screen in Obsidian with one command.

.DESCRIPTION
  Uses Obsidian's own command line interface (Settings > General > Advanced >
  Command line interface, then "Register CLI"). Starts Obsidian on this vault if
  it is not running, closes stale canvas/graph tabs, opens both, and leaves the
  one named by -Show in front.

  Run from anywhere:  powershell -File views\show-maps.ps1
                      powershell -File views\show-maps.ps1 -Show graph
#>
param(
    [ValidateSet('canvas', 'graph')][string]$Show = 'canvas',
    [string]$Vault = 'computer_science_2',
    [string]$Canvas = 'views/semester-topic-map.canvas'
)

$ErrorActionPreference = 'Stop'

# The installer puts Obsidian.com (the CLI shim) next to Obsidian.exe; `obsidian`
# is on PATH only after "Register CLI" has been run.
$cli = (Get-Command obsidian -ErrorAction SilentlyContinue).Source
if (-not $cli) { $cli = Join-Path $env:LOCALAPPDATA 'Programs\Obsidian\Obsidian.com' }
if (-not (Test-Path $cli)) { throw "Obsidian CLI not found. Install: winget install --id Obsidian.Obsidian -e --scope user" }

function Invoke-Obsidian {
    & $cli @args "vault=$Vault" 2>&1 | Out-String
}

if (-not (Get-Process Obsidian -ErrorAction SilentlyContinue)) {
    Start-Process "obsidian://open?vault=$Vault"
}

# Wait until the running app answers.
$ready = $false
for ($i = 0; $i -lt 30 -and -not $ready; $i++) {
    $ready = (Invoke-Obsidian vault) -match 'name\s+' + [regex]::Escape($Vault)
    if (-not $ready) { Start-Sleep 1 }
}
if (-not $ready) { throw "Obsidian did not respond for vault '$Vault' within 30 seconds." }

# Close stale copies so repeated runs do not pile up tabs.
$null = Invoke-Obsidian eval "code=(() => { app.workspace.detachLeavesOfType('canvas'); app.workspace.detachLeavesOfType('graph'); return 'ok'; })()"

if ($Show -eq 'canvas') {
    $null = Invoke-Obsidian tab:open view=graph
    $null = Invoke-Obsidian open "path=$Canvas" newtab
} else {
    $null = Invoke-Obsidian open "path=$Canvas"
    $null = Invoke-Obsidian tab:open view=graph
}

# Fit the canvas to the pane so the whole map is visible, not a corner of it.
$null = Invoke-Obsidian eval "code=(() => { const l = app.workspace.getLeavesOfType('canvas')[0]; if (l && l.view.canvas) l.view.canvas.zoomToFit(); return 'ok'; })()"

(Invoke-Obsidian workspace) -split "`r?`n" | Where-Object { $_ -match '\[(canvas|graph)\]' } | ForEach-Object { Write-Host $_.Trim() }
