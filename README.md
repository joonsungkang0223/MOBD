# 🧠 Graph-Based Multi-Omics Framework for Alzheimer's Biomarker Discovery

This repository contains the manuscript, supplementary materials, and source code for our unified framework that integrates Graph Attention Networks (GAT), Multi-Omics Variational Embedding (MOVE), ElasticNet regression, and Storey's False Discovery Rate (FDR) control. The framework is designed for high-dimensional, low-sample size (HDLSS) multi-omics data and has been validated across synthetic, ADNI, and ROSMAP cohorts.

---

## 📌 Highlights

- 🔗 Graph-based modeling of gene-gene interactions
- 🧬 Variational manifold encoding across omics layers
- 📉 Sparse regression for biomarker selection
- ✅ Statistical rigor via FDR control
- 🧠 Discovery of canonical and novel biomarkers (e.g., TREM2–PLCG2, MAPT–GRN)

---

## 📁 Repository Structure

---

## 🚀 Getting Started

### Requirements
- Python ≥ 3.8
- PyTorch ≥ 1.10
- NumPy, Pandas, Scikit-learn
- NetworkX, Matplotlib

### Installation
```bash
git clone https://github.com/your-username/alzheimer-multiomics-framework.git
cd alzheimer-multiomics-framework
pip install -r requirements.txt

python code/gat_move_pipeline.py --input data/adni_processed.csv