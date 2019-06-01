import pathlib
from git import Repo
from git.exc import GitCommandError

def sparse_checkout(repo_name, remote_url, paths):
    """ Do a sparse checkout for a remote repository
        Given a repo name a remote url
        "path" is used to specify the directory in the remote repository
    """
    try:
        repo = Repo.init(repo_name)
        remote = repo.create_remote('origin', url=remote_url)
        origin = repo.remotes.origin
        config = repo.config_writer()
        config.set_value('core', 'sparsecheckout', True)
        config.release()
        sparse_checkout_file = pathlib.Path(repo_name) / pathlib.Path('.git/info/sparse-checkout')
        with open(sparse_checkout_file, 'w') as f:
            f.write("\n".join(paths))
        origin.fetch(depth=1)
    except GitCommandError as e:
        pass

    origin = repo.remotes.origin
    origin.pull("master", depth=1)