# GenomicElementsFromGenomicElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perturbed_genomic_element** | [**GenomicElementsFromGenomicElementsPerturbedGenomicElement**](GenomicElementsFromGenomicElementsPerturbedGenomicElement.md) |  | 
**accessible_genomic_element** | [**GenomicElementsFromGenomicElementsPerturbedGenomicElement**](GenomicElementsFromGenomicElementsPerturbedGenomicElement.md) |  | 
**name** | **str** |  | 
**inverse_name** | **str** |  | 
**label** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**files_filesets** | **str** |  | 
**biological_context** | **str** |  | [optional] 
**biosample_term** | **str** |  | [optional] 
**treatments_term_ids** | **List[str]** |  | [optional] 
**crispr_modality** | **str** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**p_value_adj** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_genomic_elements import GenomicElementsFromGenomicElements

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromGenomicElements from a JSON string
genomic_elements_from_genomic_elements_instance = GenomicElementsFromGenomicElements.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromGenomicElements.to_json())

# convert the object into a dict
genomic_elements_from_genomic_elements_dict = genomic_elements_from_genomic_elements_instance.to_dict()
# create an instance of GenomicElementsFromGenomicElements from a dict
genomic_elements_from_genomic_elements_from_dict = GenomicElementsFromGenomicElements.from_dict(genomic_elements_from_genomic_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


