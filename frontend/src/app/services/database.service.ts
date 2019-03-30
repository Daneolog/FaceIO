import { Injectable } from '@angular/core';
import { Person } from '../models/person.model';
import { HttpClient } from '@angular/common/http';
import { FaceInfo } from '../models/faceInfo.model';
import { ReturnStatement } from '@angular/compiler';

export interface ListDict {
  [id: string]: FaceInfo;
}

export interface NamesDict {
  [tid: string]: string;
}

const HOST = 'http://10.136.8.228:5000';

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  constructor(private http: HttpClient) {
    // this.customers = {
    //   87422342: new Person(
    //     'https://media.licdn.com/dms/image/C5603AQG6BF4IsM7Eaw/profile-displayphoto-shrink_200_200/0?e=1559174400&v=beta&t=H0VDKP5cQA4zf-gdFLIhuOoNf2ANBi3AKCBF2JG2i-o',
    //     'Gabriel',
    //     [
    //       'Samsung Galaxy S6',
    //       'Samsung Galaxy S7',
    //       'Samsung Galaxy S8',
    //       'Samsung Galaxy S21312'
    //     ],
    //     '(201) 702-8828',
    //     ['photography', 'other stuff'],
    //     'Family Plan',
    //     'iPhone :)'
    //   ),
    //   87422343: new Person(
    //     'https://scontent-atl3-1.xx.fbcdn.net/v/t31.0-8/1926287_542834289163885_1403268875_o.jpg?_nc_cat=106&_nc_ht=scontent-atl3-1.xx&oh=a87047ab6817fe144e3e819b311b5d31&oe=5D4EB408',
    //     'Davi',
    //     [
    //       'Samsung Galaxy S6',
    //       'Samsung Galaxy S7',
    //       'Samsung Galaxy S8',
    //       'Samsung Galaxy S21312'
    //     ],
    //     '(201) 702-8828',
    //     ['photography', 'other stuff'],
    //     'Family Plan',
    //     'iPhone :)'
    //   ),
    //   87422344: new Person(
    //     'https://media.licdn.com/dms/image/C4E03AQG3LBDHObXo0g/profile-displayphoto-shrink_200_200/0?e=1559174400&v=beta&t=NWd2qgUlg5M9QBPi47znmbKJKj17cnUhrSQToBxAzOg',
    //     'Mati',
    //     [
    //       'Samsung Galaxy S6',
    //       'Samsung Galaxy S7',
    //       'Samsung Galaxy S8',
    //       'Samsung Galaxy S21312'
    //     ],
    //     '(201) 702-8828',
    //     ['photography', 'other stuff'],
    //     'Family Plan',
    //     'iPhone :)'
    //   ),
    //   87422345: new Person(
    //     'https://media.licdn.com/dms/image/C4E03AQG3LBDHObXo0g/profile-displayphoto-shrink_200_200/0?e=1559174400&v=beta&t=NWd2qgUlg5M9QBPi47znmbKJKj17cnUhrSQToBxAzOg'
    //   )
    // };
  }

  getFaces() {
    return this.http.get(`${HOST}/store/faces`);
  }

  getNames() {
    return this.http.get(`${HOST}/store/names`);
  }

  getCustomer(faceId) {
    return this.http.get(`${HOST}/customers/${faceId}`);
  }

  assignFace(faceId, tId) {
    return this.http.get(`${HOST}/store/faces/${faceId}/assign/${tId}`);
  }
}
