# NearestGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_name** | **str** |  | [optional] 
**id** | **str** |  | 
**start** | **float** |  | 
**end** | **float** |  | 
**distance** | **float** |  | 

## Example

```python
from igvf_catalog_client.models.nearest_gene import NearestGene

# TODO update the JSON string below
json = "{}"
# create an instance of NearestGene from a JSON string
nearest_gene_instance = NearestGene.from_json(json)
# print the JSON string representation of the object
print(NearestGene.to_json())

# convert the object into a dict
nearest_gene_dict = nearest_gene_instance.to_dict()
# create an instance of NearestGene from a dict
nearest_gene_from_dict = NearestGene.from_dict(nearest_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


