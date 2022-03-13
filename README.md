# _The Chonker_

_The Chonker_ is a comprehensive dictionary for PangaeaPanga and Raysfire’s lingo.

## Story

This is how _The Chonker_ came to be.

On the [r/pangaeapanga](https://reddit.com/r/pangaeapanga) subreddit, I once saw [this dictionary](https://www.reddit.com/r/pangaeapanga/comments/o6e0se/i_updated_the_panga_dictionary_with_a_few_words/), which back then had something like four pages? Three? It was small either way, so I regularly left comments with suggestions for addition, until the [giant new 8-page update](https://www.reddit.com/r/pangaeapanga/comments/qtahy6/new_updated_8page_panga_dictionary/) came out. I realised that there was much more potential than this document, so I copied it into a spreadsheet, and added new entries, examples and references almost daily.

Panga mentioned once that he took over the habit of pronouncing ‘block’ with a dark ‘o’ from Raysfire, so I started checking his channel out too, to see how related their lingo would be. And it yielded tons of new terms that I happily kept track of in the spreadsheet.

It got very large, but it remained structured, because I consistently adhered to a small set of rules.

## Implementation

_The Chonker_ is made up of two parts:

- the **spreadsheet**, which contains the raw data;
- the **Python script**, which converts it to a website.

### Spreadsheet

The main spreadsheet has a simple structure. Each row is one term; a cell can be either of four things:

- a **term** (always & only the first column)
- an **example**
- a **meaning**
- an **internal reference**

Furthermore, _in_ a cell, there can be:

- a **context** (a set of parenthesis at the beginning of a cell or after a semicolon)
- a **tilde** (to replace the term; I saw this in a real dictionary and it’s super useful)
- a **separator** (only before an _example_ or a _meaning_)
- an **external reference** (a YouTube ID + timestamp)

This spreadsheet can be exported to a TSV file and this is then fed into the Python script.

### Python script

With the help of a Python script – and surprisingly few errors along the way, because I’m a cracked programmer – I converted the TSV file into an HTML file. Some interesting regular expressions were also necessary to convert e.g. the external references.

## Naming

The original name, _PangaeaPanga Dictionary_, became stale. (To be frank, it was already boring, though descriptive.) With all the new Raysfire lingo added in, it needed a more creative name. I thought about _Dictionary for the Fans_ or _The Juicer_, but these didn’t make it: the first one was boring, and using ‘juicer’ would interfere with the actual, frequently used meaning, and that isn’t desirable.

Eventually, I settled on _The Chonker_. ‘Chonker’ had then appeared once in a Panga video ([that’s _a_ chonker, dude](https://thechonker.fans/#chonker)). It is immediately clear what it means – it’s a derivative of ‘chonky’ (huge) – and it the term isn’t used that often by our bois. In any case, using ‘the’ made it distinctive enough.

I registered [thechonker.fans](https://thechonker.fans/) because I noticed the .fans domain, and it was the same price as a .com – couldn’t let that opportunity slide. With the definitive article, for consistency.

## Acknowledgements

Thanks to [u/Garlicboy101](https://reddit.com/user/Garlicboy101) for [the original concept](https://www.reddit.com/r/pangaeapanga/comments/o4xoox/i_put_together_a_dictionary_of_pangaspecific/) of a dictionary for PangaeaPanga lingo. _The Chonker_ would not have existed without your work.

I should also either thank or blame Raysfire for this, as he has often mentioned that someone should really put together a dictionary of lingo. [One post](https://www.reddit.com/r/Raysfire/comments/ssuds2/raysfire_lingo_dictionary_part_1/) on the [r/Raysfire](https://reddit.com/r/Raysfire) subreddit, which showcased and explained six terms, reached the weekly top and therefore the [Reddit recap](https://youtu.be/I_-M3zq38sg?t=102), where Raysfire said he was going to ‘critique these definitions’. If you have time for _The Chonker_, Rays – well, you’re probably going to fully read it out of interest anyway – I would much appreciate some devastating feedback; don’t spare me.

## Suggestions

If you have any suggestions for new entries, share them with me! Although I watch all _Super Mario Maker 2_ videos by [Raysfire](https://www.youtube.com/c/raysfireplus) and [PangaeaPanga](https://www.youtube.com/user/PangaTAS), a YouTube link is appreciated. In addition to the main tab of the spreadsheet, I also have a secondary tab with pending entries – about 200 at the moment. Most of them have only occurred once; some of them are hard to describe and are only on there for procrastination reasons.

The general guideline is: if the term has appeared in two separate videos, it gets added. This will make sure that the term is remembered, which makes it more likely to settle into the permanent lingo. This avoids littering the dictionary with single-use terms.

## Licence

You are allowed to use this work under a [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) licence. Just don’t be a gremlin and respect the work of others.
