export CLICOLOR=1
export LSCOLORS=Exfxcxdxbxegedabagacad
export TERM=xterm-256color
export JAVA_HOME=$(/usr/libexec/java_home –v 1.8)
export PROMPT_COMMAND="echo -n \[\$(date +%H:%M:%S)\]\ "

alias up="cd .."
alias sublime="open -a /Applications/Sublime\ Text.app"
alias projects="cd ~/Documents/test-projects && ls"
alias desk="cd ~/Desktop && pwd"
alias work="desk && python get_started_at_work.py"
alias work_projects="cd ~/Documents/work_projects && pwd"
alias gpr="git pull --rebase"
alias chrome="open -na \"Google Chrome\""
alias bash_profile="cd ~ && sublime .bash_profile"
alias reload_bash="source .bash_profile"