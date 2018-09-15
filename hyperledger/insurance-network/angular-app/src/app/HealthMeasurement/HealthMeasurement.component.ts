/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { HealthMeasurementService } from './HealthMeasurement.service';
import 'rxjs/add/operator/toPromise';

@Component({
  selector: 'app-healthmeasurement',
  templateUrl: './HealthMeasurement.component.html',
  styleUrls: ['./HealthMeasurement.component.css'],
  providers: [HealthMeasurementService]
})
export class HealthMeasurementComponent implements OnInit {

  myForm: FormGroup;

  private allAssets;
  private asset;
  private currentId;
  private errorMessage;

  heartRate = new FormControl('', Validators.required);
  numberOfStepsInInterval = new FormControl('', Validators.required);
  datetimeBeginStepsInterval = new FormControl('', Validators.required);
  datetimeEndStepsInterval = new FormControl('', Validators.required);
  id = new FormControl('', Validators.required);
  viewer = new FormControl('', Validators.required);
  owner = new FormControl('', Validators.required);

  constructor(public serviceHealthMeasurement: HealthMeasurementService, fb: FormBuilder) {
    this.myForm = fb.group({
      heartRate: this.heartRate,
      numberOfStepsInInterval: this.numberOfStepsInInterval,
      datetimeBeginStepsInterval: this.datetimeBeginStepsInterval,
      datetimeEndStepsInterval: this.datetimeEndStepsInterval,
      id: this.id,
      viewer: this.viewer,
      owner: this.owner
    });
  };

  ngOnInit(): void {
    this.loadAll();
  }

  loadAll(): Promise<any> {
    const tempList = [];
    return this.serviceHealthMeasurement.getAll()
    .toPromise()
    .then((result) => {
      this.errorMessage = null;
      result.forEach(asset => {
        tempList.push(asset);
      });
      this.allAssets = tempList;
    })
    .catch((error) => {
      if (error === 'Server error') {
        this.errorMessage = 'Could not connect to REST server. Please check your configuration details';
      } else if (error === '404 - Not Found') {
        this.errorMessage = '404 - Could not find API route. Please check your available APIs.';
      } else {
        this.errorMessage = error;
      }
    });
  }

	/**
   * Event handler for changing the checked state of a checkbox (handles array enumeration values)
   * @param {String} name - the name of the asset field to update
   * @param {any} value - the enumeration value for which to toggle the checked state
   */
  changeArrayValue(name: string, value: any): void {
    const index = this[name].value.indexOf(value);
    if (index === -1) {
      this[name].value.push(value);
    } else {
      this[name].value.splice(index, 1);
    }
  }

	/**
	 * Checkbox helper, determining whether an enumeration value should be selected or not (for array enumeration values
   * only). This is used for checkboxes in the asset updateDialog.
   * @param {String} name - the name of the asset field to check
   * @param {any} value - the enumeration value to check for
   * @return {Boolean} whether the specified asset field contains the provided value
   */
  hasArrayValue(name: string, value: any): boolean {
    return this[name].value.indexOf(value) !== -1;
  }

  addAsset(form: any): Promise<any> {
    this.asset = {
      $class: 'org.example.biznet.HealthMeasurement',
      'heartRate': this.heartRate.value,
      'numberOfStepsInInterval': this.numberOfStepsInInterval.value,
      'datetimeBeginStepsInterval': this.datetimeBeginStepsInterval.value,
      'datetimeEndStepsInterval': this.datetimeEndStepsInterval.value,
      'id': this.id.value,
      'viewer': this.viewer.value,
      'owner': this.owner.value
    };

    this.myForm.setValue({
      'heartRate': null,
      'numberOfStepsInInterval': null,
      'datetimeBeginStepsInterval': null,
      'datetimeEndStepsInterval': null,
      'id': null,
      'viewer': null,
      'owner': null
    });

    return this.serviceHealthMeasurement.addAsset(this.asset)
    .toPromise()
    .then(() => {
      this.errorMessage = null;
      this.myForm.setValue({
        'heartRate': null,
        'numberOfStepsInInterval': null,
        'datetimeBeginStepsInterval': null,
        'datetimeEndStepsInterval': null,
        'id': null,
        'viewer': null,
        'owner': null
      });
      this.loadAll();
    })
    .catch((error) => {
      if (error === 'Server error') {
          this.errorMessage = 'Could not connect to REST server. Please check your configuration details';
      } else {
          this.errorMessage = error;
      }
    });
  }


  updateAsset(form: any): Promise<any> {
    this.asset = {
      $class: 'org.example.biznet.HealthMeasurement',
      'heartRate': this.heartRate.value,
      'numberOfStepsInInterval': this.numberOfStepsInInterval.value,
      'datetimeBeginStepsInterval': this.datetimeBeginStepsInterval.value,
      'datetimeEndStepsInterval': this.datetimeEndStepsInterval.value,
      'viewer': this.viewer.value,
      'owner': this.owner.value
    };

    return this.serviceHealthMeasurement.updateAsset(form.get('id').value, this.asset)
    .toPromise()
    .then(() => {
      this.errorMessage = null;
      this.loadAll();
    })
    .catch((error) => {
      if (error === 'Server error') {
        this.errorMessage = 'Could not connect to REST server. Please check your configuration details';
      } else if (error === '404 - Not Found') {
        this.errorMessage = '404 - Could not find API route. Please check your available APIs.';
      } else {
        this.errorMessage = error;
      }
    });
  }


  deleteAsset(): Promise<any> {

    return this.serviceHealthMeasurement.deleteAsset(this.currentId)
    .toPromise()
    .then(() => {
      this.errorMessage = null;
      this.loadAll();
    })
    .catch((error) => {
      if (error === 'Server error') {
        this.errorMessage = 'Could not connect to REST server. Please check your configuration details';
      } else if (error === '404 - Not Found') {
        this.errorMessage = '404 - Could not find API route. Please check your available APIs.';
      } else {
        this.errorMessage = error;
      }
    });
  }

  setId(id: any): void {
    this.currentId = id;
  }

  getForm(id: any): Promise<any> {

    return this.serviceHealthMeasurement.getAsset(id)
    .toPromise()
    .then((result) => {
      this.errorMessage = null;
      const formObject = {
        'heartRate': null,
        'numberOfStepsInInterval': null,
        'datetimeBeginStepsInterval': null,
        'datetimeEndStepsInterval': null,
        'id': null,
        'viewer': null,
        'owner': null
      };

      if (result.heartRate) {
        formObject.heartRate = result.heartRate;
      } else {
        formObject.heartRate = null;
      }

      if (result.numberOfStepsInInterval) {
        formObject.numberOfStepsInInterval = result.numberOfStepsInInterval;
      } else {
        formObject.numberOfStepsInInterval = null;
      }

      if (result.datetimeBeginStepsInterval) {
        formObject.datetimeBeginStepsInterval = result.datetimeBeginStepsInterval;
      } else {
        formObject.datetimeBeginStepsInterval = null;
      }

      if (result.datetimeEndStepsInterval) {
        formObject.datetimeEndStepsInterval = result.datetimeEndStepsInterval;
      } else {
        formObject.datetimeEndStepsInterval = null;
      }

      if (result.id) {
        formObject.id = result.id;
      } else {
        formObject.id = null;
      }

      if (result.viewer) {
        formObject.viewer = result.viewer;
      } else {
        formObject.viewer = null;
      }

      if (result.owner) {
        formObject.owner = result.owner;
      } else {
        formObject.owner = null;
      }

      this.myForm.setValue(formObject);

    })
    .catch((error) => {
      if (error === 'Server error') {
        this.errorMessage = 'Could not connect to REST server. Please check your configuration details';
      } else if (error === '404 - Not Found') {
        this.errorMessage = '404 - Could not find API route. Please check your available APIs.';
      } else {
        this.errorMessage = error;
      }
    });
  }

  resetForm(): void {
    this.myForm.setValue({
      'heartRate': null,
      'numberOfStepsInInterval': null,
      'datetimeBeginStepsInterval': null,
      'datetimeEndStepsInterval': null,
      'id': null,
      'viewer': null,
      'owner': null
      });
  }

}
