# TargetGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_name** | **str** |  | 
**id** | **str** |  | 
**chr** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.target_gene import TargetGene

# TODO update the JSON string below
json = "{}"
# create an instance of TargetGene from a JSON string
target_gene_instance = TargetGene.from_json(json)
# print the JSON string representation of the object
print(TargetGene.to_json())

# convert the object into a dict
target_gene_dict = target_gene_instance.to_dict()
# create an instance of TargetGene from a dict
target_gene_from_dict = TargetGene.from_dict(target_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


