@isTest(seeAllData=true)
public class Test_DevOps_Center_TestClass {
static testMethod void validateSampleApex() {
Account c = new Account(Name='BMW', DevOps_Center_Promote__c=100000);
 
Test.startTest();
insert c;
Test.stopTest();
 
// Retrieve the record
c = [SELECT DevOps_Center_Promote__c FROM Account WHERE Id =:c.Id];
 
// Test that the trigger correctly updated the price
System.assertEquals(90000, c.DevOps_Center_Promote__c);
}
}
