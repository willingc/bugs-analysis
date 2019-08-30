# bug-analysis

This is different methods for exploring data from bugs.python.org

## Datasette approach

Install:

```
pip install csvs-to-sqlite
pip install datasette
```

Convert csv to sqlite:

```
csvs-to-sqlite -s ',' ../org-python/bug-analysis/2019-08-27-bpo.csv bugs.db
```

Run:

```
datasette bugs.db
```

## Notebooks and pandas

Use `environment.yml` to create a conda environment.

Use pandas `df.read_csv`.
