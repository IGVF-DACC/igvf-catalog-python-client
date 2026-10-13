# Gene4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_name** | **str** |  | 
**gene_id** | **str** |  | 
**gene_start** | **float** |  | 
**gene_end** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.gene4 import Gene4

# TODO update the JSON string below
json = "{}"
# create an instance of Gene4 from a JSON string
gene4_instance = Gene4.from_json(json)
# print the JSON string representation of the object
print(Gene4.to_json())

# convert the object into a dict
gene4_dict = gene4_instance.to_dict()
# create an instance of Gene4 from a dict
gene4_from_dict = Gene4.from_dict(gene4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


