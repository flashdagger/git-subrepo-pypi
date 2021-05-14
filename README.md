
# Git subrepo python package
Provides easy deployment for [git subrepo](https://github.com/ingydotnet/git-subrepo).


## How to use
### Prerequisites
 - git >= 2.10.0 (on path)
 - python >= 3.6


### Installation
Stable releases can be installed via [PyPI](https://pypi.python.org/pypi/git-subrepo):
```bash
$ pip install git-subrepo
```

### Usage
Run the subrepo command to see usage
```bash
subrepo <command> <argument> <options>
```

### shell support
If you need to use subrepo as `git subrepo` command use the init scripts

#### Bash
```bash
$ source git-subrepo-init.sh
$ git subrepo version
```

#### Cmd
```bash
> git-subrepo-init.bat
> git subrepo version
```

#### PowerShell
```bash
PS> .\git-subrepo-init.ps1
PS> git subrepo version
```


## License
[MIT license](LICENSE).
