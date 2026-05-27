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
export PATH='/c/Users/Sascha Zielke/bin:/mingw64/bin:/usr/local/bin:/usr/bin:/bin:/mingw64/bin:/usr/bin:/c/Users/Sascha Zielke/bin:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files (x86)/NVIDIA Corporation/PhysX/Common:/c/Program Files/Docker/Docker/resources/bin:/c/Program Files/NVIDIA Corporation/NVIDIA App/NvDLISR:/c/Program Files/nodejs:/cmd:/c/Users/Sascha Zielke/AppData/Local/Microsoft/WindowsApps:/c/Users/Sascha Zielke/AppData/Roaming/npm:/c/Users/Sascha Zielke/AppData/Local/GitHubDesktop/bin:/c/Users/Sascha Zielke/AppData/Local/Programs/Microsoft VS Code/bin:/c/Program Files/nodejs:/mingw64/bin:/usr/bin/vendor_perl:/usr/bin/core_perl:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/c9c03020-54b3-40c1-8826-ee0939b25c52/18364419-124c-4e68-b4c7-5d4d8eccd957/bin:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/18364419-124c-4e68-b4c7-5d4d8eccd957/c9c03020-54b3-40c1-8826-ee0939b25c52/rpm/plugin_0155zZVATbJU3jHUmPP9NvMC/bin:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/18364419-124c-4e68-b4c7-5d4d8eccd957/c9c03020-54b3-40c1-8826-ee0939b25c52/rpm/plugin_01XXJmxLXPEhPMmnxmrgntNw/bin:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/18364419-124c-4e68-b4c7-5d4d8eccd957/c9c03020-54b3-40c1-8826-ee0939b25c52/rpm/plugin_01Eeb9y5m4iFuY3yRtytYfdc/bin:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/18364419-124c-4e68-b4c7-5d4d8eccd957/c9c03020-54b3-40c1-8826-ee0939b25c52/rpm/plugin_01FTLa86dhbVJ3HB1LdHdhN7/bin:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/18364419-124c-4e68-b4c7-5d4d8eccd957/c9c03020-54b3-40c1-8826-ee0939b25c52/rpm/plugin_01VTbvGZYaCVU2CNSvhDCnkg/bin:/c/Users/Sascha Zielke/AppData/Roaming/Claude/local-agent-mode-sessions/18364419-124c-4e68-b4c7-5d4d8eccd957/c9c03020-54b3-40c1-8826-ee0939b25c52/rpm/plugin_012ABz1xjgtJYWKrcJkXW6ad/bin'
