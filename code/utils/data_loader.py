import pandas as pd

def load_multiomics_data(transcriptomics_path, methylomics_path, proteomics_path):
    transcriptomics = pd.read_csv(transcriptomics_path, index_col=0)
    methylomics = pd.read_csv(methylomics_path, index_col=0)
    proteomics = pd.read_csv(proteomics_path, index_col=0)

    return {
        'transcriptomics': transcriptomics,
        'methylomics': methylomics,
        'proteomics': proteomics
    }

def align_samples(omics_dict):
    common_samples = set.intersection(*[set(df.index) for df in omics_dict.values()])
    aligned = {k: df.loc[common_samples] for k, df in omics_dict.items()}
    return aligned