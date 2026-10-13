# GenesFromVariantsSequenceVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chr** | **str** |  | 
**pos** | **float** |  | 
**rsid** | **List[str]** |  | [optional] 
**ref** | **str** |  | 
**alt** | **str** |  | 
**spdi** | **str** |  | [optional] 
**hgvs** | **str** |  | [optional] 
**ca_id** | **str** |  | [optional] 
**strain** | **List[str]** |  | [optional] 
**qual** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**annotations** | [**VariantAnnotations**](VariantAnnotations.md) |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**organism** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.genes_from_variants_sequence_variant import GenesFromVariantsSequenceVariant

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromVariantsSequenceVariant from a JSON string
genes_from_variants_sequence_variant_instance = GenesFromVariantsSequenceVariant.from_json(json)
# print the JSON string representation of the object
print(GenesFromVariantsSequenceVariant.to_json())

# convert the object into a dict
genes_from_variants_sequence_variant_dict = genes_from_variants_sequence_variant_instance.to_dict()
# create an instance of GenesFromVariantsSequenceVariant from a dict
genes_from_variants_sequence_variant_from_dict = GenesFromVariantsSequenceVariant.from_dict(genes_from_variants_sequence_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


