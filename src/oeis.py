"""OEIS lookup for novelty checks.

Usage:
    python3 src/oeis.py "1,3,7,19,51"
    python3 src/oeis.py "taxicab"
"""
import json
import sys
import urllib.parse
import urllib.request


def search(query, limit=10):
    url = "https://oeis.org/search?" + urllib.parse.urlencode({"q": query, "fmt": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": "answer-first/0.1 (research script)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    # OEIS returns either a list or {"results": [...]}, depending on API version.
    results = data.get("results") if isinstance(data, dict) else data
    return (results or [])[:limit]


def main():
    query = " ".join(sys.argv[1:])
    if not query:
        sys.exit(__doc__)
    hits = search(query)
    if not hits:
        print(f"OEIS: no results for {query!r}")
        return
    for h in hits:
        print(f"A{h['number']:06d}  {h['name']}")
        print(f"         {h['data'][:100]}")


if __name__ == "__main__":
    main()
