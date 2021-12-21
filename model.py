class GithubUser:

    def __init__(self, name, email, followers, bio, public_repos_count,
                 user_type, avatar_url, company, blog, created_at, location):
        self.name = name
        self.email = email
        self.followers = followers
        self.bio = bio
        self.public_repos_count = public_repos_count
        self.user_type = user_type
        self.avatar_url = avatar_url
        self.company = company
        self.blog = blog
        self.created_at = created_at
        self.location = location
        self._repos = []

    def setRepos(self, repos):
        self._repos = repos

    def addRepos(self, repo):
        self._repos.append(repo)

    def getRepos(self):
        return self._repos

    def __str__(self) -> str:
        return "name: " + self.name


class Repo:

    def __init__(self, name, commits, languages, stars, topics):
        self.name = name
        #integer
        self.commits = commits
        #  dict of string to integer
        self.languages = languages
        # integer
        self.stars = stars
        # list of string
        self.topics = topics