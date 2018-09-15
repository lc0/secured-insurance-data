/**
 * Track the trade of a commodity from one trader to another
 * @param {org.example.biznet.Trade} trade - the trade to be processed
 * @transaction
 */
async function tradeCommodity(trade) {
    trade.healthMeasurement = trade.healthMeasurement;
    let assetRegistry = await getAssetRegistry('org.example.biznet.HealthMeasurement');
    await assetRegistry.update(trade.commodity);
}