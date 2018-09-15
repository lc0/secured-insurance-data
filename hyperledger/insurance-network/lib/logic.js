
/**
 * Sample transaction processor function.
 * @param {org.example.biznet.SampleTransaction} tx The sample transaction instance.
 * @transaction
 */
async function sampleTransaction(tx) {
    // Save the old value of the asset.
    let oldValue = tx.asset.value;
    // Update the asset with the new value.
    tx.asset.value = tx.newValue;
    // Get the asset registry for the asset.
    let assetRegistry = await getAssetRegistry('org.example.biznet.SampleAsset');
    // Update the asset in the asset registry.
    await assetRegistry.update(tx.asset);

}

/**
 * Sample transaction processor function.
 * @param {org.example.biznet.TradeHealthMeasurement} thm The sample transaction instance.
 * @transaction
 */
async function tradeHealthMeasurement(thm) {

    // Update the asset with new value for viewers.
    thm.healthMeasurement.viewers = thm.newViewers

    // Get the asset registry for the asset.
    let assetRegistry = await getAssetRegistry('org.example.biznet.HealthMeasurement');
    // Update the asset in the asset registry.
    await assetRegistry.update(thm.healthMeasurement);

}