# Phenotype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phenotype_id** | **str** |  | 
**phenotype_name** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.phenotype import Phenotype

# TODO update the JSON string below
json = "{}"
# create an instance of Phenotype from a JSON string
phenotype_instance = Phenotype.from_json(json)
# print the JSON string representation of the object
print(Phenotype.to_json())

# convert the object into a dict
phenotype_dict = phenotype_instance.to_dict()
# create an instance of Phenotype from a dict
phenotype_from_dict = Phenotype.from_dict(phenotype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


