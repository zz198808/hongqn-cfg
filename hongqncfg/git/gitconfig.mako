[user]
	name = Qiangning Hong
	email = hongqn@douban.com
[core]
	excludesfile = ~/.gitignore
[alias]
	st = status
	co = checkout
	br = branch
	ci = commit
[color]
	ui = true
%if facts.system == 'Darwin':
[credential]
	helper = osxkeychain
%endif
[push]
	default = simple
