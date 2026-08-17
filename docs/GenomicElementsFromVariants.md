# GenomicElementsFromVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**VariantBasic**](VariantBasic.md) |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**beta** | **float** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**biological_context** | **str** |  | [optional] 
**biosample_term** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**genomic_element** | [**GenomicElement9**](GenomicElement9.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_variants import GenomicElementsFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromVariants from a JSON string
genomic_elements_from_variants_instance = GenomicElementsFromVariants.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromVariants.to_json())

# convert the object into a dict
genomic_elements_from_variants_dict = genomic_elements_from_variants_instance.to_dict()
# create an instance of GenomicElementsFromVariants from a dict
genomic_elements_from_variants_from_dict = GenomicElementsFromVariants.from_dict(genomic_elements_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


