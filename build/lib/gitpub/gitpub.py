"""
Module to interact with public github API
 (https://developer.github.com/guides/getting-started/)
"""
import requests

# For disabling the InsecurePlatForm warnings
# (arises when using requests in python 2.x)
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import os
import requests


class Repository(object):
    """Class to represent a Github Repository"""

    def __init__(self, name=None, html_url=None, stargazers_count=None,
                 description=None, home_page=None, cursor=None):
        """
        Initializes a `Repository` object
        Parameters
        -------------------------------------------
        name : str
            Contains name of the repository
        html_url : str
            Contains link to the repository
        stargazers_count : int
            Shows number of stars to the repository
        description : str
            Contains repository description
        home_page : str
            link to the home_page of repository
        """

        self.name = name
        self.html_url = html_url
        self.stargazers_count = stargazers_count
        self.description = description
        self.home_page = home_page
        self.cursor = cursor


class Profile(object):
    """Class to represent a Github Profile"""

    def __init__(self, username=None, name=None, location=None, email=None,
                 followers_count=None, repos_url=None, public_repos=None,
                 public_repo_count=None):
        """
        Initializes a `Profile` object
        Parameters
        ---------------------------------
        username : str
            Contains username of the user
        name : str
            Contains name of the user
        location : str
            Contains location of the user
        email : str
            Contains email-id of the user
        followers_count : int
            Total number of followers
        repos_url : str
            Link to the repository details of user
        public_repos : [github.Repository objects]
            List containing details of all the repositories of user
        public_repo_count : int
            Total public repositories of the user
        """

        self.username = username
        self.name = name
        self.location = location
        self.email = email
        self.followers_count = followers_count
        self.repos_url = repos_url
        self.public_repos = public_repos
        self.public_repo_count = public_repo_count

    def load_gh_profile(self, username):
        """
        Loads `name`, 'location', `email`, `followers_count`, `repos_url` &
        `public_repo_count` into a github.Profile object given a `username`
        Parameters
        --------------------------------------------------------------------
        username : str
            Username of the person whose profile details to be loaded
        """
        
        self.username = username

        # build api url for the user
        try:
            url = 'https://api.github.com/graphql'
            json = { 'query' : '{user(login:"' + self.username + '") { name url email location followers{totalCount} repositories{totalCount}}}'}
            headers = {"Authorization": os.environ['OAUTH_KEY']}

            profile = requests.post(url=url, json=json, headers=headers)

            profile = profile.json()['data']['user']



        except requests.Timeout:
            return("Connection Timed out\
                    while loading profile for %s" % username)
        except requests.ConnectionError:
            return("Error in Connection \
                   while loading profile for %s" % username)
        except requests.HTTPError as e:
            return("HTTPError while sending \
                     requesting while loading profile for %s" % username)
        except ValueError:
            return("No JSON found in the request")
        except KeyError:
            return("No authentication key provided")


        # fill details
        self.name = profile['name']
        self.location = profile['location']
        self.email = profile['email']

        self.followers_count = profile['followers']['totalCount']
        self.repos_url = "https://api.github.com/users/" + username + "/repos"
        self.public_repo_count = profile['repositories']['totalCount']
        print ("Loaded Github profile of %s" % self.username)


    def get_public_repos(self):
    
        """
        Fetches all the public repository details of a user & stores as an
        array of github.Repository objects in the `public_repos` attribute of
        a github.Profile object
        ------------------------------------------------------------------------
        Parameters: None
        """
    

        # if no profile loaded
        if self.username is None:
            return("No Github profile has been loaded yet.  \
                   Please load a Github Profile first to get a  \
                   list of their public repositories")

        gh_repo_url = self.repos_url
        repos_count = 0  # number of repos whose details are fetched



        repos = []  # array to store fetched `Repository`

        
        try:
            url = 'https://api.github.com/graphql'
            json = { 'query' : '{user(login:"' + self.username + '") {repositories(first:100){edges{ cursor node{ name id stargazers{ totalCount }description url homepageUrl}}totalCount}}}'}
            headers = {"Authorization": os.environ['OAUTH_KEY']}

            rep = requests.post(url=url, json=json, headers=headers)

            rep=rep.json()['data']['user']['repositories']

        except requests.Timeout:
            return ("Connection Timed out while loading public repos of %s" % self.username)
        except requests.ConnectionError:
            return ("Error in Connection while loading  public repos of %s" % self.username)
        except requests.HTTPError as e:
            return ("HTTPError while sending requesting while loading  public repos of %s" % self.username)
        except ValueError:
            return "No JSON found in the request"
        except KeyError:
            return("No authentication key provided")


        

        repos = rep['edges']
        repos_count=self.public_repo_count
        self.public_repos = []

        print("Found %s repositories.\n\
              Fetching repo details..." % repos_count)
        

        # fill fetched repo details
        for idx in repos:
            repo = Repository()
            repo.cursor=idx['cursor']
            repo.name = idx['node']['name']
            repo.html_url = idx['node']['url']
            repo.stargazers_count = idx['node']['stargazers']['totalCount']
            repo.description = idx['node']['description']
            repo.home_page = idx['node']['homepageUrl']
            self.public_repos.append(repo)

        
        
        while(repos_count>0):

            try:
                url = 'https://api.github.com/graphql'
                json = { 'query' : '{user(login:"' + self.username + '") {repositories(first:100,after:"' + self.public_repos[-1].cursor + '"){edges{ cursor node{ name id stargazers{ totalCount }description url homepageUrl}}totalCount}}}'}
                headers = {"Authorization": os.environ['OAUTH_KEY']}

                rep = requests.post(url=url, json=json, headers=headers)

                rep=rep.json()['data']['user']['repositories']

            except requests.Timeout:
                return("Connection Timed out while \
                        loading public repos of %s" % self.username)
            except requests.ConnectionError:
                return("Error in Connection while \
                         loading  public repos of %s" % self.username)
            except requests.HTTPError as e:
                return("HTTPError while sending requesting while \
                         loading  public repos of %s" % self.username)
            except ValueError:
                return("No JSON found in the request")

            repos = rep['edges']

            for idx in repos:
                repo = Repository()
                repo.cursor=idx['cursor']
                repo.name = idx['node']['name']
                repo.html_url = idx['node']['url']
                repo.stargazers_count = idx['node']['stargazers']['totalCount']
                repo.description = idx['node']['description']
                repo.home_page = idx['node']['homepageUrl']
                self.public_repos.append(repo)

            repos_count-=100


        print ("Loaded all repositories for {}".format(self.username))


