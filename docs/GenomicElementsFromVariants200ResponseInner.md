# GenomicElementsFromVariants200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**ProteinsFromVariants200ResponseInnerSequenceVariantAnyOf**](ProteinsFromVariants200ResponseInnerSequenceVariantAnyOf.md) |  | 
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
**genomic_element** | [**GenomicElementsFromVariants200ResponseInnerGenomicElement**](GenomicElementsFromVariants200ResponseInnerGenomicElement.md) |  | [optional] 

## Example

```python
from igvf_catalog_client.models.genomic_elements_from_variants200_response_inner import GenomicElementsFromVariants200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenomicElementsFromVariants200ResponseInner from a JSON string
genomic_elements_from_variants200_response_inner_instance = GenomicElementsFromVariants200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GenomicElementsFromVariants200ResponseInner.to_json())

# convert the object into a dict
genomic_elements_from_variants200_response_inner_dict = genomic_elements_from_variants200_response_inner_instance.to_dict()
# create an instance of GenomicElementsFromVariants200ResponseInner from a dict
genomic_elements_from_variants200_response_inner_from_dict = GenomicElementsFromVariants200ResponseInner.from_dict(genomic_elements_from_variants200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


