Git / GitHub Vudoo

```
--system, --global, --local
```
```
git config --global user.name "username"
git config --global user.name

git config --global user.email "davidkypuros"
git config --global user.email
```

[Create a GitHub Repo from APIs

Example command:
```
curl -u 'USER' https://api.github.com/user/repos -d '{"name":"REPO"}'
```

My Specific command:
```
curl -u 'davidkypuros@gmail.com' https://api.github.com/user/repos -d '{"name":"favoritecommands"}'
#<enter password>

#Look in the output
  "git_url": "git://github.com/dkypuros/favoritecommands.git",

pwd
/home/davidkypuros
git clone git://github.com/dkypuros/favoritecommands.git

git add .
git status
git log
git commit -s  #add message :wq!
git log
git status #not staged
git push https://github.com/dkypuros/favoritecommands.git


...cli output...
Cloning into 'favoritecommands'...
warning: You appear to have cloned an empty repository.


```

<details><summary>CLI output</summary>
<p>

#### $curl -u 'davidkypuros@gmail.com' https://api.github.com/user/repos -d '{"name":"favoritecommands"}'

```
...cli output of command...

{
  "id": 261494969,
  "node_id": "MDEwOlJlcG9zaXRvcnkyNjE0OTQ5Njk=",
  "name": "favoritecommands",
  "full_name": "dkypuros/favoritecommands",
  "private": false,
  "owner": {
    "login": "dkypuros",
    "id": 363856,
    "node_id": "MDQ6VXNlcjM2Mzg1Ng==",
    "avatar_url": "https://avatars1.githubusercontent.com/u/363856?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/dkypuros",
    "html_url": "https://github.com/dkypuros",
    "followers_url": "https://api.github.com/users/dkypuros/followers",
    "following_url": "https://api.github.com/users/dkypuros/following{/other_user}",
    "gists_url": "https://api.github.com/users/dkypuros/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/dkypuros/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/dkypuros/subscriptions",
    "organizations_url": "https://api.github.com/users/dkypuros/orgs",
    "repos_url": "https://api.github.com/users/dkypuros/repos",
    "events_url": "https://api.github.com/users/dkypuros/events{/privacy}",
    "received_events_url": "https://api.github.com/users/dkypuros/received_events",
    "type": "User",
    "site_admin": false
  },
  "html_url": "https://github.com/dkypuros/favoritecommands",
  "description": null,
  "fork": false,
  "url": "https://api.github.com/repos/dkypuros/favoritecommands",
  "forks_url": "https://api.github.com/repos/dkypuros/favoritecommands/forks",
  "keys_url": "https://api.github.com/repos/dkypuros/favoritecommands/keys{/key_id}",
  "collaborators_url": "https://api.github.com/repos/dkypuros/favoritecommands/collaborators{/collaborator}",
  "teams_url": "https://api.github.com/repos/dkypuros/favoritecommands/teams",
  "hooks_url": "https://api.github.com/repos/dkypuros/favoritecommands/hooks",
  "issue_events_url": "https://api.github.com/repos/dkypuros/favoritecommands/issues/events{/number}",
  "events_url": "https://api.github.com/repos/dkypuros/favoritecommands/events",
  "assignees_url": "https://api.github.com/repos/dkypuros/favoritecommands/assignees{/user}",
  "branches_url": "https://api.github.com/repos/dkypuros/favoritecommands/branches{/branch}",
  "tags_url": "https://api.github.com/repos/dkypuros/favoritecommands/tags",
  "blobs_url": "https://api.github.com/repos/dkypuros/favoritecommands/git/blobs{/sha}",
  "git_tags_url": "https://api.github.com/repos/dkypuros/favoritecommands/git/tags{/sha}",
  "git_refs_url": "https://api.github.com/repos/dkypuros/favoritecommands/git/refs{/sha}",
  "trees_url": "https://api.github.com/repos/dkypuros/favoritecommands/git/trees{/sha}",
  "statuses_url": "https://api.github.com/repos/dkypuros/favoritecommands/statuses/{sha}",
  "languages_url": "https://api.github.com/repos/dkypuros/favoritecommands/languages",
  "stargazers_url": "https://api.github.com/repos/dkypuros/favoritecommands/stargazers",
  "contributors_url": "https://api.github.com/repos/dkypuros/favoritecommands/contributors",
  "subscribers_url": "https://api.github.com/repos/dkypuros/favoritecommands/subscribers",
  "subscription_url": "https://api.github.com/repos/dkypuros/favoritecommands/subscription",
  "commits_url": "https://api.github.com/repos/dkypuros/favoritecommands/commits{/sha}",
  "git_commits_url": "https://api.github.com/repos/dkypuros/favoritecommands/git/commits{/sha}",
  "comments_url": "https://api.github.com/repos/dkypuros/favoritecommands/comments{/number}",
  "issue_comment_url": "https://api.github.com/repos/dkypuros/favoritecommands/issues/comments{/number}",
  "contents_url": "https://api.github.com/repos/dkypuros/favoritecommands/contents/{+path}",
  "compare_url": "https://api.github.com/repos/dkypuros/favoritecommands/compare/{base}...{head}",
  "merges_url": "https://api.github.com/repos/dkypuros/favoritecommands/merges",
  "archive_url": "https://api.github.com/repos/dkypuros/favoritecommands/{archive_format}{/ref}",
  "downloads_url": "https://api.github.com/repos/dkypuros/favoritecommands/downloads",
  "issues_url": "https://api.github.com/repos/dkypuros/favoritecommands/issues{/number}",
  "pulls_url": "https://api.github.com/repos/dkypuros/favoritecommands/pulls{/number}",
  "milestones_url": "https://api.github.com/repos/dkypuros/favoritecommands/milestones{/number}",
  "notifications_url": "https://api.github.com/repos/dkypuros/favoritecommands/notifications{?since,all,participating}",
  "labels_url": "https://api.github.com/repos/dkypuros/favoritecommands/labels{/name}",
  "releases_url": "https://api.github.com/repos/dkypuros/favoritecommands/releases{/id}",
  "deployments_url": "https://api.github.com/repos/dkypuros/favoritecommands/deployments",
  "created_at": "2020-05-05T14:28:51Z",
  "updated_at": "2020-05-05T14:28:51Z",
  "pushed_at": "2020-05-05T14:28:52Z",
  "git_url": "git://github.com/dkypuros/favoritecommands.git",
  "ssh_url": "git@github.com:dkypuros/favoritecommands.git",
  "clone_url": "https://github.com/dkypuros/favoritecommands.git",
  "svn_url": "https://github.com/dkypuros/favoritecommands",
  "homepage": null,
  "size": 0,
  "stargazers_count": 0,
  "watchers_count": 0,
  "language": null,
  "has_issues": true,
  "has_projects": true,
  "has_downloads": true,
  "has_wiki": true,
  "has_pages": false,
  "forks_count": 0,
  "mirror_url": null,
  "archived": false,
  "disabled": false,
  "open_issues_count": 0,
  "license": null,
  "forks": 0,
  "open_issues": 0,
  "watchers": 0,
  "default_branch": "master",
  "permissions": {
    "admin": true,
    "push": true,
    "pull": true
  },
  "allow_squash_merge": true,
  "allow_merge_commit": true,
  "allow_rebase_merge": true,
  "delete_branch_on_merge": false,
  "network_count": 0,
  "subscribers_count": 1
}

```
</p>
</details>


use SSH Keys to "git push"

```
cd ~/.ssh
ssh-keygen -t rsa -C "davidkypuros@gmail.com"

```


[davidkypuros@localhost favoritecommands]$ cd ~/.ssh
[davidkypuros@localhost .ssh]$ ls
known_hosts
[davidkypuros@localhost .ssh]$ ssh-keygen -t rsa -C "davidkypuros@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/davidkypuros/.ssh/id_rsa):
Enter passphrase (empty for no passphrase): XXXXXX
Enter same passphrase again: XXXXXXX
Your identification has been saved in /home/davidkypuros/.ssh/id_rsa.
Your public key has been saved in /home/davidkypuros/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:XXXXX XXXXXXXXXXxs@gmail.com
The key's randomart image is: XXXXXX


[davidkypuros@localhost .ssh]$ ls
id_rsa  id_rsa.pub  known_hosts


SSH way to connect
```
git@github.com:dkypuros/favoritecommands.git
```

```
cd /home/davidkypuros/favoritecommands
vim .git/config

```


before
```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = git://github.com/dkypuros/favoritecommands.git
        fetch = +refs/heads/*:refs/remotes/origin/*

```

after
```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = git@github.com:dkypuros/favoritecommands.git
        fetch = +refs/heads/*:refs/remotes/origin/*


```


git push --set-upstream origin master

... cli output ...

```
The authenticity of host 'github.com (140.82.112.4)' can't be established.
RSA key fingerprint is SHA256:XXXXX.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,140.82.112.4' (RSA) to the list of known hosts.
```
