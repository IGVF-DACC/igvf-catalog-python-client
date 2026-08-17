# NearestGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nearest_coding_gene** | [**NearestGene**](NearestGene.md) |  | 
**nearest_gene** | [**NearestGene**](NearestGene.md) |  | 

## Example

```python
from igvf_catalog_client.models.nearest_genes import NearestGenes

# TODO update the JSON string below
json = "{}"
# create an instance of NearestGenes from a JSON string
nearest_genes_instance = NearestGenes.from_json(json)
# print the JSON string representation of the object
print(NearestGenes.to_json())

# convert the object into a dict
nearest_genes_dict = nearest_genes_instance.to_dict()
# create an instance of NearestGenes from a dict
nearest_genes_from_dict = NearestGenes.from_dict(nearest_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


