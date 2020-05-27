# {{@@ env['dotdrop_warning'] @@}}
# flake8: noqa: E266

from urllib.parse import urlencode


c = c  # noqa
config = config  # noqa


def get_ddg():
    ddg_config = {
        "k1": "-1",
        "k7": "111111",
        "k8":"b8b8b8",
        "k9":"b8b8b8",
        "ka": "Fira Code",
        "kae": "d",
        "kah": "ch-de",
        "kaj": "m",
        "kak": "-1",
        "kal": "-1",
        "kam": "osm",
        "kao": "-1",
        "kap": "-1",
        "kaq": "-1",
        "kau": "-1",
        "kav": "1",
        "kax": "-1",
        "kg": "g",
        "kk": "-1",
        "kp": "-2",
        "kt": "Fira Sans",
        "ku": "1",
        "kx":"c6c6c6",
    }
    return f"https://start.duckduckgo.com/?q={{}}&{urlencode(ddg_config)}"


ddg = get_ddg()

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
ENGINES = {'DEFAULT': ddg,
           'a': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
           'aur': 'https://aur.archlinux.org/packages/?O=0&K={}',
           'cc': 'https://www.dict.cc/?s={}',
           'ddg': ddg,
           'deepl': "https://www.deepl.com/en/translator#{}",  # Expects a string like `en/de/something`
           'g': 'https://www.google.com/search?q={}',
           'gh': 'https://github.com/search?utf8=%E2%9C%93&q={}&type=',
           'w': 'https://en.wikipedia.org/wiki/{}',
           'wd': 'https://de.wikipedia.org/w/index.php?title=Spezial:Suche&search={}',
           'yt': 'https://www.youtube.com/results?search_query={}'}

# Add some searchengines from dotdrop .env-file
ENGINES.update({{@@ env['qutebrowser_search_engines'] @@}})

c.url.searchengines = ENGINES
