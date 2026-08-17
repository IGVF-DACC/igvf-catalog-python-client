# BiosamplesFromGenomicElementsGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | [optional] 
**name** | **str** |  | 
**method** | **str** |  | [optional] 
**source_annotation** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.biosamples_from_genomic_elements_genomic_element import BiosamplesFromGenomicElementsGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromGenomicElementsGenomicElement from a JSON string
biosamples_from_genomic_elements_genomic_element_instance = BiosamplesFromGenomicElementsGenomicElement.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromGenomicElementsGenomicElement.to_json())

# convert the object into a dict
biosamples_from_genomic_elements_genomic_element_dict = biosamples_from_genomic_elements_genomic_element_instance.to_dict()
# create an instance of BiosamplesFromGenomicElementsGenomicElement from a dict
biosamples_from_genomic_elements_genomic_element_from_dict = BiosamplesFromGenomicElementsGenomicElement.from_dict(biosamples_from_genomic_elements_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


