export class FaceInfo {
  pfp: string;
  name: string;
  isCustomer: boolean;

  constructor(pfp: string, name: string, isCustomer: boolean) {
    this.pfp = pfp;
    this.name = name;
    this.isCustomer = isCustomer;
  }
}
