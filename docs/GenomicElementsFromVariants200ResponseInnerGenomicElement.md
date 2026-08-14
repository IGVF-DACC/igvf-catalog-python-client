# GenomicElementsFromVariants200ResponseInnerGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**type** | **str** |  | 
**source_annotation** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_variants200_response_inner_genomic_element import GenomicElementsFromVariants200ResponseInnerGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromVariants200ResponseInnerGenomicElement from a JSON string
genomic_elements_from_variants200_response_inner_genomic_element_instance = GenomicElementsFromVariants200ResponseInnerGenomicElement.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromVariants200ResponseInnerGenomicElement.to_json())

# convert the object into a dict
genomic_elements_from_variants200_response_inner_genomic_element_dict = genomic_elements_from_variants200_response_inner_genomic_element_instance.to_dict()
# create an instance of GenomicElementsFromVariants200ResponseInnerGenomicElement from a dict
genomic_elements_from_variants200_response_inner_genomic_element_from_dict = GenomicElementsFromVariants200ResponseInnerGenomicElement.from_dict(genomic_elements_from_variants200_response_inner_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


