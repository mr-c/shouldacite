# ShouldaCite

[![DOI](https://zenodo.org/badge/54544657.svg)](https://zenodo.org/badge/latestdoi/54544657)

You are writing up your research and wonder if you should cite a particular software package that you used.

[Should you cite this particular piece of software?](should-I-cite-this-software.md)

http://bit.ly/shouldacite

# Web page

* To generate a webpage you need to install `flask`, `markdown`, `frozen-flask`
and `ghp-import`. You can use Conda to get everything needed:

    ```bash
    conda env create -f app/environment.yml
    source activate shouldicite
    ```

* To serve the app type:

    ```bash
    make serve
    ```

    and point your browser to http://0.0.0.0:5000.

* To genearet a static HTML version type:

    ```bash
    make html
    ```

* And finally to publish the content on github pages type:

    ```bash
    make publish
    ```

# License

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
