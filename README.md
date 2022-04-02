# xkcd2601

This is a project to transcribe xkcd #2601, the April Fools post for 2022, to runnable logo code.

### Running the code:

There are options.

#### jslogo

One of the developers of #2601 [helpfully shared](https://github.com/theinternetftw/xkcd2601/issues/26)
that the logo they used to develop the code was jslogo, which can be found online [here](https://www.calormen.com/jslogo/).
To run the current iteration of the transcription in it, copy/paste the code into the window, then stick a line that says
**xkcd** at the bottom of it all. If the image doesn't fit in your window, add **SETSCRUNCH 0.5 0.5** (or some other decimal)
to the code right before you call xkcd.

This is fun to watch, and renders very nicely, but is slow (at least on my laptop).

#### xkcd 2601 Drawer

Benedikt Werner made a dedicated [xkcd 2601 drawer](https://benediktwerner.github.io/xkcd-2601-drawer/) with a 
zooming/panning feature, which is very fast and loads the latest version of the logo code from this repo. Click the 
"Load latest" and "Draw" buttons, use scroll-up/down to zoom in/out, click-and-drag to pan around.

#### makesvg.py

There's also now a python script to generate an svg, which might be of use.

#### FMSLogo

To quickly run the code again and again to check the commits as they come in, I'm currently
using FMSLogo, which is windows only, sadly. But it might also run on your native logo
variant of choice.

If you know of a better fast-rendering, multi-platform logo variant that runs
this code as is or close to it, feel free to file a bug report with that info.

To run this code in FMSLogo, open the file, then in the console, type **xkcd**.

To open the file for editing in FMSLogo, you press the inscrutable "Edall"
button. You must then save and close your edit before running it again, or
highlight lines in the editor and hit ctrl-R to run them immediately.

Like I said, any good, fast alternatives to this logo interpreter are welcome.

### Aiding transcription

If you want to aid transcription, take a look at the code to get a sense of what
things should look like. Make what you write look like that. Claim a time period in
the [file](https://xkcd.com/2601/radio.mp3) (in chunks of 10 minutes) with a bug report.
File your transcription with a pull request.

In the pull request, start and end your contribution with a comment showing the time, and
add additional timestamps every 5 minutes or so, which will make it easier to fix transcription
bugs. They should look like e.g.

**; NOTE: [00:40:00]**

If you don't know how things should be typed out, check the current code or some logo docs.
[This is what I've been using.](http://people.eecs.berkeley.edu/~bh/usermanual)

Try to run your code before submitting by sticking it at the end of what we already have. Make sure it looks sane.

If you don't have a github account and want to help, you can message me on reddit if you
have an account there, and I'll update the bugs and such accordingly.

### First 270 minutes of transcription:

![first 270 minutes](https://github.com/Gh05t-1337/xkcd2601/blob/main/screens/xkcd2601.png)
