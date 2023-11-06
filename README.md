# Test snakemake cli

Aim: have snakemake workflows run through a packaged executable through a template like

```python
import os
import snakemake

workflow_path = f"{os.path.dirname(os.path.abspath(__file__))}"

def run_snakemake_workflow(snakefile: str = f"{workflow_path}/workflows/w1.smk",
                           targets=None, dryrun=False):
    print(f"module path: {workflow_path}")
    snakemake.snakemake(
        snakefile,
        targets=targets,
        dryrun=dryrun
    )

if __name__ == "__main__":
    run_snakemake_workflow(
        snakefile=f"{workflow_path}/workflows/w1.smk"
    )
```

## Bioconda

Basically you need to make a pull request to bioconda, but you could/should test your package locally first.

References: 
- https://docs.conda.io/projects/conda-build/en/stable/concepts/recipe.html
- https://bioconda.github.io/contributor/setup.html#
- https://bioconda.github.io/contributor/building-locally.html

To test locally, we need to build bioconda-utils env, with mamba.

Might use conda skeleton? Looks like it's only for pypi or others

## Poetry

### TL;DR

```bash
# build the package
poetry build # Idk what's wrong with test-pypi token

# create venv
# will create ~/.cache/pypoetry/virtualenvs/test-cli-dk-ovnLU1uv-py3.9/bin/activate
poetry install

```

### Test

```bash
# activate venv
poetry shell

# test within repo with data folder
wf1 # as defined in pyproject.toml

# test if it works anywhere
# a dir with a data folder
# same as data folder in repo
cd ~/developing/temb
wf1
```
