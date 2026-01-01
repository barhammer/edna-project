# EDNA Project

This repository contains the code and environment setup for an **eDNA (environmental DNA) analysis project**, covering **raw sequencing preprocessing**, **clustering**, and **downstream exploratory analysis**.

The goal is to provide a **reproducible, low-friction workflow** so all team members can run the same pipeline reliably, even if they work on different stages of the project.

---

## Overview

The project is intentionally split into **two stages**, each with its own Conda environment:

1. **Preprocessing stage**
   Raw FASTQ → QC → trimmed reads / ASVs / OTUs
2. **Analysis stage**
   Feature tables → clustering → visualization / ML

Not every user needs to run both stages.

---

## Requirements

### Operating System

* **Linux** or **macOS**
* **Windows users must use WSL2 (Ubuntu)**

> Native Windows is not supported for several bioinformatics tools used here.

### Software

* **Git**
* **Miniconda / Conda**

---

## Repository Structure

```
edna-project/
├── preprocess.yml        # Conda env for FASTQ preprocessing (FastQC, fastp, vsearch, DADA2)
├── environment.yml       # Conda env for analysis & ML
├── data/                 # Data directory (raw + intermediate data; not tracked)
│   ├── raw_fastq/        # Raw FASTQ files (user-provided)
│   ├── trimmed/          # Trimmed FASTQs (generated)
│   └── qc/               # QC reports (generated)
├── scripts/              # Pipeline and analysis scripts
├── README.md
└── LICENSE
```

> **Important:** Raw sequencing data and generated outputs are intentionally **not tracked in Git**.

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/barhammer/edna-project.git
cd edna-project
```

---

## Environment Setup (Important)

This project uses **two Conda environments**.
You only need to install the environment relevant to the stage you are running.

---

## Environment 1: Preprocessing (FASTQ → cleaned reads)

### Who needs this?

* Anyone starting from **raw sequencing data (FASTQ)**
* Anyone running **FastQC, fastp, vsearch, or DADA2**

### Create the preprocessing environment

```bash
conda env create -f preprocess.yml
```

### Activate it

```bash
conda activate prepro
```

### (Optional) Verify installation

```bash
fastqc --version
fastp --version
vsearch --version
R -q -e "library(dada2)"
```

---

## Environment 2: Analysis & Clustering

### Who needs this?

* Anyone working from **feature tables / abundance matrices**
* Anyone doing **clustering, visualization, or ML**

### Create the analysis environment

```bash
conda env create -f environment.yml
```

### Activate it

```bash
conda activate edna
```

### (Optional) Verify installation

```bash
python -c "import numpy, pandas, sklearn, umap, hdbscan"
```

---

## Data Input Convention

Users should place their raw paired-end FASTQ files here:

```
data/raw_fastq/
├── sample_1.fastq.gz
├── sample_2.fastq.gz
```

Downstream outputs will be written automatically to:

* `data/qc/`
* `data/trimmed/`
* (later) feature tables / clustering outputs

---

## Notes for Windows Users

* Install **WSL2 with Ubuntu**
* Run **all commands inside the Ubuntu terminal**
* VS Code with the **Remote – WSL** extension is strongly recommended

---

## Dependency Management (Very Important)

* **All dependencies must be declared** in the appropriate YAML file
* Do **not** install packages manually using `pip install` or `conda install`
* Do **not** run `conda env export`

If a new dependency is required:

1. Discuss it with the team
2. Add it explicitly to the correct YAML file
3. Recreate the environment
4. Commit the updated YAML file

This ensures everyone stays on the same, stable setup.

---

## Contributing Guidelines

* Commit small, logical changes
* Never commit raw sequencing data or large output files
* Keep exploratory work in notebooks
* Move finalized logic into scripts

---

## License

This project is licensed under the **MIT License**.
