# VariantsGenomicElementsGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**VariantBasic**](VariantBasic.md) |  | 
**distance_to_tss** | **float** |  | [optional] 
**genomic_element** | [**GenomicElement8**](GenomicElement8.md) |  | 
**gene** | [**Gene6**](Gene6.md) |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**files_filesets** | **str** |  | 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**crispr_modality** | **str** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**p_value** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**p_value_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**effect_size** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variants_genomic_elements_genes import VariantsGenomicElementsGenes

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsGenomicElementsGenes from a JSON string
variants_genomic_elements_genes_instance = VariantsGenomicElementsGenes.from_json(json)
# print the JSON string representation of the object
print(VariantsGenomicElementsGenes.to_json())

# convert the object into a dict
variants_genomic_elements_genes_dict = variants_genomic_elements_genes_instance.to_dict()
# create an instance of VariantsGenomicElementsGenes from a dict
variants_genomic_elements_genes_from_dict = VariantsGenomicElementsGenes.from_dict(variants_genomic_elements_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


