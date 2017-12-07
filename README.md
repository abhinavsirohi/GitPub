## GitPub - Python library to interact with github's public API
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


## Getting started!
Follow up these instructions if you want to see it in action up and running on your machine.

### System Requirements:


* [pytest](http://doc.pytest.org/en/latest/): Uses __pytest__ as the unit-testing framework. Install using <code>pip install pytest</code>.
* [requests](https://pypi.python.org/pypi/requests/2.11.1): Uses __requests__ for interacting with the various api urls.




### Few Final Steps:


*Step 1:* __Load Github Profile & Public Repo details of a user__: Loading a github profile just needs a _username_ to startwith. Here is a small demo with _username_ [__demfier__](https://github.com/Demfier).<br>

*Step 2:* Type the following commands in python shell:

```python
import gitpub

username = 'demfier' # there goes your username, inside ' '
profile = gitpub.Profile()
profile.load_gh_profile(username)  # loads profile details of `username`
profile.get_public_repos()  # loads all the public repo details of `username`
```

*Step 3:* __Run Tests__ : Just run the command `py.test -v` to see the test results.
   and you're done!!



## Contribution
Want to contribute? Awesome, we always wanted a larger development base. Jump into  [contribution instructions](CONTRIBUTING.md) for further instructions.

# LICENSE
The MIT License (MIT) 2017 - [Gaurav Sahu](https://github.com/demfier). Please have a look at the [LICENSE.txt](https://github.com/Demfier/GitPub/blob/master/LICENSE.txt) for more details.
