# DiseaseFromVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_variant** | [**DiseaseFromVariantsSequenceVariant**](DiseaseFromVariantsSequenceVariant.md) |  | [optional] 
**disease** | [**BiosamplesFromGenomicElementsBiosample**](BiosamplesFromGenomicElementsBiosample.md) |  | [optional] 
**gene_id** | **str** |  | [optional] 
**gene_name** | **str** |  | [optional] 
**assertion** | **str** |  | [optional] 
**pmids** | **List[str]** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.disease_from_variants import DiseaseFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of DiseaseFromVariants from a JSON string
disease_from_variants_instance = DiseaseFromVariants.from_json(json)
# print the JSON string representation of the object
print(DiseaseFromVariants.to_json())

# convert the object into a dict
disease_from_variants_dict = disease_from_variants_instance.to_dict()
# create an instance of DiseaseFromVariants from a dict
disease_from_variants_from_dict = DiseaseFromVariants.from_dict(disease_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


