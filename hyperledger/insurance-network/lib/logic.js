/**
 * Track the trade of a commodity from one trader to another
 * @param {org.example.biznet.Trade} trade - the trade to be processed
 * @transaction
 */
async function tradeCommodity(trade) {
    console.log(trade);
    trade.healthMeasurement = trade.healthMeasurement;
    let assetRegistry = await getAssetRegistry('org.example.biznet.HealthMeasurement');
    await assetRegistry.update(trade.commodity);
}

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