# ShouldaCite

ShouldaCite will help you answer the question: **"Should I cite this piece of
software in my academic work?"**

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
