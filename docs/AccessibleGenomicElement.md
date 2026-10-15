# AccessibleGenomicElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**type** | **str** |  | [optional] 
**source_annotation** | **str** |  | [optional] 
**promoter_of** | [**AccessibleGenomicElementPromoterOf**](AccessibleGenomicElementPromoterOf.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.accessible_genomic_element import AccessibleGenomicElement

# TODO update the JSON string below
json = "{}"
# create an instance of AccessibleGenomicElement from a JSON string
accessible_genomic_element_instance = AccessibleGenomicElement.from_json(json)
# print the JSON string representation of the object
print(AccessibleGenomicElement.to_json())

# convert the object into a dict
accessible_genomic_element_dict = accessible_genomic_element_instance.to_dict()
# create an instance of AccessibleGenomicElement from a dict
accessible_genomic_element_from_dict = AccessibleGenomicElement.from_dict(accessible_genomic_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


