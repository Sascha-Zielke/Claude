# Snapshot file
# Unset all aliases to avoid conflicts with functions
unalias -a 2>/dev/null || true
shopt -s expand_aliases
# Check for rg availability
if ! (unalias rg 2>/dev/null; command -v rg) >/dev/null 2>&1; then
  function rg {
  local _cc_bin="${CLAUDE_CODE_EXECPATH:-}"
  [[ -x $_cc_bin ]] || _cc_bin='/c/Users/Sascha Zielke/.local/bin/claude.exe'
  if [[ ! -x $_cc_bin ]]; then command rg "$@"; return; fi
  if [[ -n $ZSH_VERSION ]]; then
    ARGV0=rg "$_cc_bin" "$@"
  elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
    ARGV0=rg "$_cc_bin" "$@"
  elif [[ $BASHPID != $$ ]]; then
    exec -a rg "$_cc_bin" "$@"
  else
    (exec -a rg "$_cc_bin" "$@")
  fi
}
fi
export PATH='/c/Users/Sascha Zielke/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/Sascha Zielke/bin:/c/Program Files/nodejs:/c/Users/Sascha Zielke/AppData/Roaming/npm:/c/Users/Sascha Zielke/AppData/Local/Programs/nodejs:/c/Users/Sascha Zielke/AppData/Local/Programs/node:/c/Program Files (x86)/nodejs:/c/Users/Sascha Zielke/AppData/Roaming/nvm:/c/Users/Sascha Zielke/.volta/bin:/c/Users/Sascha Zielke/AppData/Local/fnm:/c/ProgramData/chocolatey/bin:/c/Users/Sascha Zielke/scoop/shims:/c/Users/Sascha Zielke/scoop/apps/nodejs/current/bin:/c/Users/Sascha Zielke/scoop/apps/nodejs/current:/c/Program Files/Docker/Docker/resources/bin:/c/Users/Sascha Zielke/.local/bin:/c/Users/Sascha Zielke/.bun/bin:/c/Users/Sascha Zielke/.opencode/bin:/c/Users/Sascha Zielke/AppData/Local/Programs/Obsidian:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/Program Files/NVIDIA Corporation/NVIDIA App/NvDLISR:/c/Program Files/nodejs:/cmd:/c/Users/Sascha Zielke/AppData/Local/Microsoft/WindowsApps:/c/Users/Sascha Zielke/AppData/Local/GitHubDesktop/bin:/c/Users/Sascha Zielke/AppData/Local/Programs/Microsoft VS Code/bin:/usr/bin/vendor_perl:/usr/bin/core_perl'
