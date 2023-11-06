SAMPLES = ["A", "B"]


rule all:
    input:
        expand("results/{sample}_w1.txt", sample=SAMPLES) 


rule bwa_map:
    input:
        "data/{sample}_input.txt",
    output:
        "results/{sample}_w1.txt"
    shell:
        "touch {output}"