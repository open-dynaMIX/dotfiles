# This file is managed by dotdrop, only edit it in your dotdrop files!
# flake8: noqa: E266


c = c  # noqa
config = config  # noqa

## Definitions of search engines which can be used via the address bar.
## Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
## `{}` placeholder. The placeholder will be replaced by the search term,
## use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
## `DEFAULT` is used when `url.auto_search` is turned on and something
## else than a URL was entered to be opened. Other search engines can be
## used by prepending the search engine name to the search term, e.g.
## `:open google qutebrowser`.
## Type: Dict
# c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}
ENGINES = {'DEFAULT': 'https://www.google.ch/search?q={}',
           'a': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
           'aur': 'https://aur.archlinux.org/packages/?O=0&K={}',
           'cc': 'https://www.dict.cc/?s={}',
           'ddg': 'https://start.duckduckgo.com/?q={}&kae=d&kak=-1&kal=-1&kao=-1&kaq=-1&kl=ch-de&kp=-2&k1=-1&kk=-1&kaj=m&kam=osm&kax=-1&kap=-1&ia=web',
           'gh': 'https://github.com/search?utf8=%E2%9C%93&q={}&type=',
           'w': 'https://en.wikipedia.org/wiki/{}',
           'wd': 'https://de.wikipedia.org/w/index.php?title=Spezial:Suche&search={}',
           'yt': 'https://www.youtube.com/results?search_query={}'}
# Add some searchengines from dotdrop .env-file
for engine in "{{@@ env['qutebrowser_search_engines'] @@}}".split('&SPLOT&'):
    if engine:
        ENGINES[engine.split('&SPLIT&')[0]] = engine.split('&SPLIT&')[1]
c.url.searchengines = ENGINES
