export class Person {
  pfp: string;
  name: string;
  email: string;
  age: number;
  gender: string;
  phonesOwned: string[];
  phoneNo: string;
  interests: string[];
  plan: string;

  constructor(
    pfp: string,
    name: string,
    email: string,
    age: number,
    gender: string,
    phonesOwned: string[],
    phoneNo: string,
    interests: string[],
    plan: string
  ) {
    this.pfp = pfp;
    this.name = name;
    this.email = email;
    this.age = age;
    this.gender = gender;
    this.phonesOwned = phonesOwned;
    this.phoneNo = phoneNo;
    this.interests = interests;
    this.plan = plan;
  }
}
