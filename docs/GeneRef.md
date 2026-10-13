# GeneRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**chr** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.gene_ref import GeneRef

# TODO update the JSON string below
json = "{}"
# create an instance of GeneRef from a JSON string
gene_ref_instance = GeneRef.from_json(json)
# print the JSON string representation of the object
print(GeneRef.to_json())

# convert the object into a dict
gene_ref_dict = gene_ref_instance.to_dict()
# create an instance of GeneRef from a dict
gene_ref_from_dict = GeneRef.from_dict(gene_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


