from pyinfra.operations import apt

apt.update(
    name="Update apt",
    _sudo=True,
)

apt.upgrade(
    name="Upgrade apt",
    _sudo=True,
)

apt.packages(
    name="install base packages",
    packages=["curl", "git", "vim", "tmux", "zsh", "build-essential", "libssl-dev", "libreadline-dev", "zlib1g-dev", "libncurses5-dev", "libffi-dev", "libgdbm-dev", "libdb-dev", "libbz2-dev", "liblzma-dev", "libsqlite3-dev", "libxml2-dev", "libxslt1-dev", "libyaml-dev"],
    present=True,
    _sudo=True,
)