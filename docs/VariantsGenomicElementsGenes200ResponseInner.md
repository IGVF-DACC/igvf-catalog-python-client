# VariantsGenomicElementsGenes200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**ProteinsFromVariants200ResponseInnerSequenceVariantAnyOf**](ProteinsFromVariants200ResponseInnerSequenceVariantAnyOf.md) |  | 
**distance_to_tss** | **float** |  | [optional] 
**genomic_element** | [**VariantsGenomicElementsGenes200ResponseInnerGenomicElement**](VariantsGenomicElementsGenes200ResponseInnerGenomicElement.md) |  | 
**gene** | [**VariantsGenomicElementsGenes200ResponseInnerGene**](VariantsGenomicElementsGenes200ResponseInnerGene.md) |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**files_filesets** | **str** |  | 
**biological_context** | **str** |  | 
**biosample_term** | **str** |  | 
**crispr_modality** | **str** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**p_value** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**p_value_adj** | [**GenesFromVariants200ResponseInnerNegLog10Pvalue**](GenesFromVariants200ResponseInnerNegLog10Pvalue.md) |  | [optional] 
**effect_size** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.variants_genomic_elements_genes200_response_inner import VariantsGenomicElementsGenes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariantsGenomicElementsGenes200ResponseInner from a JSON string
variants_genomic_elements_genes200_response_inner_instance = VariantsGenomicElementsGenes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(VariantsGenomicElementsGenes200ResponseInner.to_json())

# convert the object into a dict
variants_genomic_elements_genes200_response_inner_dict = variants_genomic_elements_genes200_response_inner_instance.to_dict()
# create an instance of VariantsGenomicElementsGenes200ResponseInner from a dict
variants_genomic_elements_genes200_response_inner_from_dict = VariantsGenomicElementsGenes200ResponseInner.from_dict(variants_genomic_elements_genes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


