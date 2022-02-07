# JFrog-Art-CLI

Solution to JFrog's home assignment


## Workflow

I had to research pretty much EVERYTHING.

It is hard for me to cite sources, as my browsing history during this assignment had gotten **over 400 new entries**.

Most of these entries are about python syntax, and are not specificly relevant to this assignment.

The most prominent sources I used:

1. [JFrog's official Documentation](https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API)
2. [How to Generate an access Token](https://www.youtube.com/watch?v=OQ4_ZGCnqIo)
3. [python requests docs](https://docs.python-requests.org/en/master/user/quickstart/)
4. [stackoverflow](https://stackoverflow.com/), and specificly these threads:
4. * [1](https://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python), [2](https://stackoverflow.com/questions/13782198/how-to-do-a-put-request-with-curl), [3](https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist).
5. [DelfStack](https://www.delftstack.com/howto/python/python-clear-console/)

I also used [this tool](https://curlconverter.com/#) quite a lot.

### About some descisions I made during this project:

* **Writing dirty** - The time constraint was too tight for me to both learn how to do it all, *and* to do it pretty. while dirty is bloated, it often is the *fastest* way to a result (and I neede *fast*).
* **Creating an entire Shell** - A simple CLI is good when you only use it a small amounts of times in succession, but if you want to manage something that requires various variables, you don'y want to type them *every single time you run a command*; From a tool that helps you, a CLI can easily become jarring, and even harder to use. An interactive shell on the other hand, is ment for repetetive use.
* **Inserting path to access token** - It allowed me to create a bit of a safer 'cache', without the complications of encryption (which would be another thing to learn).
* **Repetitive password prompts** - Again, a security meassure. The password prompts are only used for commands which require an admin user.
* **Instance and Username caching** - Hard coding credentials isn't a good idea, but if only a single user works with the shell, it feels much smoother to only confirm your identity instead of re-supplying it every time, especially during testing.



## Console Usage:

Just type 'help' in console.

All commands are typed as their entire tree, except for commands in the 'misc' branch, which are not prefixed and only use the final command.

So for e.g, if you want to see your system version, the command you type is
> get system version

Or if you want to delete a user:
> DELETE user

But if you want to clear the console you'd only have to type:
> cls

Some commands ask you for further input, and commands that require an administrator access always ask for password confirmation.
Note that all misc commands are unprefixed