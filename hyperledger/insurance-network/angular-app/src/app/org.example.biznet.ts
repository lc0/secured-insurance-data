import {Asset} from './org.hyperledger.composer.system';
import {Participant} from './org.hyperledger.composer.system';
import {Transaction} from './org.hyperledger.composer.system';
import {Event} from './org.hyperledger.composer.system';
// export namespace org.example.biznet{
   export abstract class BaseAsset extends Asset {
      id: string;
      viewer: Insurance;
      owner: InsuredClient;
   }
   export class HealthMeasurement extends BaseAsset {
      heartRate: number;
      numberOfStepsInInterval: number;
      datetimeBeginStepsInterval: Date;
      datetimeEndStepsInterval: Date;
   }
   export abstract class Predictor extends Asset {
      key: string;
      probability: number;
   }
   export class PictureMeasurement extends BaseAsset {
      predictors: Predictor[];
      datetimeMeasurement: Date;
   }
   export class HealthcareContract extends BaseAsset {
      contractValidTo: Date;
      insurance: Insurance;
      insuredClient: InsuredClient;
   }
   export class BaseClient extends Participant {
      id: string;
      name: string;
   }
   export class Insurance extends BaseClient {
   }
   export class InsuredClient extends BaseClient {
      age: string;
   }
   export class tradeHealthMeasurement extends Transaction {
      healthMeasurement: HealthMeasurement;
      newViewer: Insurance;
   }
   export class Trade extends Transaction {
      healthMeasurement: HealthMeasurement;
   }
// }
