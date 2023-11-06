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