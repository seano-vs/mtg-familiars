My friends wanted to play a modified MTG commander format where all creatures were animals. An animal deck where you can only choose two animal types for creatures in your decks- and the animals have to exist IRL.

To account for the challenges a single commander has with its pool of similar creatures, we added an additional rule saying that all legendary creatures just had [Partner](https://mtg.fandom.com/wiki/Partner) slapped onto them. That way, the colors really opened things up to more creatures that you were allowed to use.

However, now I don't have as many resources for deck building as I normally do. And I am VERY VERY BAD at deck building. EDHRec and others now are significantly less helpful. So I made this notebook to help find good candidates with high synergy to pick as my two creature types.

Most likely, nobody else on the planet will ever use this. But I successfully procrastinated cleaning the house and did this instead. 

To use this, download the [all-cards scryfall bulk data](https://scryfall.com/docs/api/bulk-data) and create an `secret_constants.py` file with a gemini key `gemini_key` in it. 

What it looks like:

It gives output that looks a lil smthn like this.

- SYNERGY is how confident Gemini is that the two cards vibe withe ach other
- CARDS are the two cards that ahave chemistry
- ANIMALS are the legal IRL creature types between the two commanders
- COLORS are the combined color identities of the commanders. [The codes are covered here](https://scryfall.com/docs/api/colors)
- ANIMAL POOL is how many unique creatures that share a color and creature type with a commander. So, the max # of legal creatures for that deck

<table>
<thead>
<tr><th style="text-align: right;">  Synergy</th><th>Cards                                                    </th><th>Animals                 </th><th>Colors              </th><th>Card 1 Link                                                                                           </th><th>Card 2 Link                                                                                          </th><th>Animal Pool                           </th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;">       95</td><td>Snapdax, Apex of the Hunt & Nethroi, Apex of Death       </td><td>{'Cat'}                 </td><td>['G', 'R', 'B', 'W']</td><td><a href="https://scryfall.com/card/piko/209p/snapdax-apex-of-the-hunt?utm_source=api">CLICK_HERE</a>  </td><td><a href="https://scryfall.com/card/dmc/163/nethroi-apex-of-death?utm_source=api">CLICK_HERE</a>      </td><td>{'Cat': 325}                          </td></tr>
<tr><td style="text-align: right;">       90</td><td>Greasefang, Okiba Boss & Calamity, Galloping Inferno     </td><td>{'Rat', 'Horse'}        </td><td>['B', 'W', 'R']     </td><td><a href="https://scryfall.com/card/neo/485/greasefang-okiba-boss?utm_source=api">CLICK_HERE</a>       </td><td><a href="https://scryfall.com/card/otj/330/calamity-galloping-inferno?utm_source=api">CLICK_HERE</a> </td><td>{'Rat': 83, 'Horse': 26}              </td></tr>
<tr><td style="text-align: right;"></td></tr>
</tbody>
</table>