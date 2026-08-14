# BiosamplesFromVariants200ResponseInnerGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**chr** | **str** |  | [optional] 
**start** | **float** |  | [optional] 
**end** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**source_annotation** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.biosamples_from_variants200_response_inner_genomic_element import BiosamplesFromVariants200ResponseInnerGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromVariants200ResponseInnerGenomicElement from a JSON string
biosamples_from_variants200_response_inner_genomic_element_instance = BiosamplesFromVariants200ResponseInnerGenomicElement.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromVariants200ResponseInnerGenomicElement.to_json())

# convert the object into a dict
biosamples_from_variants200_response_inner_genomic_element_dict = biosamples_from_variants200_response_inner_genomic_element_instance.to_dict()
# create an instance of BiosamplesFromVariants200ResponseInnerGenomicElement from a dict
biosamples_from_variants200_response_inner_genomic_element_from_dict = BiosamplesFromVariants200ResponseInnerGenomicElement.from_dict(biosamples_from_variants200_response_inner_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


