import torch
import torch.nn.functional as F
from torch_geometric.nn import GATConv
from elasticnet_fdr import run_elasticnet, compute_fdr
from data_loader import load_multiomics_data, align_samples

class GAT(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(GAT, self).__init__()
        self.gat = GATConv(in_channels, out_channels)

    def forward(self, x, edge_index):
        return F.elu(self.gat(x, edge_index))

def run_pipeline(transcriptomics_path, methylomics_path, proteomics_path, labels_path):
    omics = load_multiomics_data(transcriptomics_path, methylomics_path, proteomics_path)
    omics = align_samples(omics)
    labels = pd.read_csv(labels_path, index_col=0).loc[omics['transcriptomics'].index].values.ravel()

    # Placeholder: concatenate omics features
    X = pd.concat(omics.values(), axis=1).values
    y = labels

    # ElasticNet regression
    selected, coef = run_elasticnet(X, y)

    # Simulated p-values for demo
    import numpy as np
    p_values = np.random.uniform(0, 0.05, size=len(coef))
    rejected, q_values = compute_fdr(p_values)

    print("Selected features:", selected)
    print("FDR-controlled significant features:", np.where(rejected)[0])

if __name__ == "__main__":
    run_pipeline(
        transcriptomics_path="data/adni_transcriptomics.csv",
        methylomics_path="data/adni_methylomics.csv",
        proteomics_path="data/adni_proteomics.csv",
        labels_path="data/adni_labels.csv"
    )