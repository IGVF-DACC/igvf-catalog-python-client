# GenesFromGenomicElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**biosample_term** | **str** |  | [optional] 
**cell_annotation** | **str** |  | [optional] 
**cell_annotation_term** | **str** |  | [optional] 
**treatments_term_ids** | **List[str]** |  | [optional] 
**files_filesets** | **str** |  | 
**perturbation** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**transcription_start_site** | **float** |  | [optional] 
**rna_pseudobulk_tpm** | **float** |  | [optional] 
**negative_selection_log2_fc** | **float** |  | [optional] 
**negative_selection_p_value** | **float** |  | [optional] 
**negative_selection_p_value_adj** | **float** |  | [optional] 
**negative_selection_neg_log10_pvalue** | **float** |  | [optional] 
**negative_selection_neg_log10_pvalue_adj** | **float** |  | [optional] 
**negative_selection_significant** | **bool** |  | [optional] 
**positive_selection_log2_fc** | **float** |  | [optional] 
**positive_selection_p_value** | **float** |  | [optional] 
**positive_selection_p_value_adj** | **float** |  | [optional] 
**positive_selection_neg_log10_pvalue** | **float** |  | [optional] 
**positive_selection_neg_log10_pvalue_adj** | **float** |  | [optional] 
**positive_selection_significant** | **bool** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**log2_fc_ci95_lower** | **float** |  | [optional] 
**log2_fc_ci95_upper** | **float** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**effect_size_ci_95** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**t_score** | **float** |  | [optional] 
**idr** | **float** |  | [optional] 
**pct_1** | **float** |  | [optional] 
**pct_2** | **float** |  | [optional] 
**num_guides** | **float** |  | [optional] 
**num_cells** | **float** |  | [optional] 
**fold_change** | **float** |  | [optional] 
**background_corrected_fold_change** | **float** |  | [optional] 
**cpm_perturb** | **float** |  | [optional] 
**cpm_bg** | **float** |  | [optional] 
**gamma_approximation_ln_p_value** | **float** |  | [optional] 
**hypergeometric_ln_p_value** | **float** |  | [optional] 
**empirical_p_value** | **float** |  | [optional] 
**p_value** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**p_value_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**neg_log10_pvalue** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**neg_log10_pvalue_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**significant** | **bool** |  | [optional] 
**genomic_element** | [**GenesFromGenomicElementsGenomicElement**](GenesFromGenomicElementsGenomicElement.md) |  | 
**gene** | [**GenesFromGenomicElementsGene**](GenesFromGenomicElementsGene.md) |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_genomic_elements import GenesFromGenomicElements

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromGenomicElements from a JSON string
genes_from_genomic_elements_instance = GenesFromGenomicElements.from_json(json)
# print the JSON string representation of the object
print(GenesFromGenomicElements.to_json())

# convert the object into a dict
genes_from_genomic_elements_dict = genes_from_genomic_elements_instance.to_dict()
# create an instance of GenesFromGenomicElements from a dict
genes_from_genomic_elements_from_dict = GenesFromGenomicElements.from_dict(genes_from_genomic_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


