# DiseaseFromVariantsSequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chr** | **str** |  | 
**pos** | **float** |  | 
**ref** | **str** |  | 
**alt** | **str** |  | 
**rsid** | **List[str]** |  | [optional] 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.disease_from_variants_sequence_variant import DiseaseFromVariantsSequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of DiseaseFromVariantsSequenceVariant from a JSON string
disease_from_variants_sequence_variant_instance = DiseaseFromVariantsSequenceVariant.from_json(json)
# print the JSON string representation of the object
print(DiseaseFromVariantsSequenceVariant.to_json())

# convert the object into a dict
disease_from_variants_sequence_variant_dict = disease_from_variants_sequence_variant_instance.to_dict()
# create an instance of DiseaseFromVariantsSequenceVariant from a dict
disease_from_variants_sequence_variant_from_dict = DiseaseFromVariantsSequenceVariant.from_dict(disease_from_variants_sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


