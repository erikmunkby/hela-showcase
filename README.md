# hela-showcase
Repository showcasing the hela python data catalog package. Browse this fictional online beer store
[data catalog](https://erikmunkby.github.io/hela-showcase/)

More links:
* Find `hela` on [PyPI](https://pypi.org/project/hela/)
* Find `hela` on [GitHub](https://github.com/erikmunkby/hela)
* `hela` [docs](https://erikmunkby.github.io/hela/)


## Beer Catalog
Within this repository you can find the code for the beer catalog built using the `hela` package.

### Folder structure
The catalog is built in the following folder structure:

```
beer_catalog/
├── rich_descriptions/
│   ├── beer_info.md
│   └── ...
├── datasets/
│   ├── sales/
│   │   ├── beer_info.py
│   │   └── orders.py
│   └── web/
│       ├── beer_reviews.py
│       └── orders.py
├── beer_catalog.py
└── column_store.py
```

### Important files/scripts
* `generate_web_app.py` is generating the `index.html` file used to build the web app.
* `.github/workflows/github_pages.yaml` is the automated github action triggering the script above and committing to GH pages branch.