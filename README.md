# EDNA Project

This repository contains the code and environment setup for an **eDNA (environmental DNA) analysis project**, focusing on data preprocessing, clustering, and exploratory analysis using Python and bioinformatics tools.

The goal is to provide a **reproducible, cross-platform setup** so all team members can run the same pipeline with minimal friction.

---

## Requirements

### Operating system

* **Linux** or **macOS**
* **Windows users must use WSL2 (Ubuntu)**

> Native Windows is not supported for some bioinformatics tools used in this project.

### Software

* Miniconda / Conda
* Git

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/edna-project.git
cd edna-project
```

---

### 2. Create the conda environment

```bash
conda env create -f environment.yml
```

---

### 3. Activate the environment

```bash
conda activate edna
```

---

### 4. Verify installation (optional)

```bash
python -c "import numpy, pandas, torch, hdbscan, umap"
fastp --version
vsearch --version
seqkit version
```

If these commands run without errors, the environment is set up correctly.

---

## Project Structure

```text
edna-project/
├── environment.yml      # Conda environment definition
├── README.md            # Project documentation
├── data/                # Raw input data (ignored by Git)
├── scripts/             # Analysis and preprocessing scripts
├── outputs/             # Generated results (ignored by Git)
└── notebooks/           # Exploratory notebooks
```

> **Important:**
> Raw sequencing data and generated outputs are **not tracked** in Git.

---

## Notes for Windows Users

* Install **WSL2 with Ubuntu**
* Run all commands inside the Ubuntu terminal
* Use VS Code with the **Remote – WSL** extension (recommended)

---

## Contributing

* Commit small, logical changes
* Do not commit raw data or large output files
* If you add a new dependency:

  1. Install it in the `edna` environment
  2. Re-export `environment.yml`
  3. Commit the updated file

---

## License

This project is licensed under the **MIT License**.
