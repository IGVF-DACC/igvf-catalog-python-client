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
**files_filesets** | **str** |  | 
**crispr_modality** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**transcription_start_site** | **float** |  | [optional] 
**rna_pseudobulk_tpm** | **float** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**effect_size** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**t_score** | **float** |  | [optional] 
**idr** | **float** |  | [optional] 
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


