# PhenotypesFromGenomicElements200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**files_filesets** | **str** |  | 
**crispr_modality** | **str** |  | [optional] 
**z_score** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**num_guides** | **float** |  | [optional] 
**num_guides_hit** | **float** |  | [optional] 
**num_guides_nonhit** | **float** |  | [optional] 
**fraction_guides_hit** | **float** |  | [optional] 
**phenotype_name** | **str** |  | [optional] 
**genomic_element** | [**GenomicElementsFromGenes200ResponseInnerGenomicElement**](GenomicElementsFromGenes200ResponseInnerGenomicElement.md) |  | 
**phenotype** | [**PhenotypesFromGenomicElements200ResponseInnerPhenotype**](PhenotypesFromGenomicElements200ResponseInnerPhenotype.md) |  | 

## Example

```python
from igvf_catalog_client.models.phenotypes_from_genomic_elements200_response_inner import PhenotypesFromGenomicElements200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypesFromGenomicElements200ResponseInner from a JSON string
phenotypes_from_genomic_elements200_response_inner_instance = PhenotypesFromGenomicElements200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(PhenotypesFromGenomicElements200ResponseInner.to_json())

# convert the object into a dict
phenotypes_from_genomic_elements200_response_inner_dict = phenotypes_from_genomic_elements200_response_inner_instance.to_dict()
# create an instance of PhenotypesFromGenomicElements200ResponseInner from a dict
phenotypes_from_genomic_elements200_response_inner_from_dict = PhenotypesFromGenomicElements200ResponseInner.from_dict(phenotypes_from_genomic_elements200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


