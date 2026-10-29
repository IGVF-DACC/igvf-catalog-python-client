# AccessibleGenomicElement11


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
**id** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.accessible_genomic_element11 import AccessibleGenomicElement11

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleGenomicElement11 from a JSON string
accessible_genomic_element11_instance = AccessibleGenomicElement11.from_json(json)
# print the JSON string representation of the object
print(AccessibleGenomicElement11.to_json())

# convert the object into a dict
accessible_genomic_element11_dict = accessible_genomic_element11_instance.to_dict()
# create an instance of AccessibleGenomicElement11 from a dict
accessible_genomic_element11_from_dict = AccessibleGenomicElement11.from_dict(accessible_genomic_element11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


