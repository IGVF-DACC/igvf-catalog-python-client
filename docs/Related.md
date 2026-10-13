# Related


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**RelatedGene**](RelatedGene.md) |  | [optional] 
**protein** | [**ProteinCompact**](ProteinCompact.md) |  | [optional] 
**sources** | [**RelatedSources**](RelatedSources.md) |  | 

## Example

```python
from igvf_catalog_client.models.related import Related

# TODO update the JSON string below
json = "{}"
# create an instance of Related from a JSON string
related_instance = Related.from_json(json)
# print the JSON string representation of the object
print(Related.to_json())

# convert the object into a dict
related_dict = related_instance.to_dict()
# create an instance of Related from a dict
related_from_dict = Related.from_dict(related_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


