# test for utf8 encoding

The section [about_py.md](quantecon_flat/mini_book/docs/about_py.md) has
several unicode characters that will raise an exception if the read/write for
input, cache and output is not encoded in utf-8

The github action prouduces the rendered html at

https://phaustin.github.io/jb_windows_test/flat_test/about_py.html#testing-greek-characters

to run:

```
conda env create -f environment.yml
conda activate buildit
```

then:

```
cd quantecon_flat/mini_book
jupyter-build build docs
```

which produces the rendered html file at `docs_build/html/index.html`
