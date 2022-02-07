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
4. [stackoverflow](https://stackoverflow.com/), and specificly these threads: [1](https://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python), [2](https://stackoverflow.com/questions/13782198/how-to-do-a-put-request-with-curl), [3](https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist)
5. [DelftStack](https://www.delftstack.com/howto/python/python-clear-console/)
6. [Creating a simple Python Interactive Shell](https://www.youtube.com/watch?v=B55roI7rE_Y)

I also used [this tool](https://curlconverter.com/#) quite a lot.

### About some descisions I made during this project:

While I was given a week, A few hours later I was asked to do it in half the time if possible. Decided I'm up for the challenge. But for this, I had to make several compromises - since a compromise is supposed to satisfy both parties, I do believe I made the right descision.

* **Writing dirty -** The time constraint was too tight for me to both learn how to do it all, *and* to do it pretty. while dirty is bloated, it often is the *fastest* way to a result (and I needed *fast*).
* **Creating an entire Shell -** A simple CLI is good when you only use it a small amounts of times in succession, but if you want to manage something that requires various variables, you don'y want to type them *every single time you run a command*; From a tool that helps you, a CLI can easily become jarring, and even harder to use. An interactive shell on the other hand, is ment for repetetive use.
* **Inserting path to access token -** It allowed me to create a bit of a safer 'cache', without the complications of encryption (which would be another thing to learn).
* **Repetitive password prompts -** Again, a security meassure. The password prompts are only used for commands which require an admin user.
* **Instance and Username caching -** Hard coding credentials isn't a good idea, but if only a single user works with the shell, it feels much smoother to only confirm your identity instead of re-supplying it every time, especially during testing.
* **Keeping a non-working function -** The funciton to `post create user` does not work. Due to time constraints I could not debug it, but it is important to me that you know I made an effort.
* **Keeping an untested function -** The fucntion to `put create repository` is untested; Since I don't have a config file, I had no way to test it, but still decided to go for this function in order to display another html verb (put).
* **Creating an `expire password` function -** While I was not asked to create such funciton, I still wanted to display a *post* function that works, and this was a quick one. I couldn't test it since I have no *pro access*, but it did not throw any errors - so I guess it's a win?
* **Uppercase DELETE function -** This one is rather destructive, so I want the user to pay attention to what they're doing. I think braking syntax in a logical way is a nice safty mechanism considering time constraints, and using `DELETE user` has the added bonus of being a great rage outlet ;).
* **Input line starting with `():` -** It looks like a frog. Definetly a relevant feature.


## Console Usage:

Just type `help` in console.

All commands are typed as their entire tree, except for commands in the 'misc' branch, which are not prefixed and only use the final command.

So for e.g, if you want to see your system version, the command you type is
> `get system version`

Or if you want to delete a user:
> `DELETE user`

But if you want to clear the console you'd only have to type:
> `cls`

Some commands ask you for further input, and commands that require an administrator access always ask for password confirmation.
Note that all misc commands are unprefixed