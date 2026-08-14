# GenomicElementsFromGenes200ResponseInnerGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_genes200_response_inner_genomic_element import GenomicElementsFromGenes200ResponseInnerGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromGenes200ResponseInnerGenomicElement from a JSON string
genomic_elements_from_genes200_response_inner_genomic_element_instance = GenomicElementsFromGenes200ResponseInnerGenomicElement.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromGenes200ResponseInnerGenomicElement.to_json())

# convert the object into a dict
genomic_elements_from_genes200_response_inner_genomic_element_dict = genomic_elements_from_genes200_response_inner_genomic_element_instance.to_dict()
# create an instance of GenomicElementsFromGenes200ResponseInnerGenomicElement from a dict
genomic_elements_from_genes200_response_inner_genomic_element_from_dict = GenomicElementsFromGenes200ResponseInnerGenomicElement.from_dict(genomic_elements_from_genes200_response_inner_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


