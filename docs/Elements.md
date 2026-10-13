# Elements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**cell_type** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**model** | **str** |  | [optional] 
**dataset** | **str** |  | [optional] 
**element_type** | **str** |  | [optional] 
**element_chr** | **str** |  | [optional] 
**element_start** | **float** |  | [optional] 
**element_end** | **float** |  | [optional] 
**name** | **str** |  | 
**method** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.elements import Elements

# TODO update the JSON string below
json = "{}"
# create an instance of Elements from a JSON string
elements_instance = Elements.from_json(json)
# print the JSON string representation of the object
print(Elements.to_json())

# convert the object into a dict
elements_dict = elements_instance.to_dict()
# create an instance of Elements from a dict
elements_from_dict = Elements.from_dict(elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


