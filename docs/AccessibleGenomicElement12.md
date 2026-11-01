# AccessibleGenomicElement12


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**strand** | **str** |  | [optional] 
**name** | **str** |  | 
**aliases** | **List[str]** |  | [optional] 
**method** | **str** |  | [optional] 
**source_annotation** | **str** |  | 
**type** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.accessible_genomic_element12 import AccessibleGenomicElement12

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleGenomicElement12 from a JSON string
accessible_genomic_element12_instance = AccessibleGenomicElement12.from_json(json)
# print the JSON string representation of the object
print(AccessibleGenomicElement12.to_json())

# convert the object into a dict
accessible_genomic_element12_dict = accessible_genomic_element12_instance.to_dict()
# create an instance of AccessibleGenomicElement12 from a dict
accessible_genomic_element12_from_dict = AccessibleGenomicElement12.from_dict(accessible_genomic_element12_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


