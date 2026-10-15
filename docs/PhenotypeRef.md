# PhenotypeRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phenotype_id** | **str** |  | 
**phenotype_name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.phenotype_ref import PhenotypeRef

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypeRef from a JSON string
phenotype_ref_instance = PhenotypeRef.from_json(json)
# print the JSON string representation of the object
print(PhenotypeRef.to_json())

# convert the object into a dict
phenotype_ref_dict = phenotype_ref_instance.to_dict()
# create an instance of PhenotypeRef from a dict
phenotype_ref_from_dict = PhenotypeRef.from_dict(phenotype_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


