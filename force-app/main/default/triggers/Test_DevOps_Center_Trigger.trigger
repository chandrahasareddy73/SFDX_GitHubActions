trigger Test_DevOps_Center_Trigger on Account (before insert) {
Account[] Acc = Trigger.new;
SampleApex.applyDiscount(Acc);
}