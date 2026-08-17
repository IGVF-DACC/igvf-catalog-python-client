# GenomicElementBasic


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
from igvf_catalog_client.models.genomic_element_basic import GenomicElementBasic

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementBasic from a JSON string
genomic_element_basic_instance = GenomicElementBasic.from_json(json)
# print the JSON string representation of the object
print(GenomicElementBasic.to_json())

# convert the object into a dict
genomic_element_basic_dict = genomic_element_basic_instance.to_dict()
# create an instance of GenomicElementBasic from a dict
genomic_element_basic_from_dict = GenomicElementBasic.from_dict(genomic_element_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


