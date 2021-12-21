from github import Github
from model import GithubUser, Repo
import operator
import collections

TOKEN = "xxxx"
g = Github(TOKEN)


def searchUser(name):
    """ return user or none if not found"""
    users = g.search_users(name)
    if users.totalCount == 0:
        return None

    result = []
    for u in users:
        u = GithubUser(u.login, u.email, u.followers, u.bio, u.public_repos, u.type,
                       u.avatar_url, u.company, u.blog, u.created_at, u.location)
        result.append(vars(u))
    return result


def searchRepoByUser(name):
    try:
        user = g.get_user(name)
    except Exception as e:
        print(e)
        return None

    repos = user.get_repos()
    repo_list = []
    for repo in repos:
        try:
            newRepo = Repo(repo.name, repo.get_commits().totalCount, repo.get_languages(),
                           repo.stargazers_count, repo.get_topics())
            repo_list.append(newRepo)

        except Exception as err:
            print(err)
            continue

    commits_list = [r.commits for r in repo_list]
    languages_list = [r.languages for r in repo_list]
    stars_list = [{"name":r.name, "value": r.stars} for r in repo_list]
    languages_dict = convertListDict(languages_list, 5)
    topics_list = [t for r in repo_list for t in r.topics]
    topics_list = dict(collections.Counter(topics_list))
    topics_list = [{"word": k, "size": v} for k, v in topics_list.items()]
    return commits_list, languages_dict, stars_list, topics_list


def convertListDict(l, n):
    r = {}
    for d in l:
        for k, v in d.items():
            if k in r.keys():
                r[k] = r[k] + v
            else:
                r.setdefault(k, v)
    sorted_d = dict(sorted(r.items(), key=operator.itemgetter(1), reverse=True))

    return {k: sorted_d[k] for k in list(sorted_d)[:n]}

